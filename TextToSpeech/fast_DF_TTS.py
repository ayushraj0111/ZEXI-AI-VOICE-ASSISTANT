import asyncio
import threading
import  os 
import edge_tts
import pygame

voice = "hi-IN-SwaraNeural"
BUFFER_SIZE = 1024

def remove_file(file_path):
    max_attempts = 5
    attpemts = 0
    while attpemts < max_attempts:  
         with open (file_path, "wb"):
           pass
           os.remove(file_path)
           break
    
async def amain(TEXT, output_path) -> None:
    try:
        cm_txt = edge_tts.Communicate(TEXT, voice)
        await cm_txt.save(output_path)
        thread= threading.Thread(target=play_audio, args=(output_path,))
        thread.start()
        thread.join()
        
    except Exception as e:
        print(f"Error: {e}")
    
    
        
def play_audio(file_path):
    try:
     pygame.init()
     pygame.mixer.init()
     sound = pygame.mixer.Sound(file_path)
     sound.play()
     
     while pygame.mixer.get_busy():
         pygame.time.Clock().tick(10)
     pygame.quit()
     
    except Exception as e:
        print(f"Error: {e}")

def speak(TEXT, output_file= None):
    try:
       if output_file is None:
         output_file = f"{os.getcwd()}/speech.mp3"
       asyncio.run(amain(TEXT, output_file))
    except Exception as e:
        print(f"Error: {e}")
    
    
# speak("namaste, aap kaise ho, aapka kya halchal hai  ")
# speak("aapka din kaisa raha, mujhe ummeed hai ki aapka din accha raha hoga")
