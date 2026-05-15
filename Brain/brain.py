from google import genai
import os
from datetime import datetime
from TextToSpeech.fast_DF_TTS import speak


API_KEY = "AIzaSyAPo2urOONOU2qaLHbcKYWlqq0rqwa9uys"
client = genai.Client(api_key=API_KEY)
MODEL_ID = "gemini-2.5-flash-lite"
HISTORY_FILE = r"P:\Studies\ZEXI ASSISTANT\ZEXI\chat_history.txt"


chat_session = client.chats.create(
    model=MODEL_ID, 
    config={
        "system_instruction": "You are a helpful voice assistant. Keep answers short and avoid markdown symbols."
    }
)

def log_chat(user_text, assistant_text):
    """Saves the conversation to a text file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n")
        f.write(f"You: {user_text}\n")
        f.write(f"Assistant: {assistant_text}\n")
        f.write("-" * 30 + "\n")

def process_input(user_text):
    """Sends input to Gemini, logs, prints, and speaks."""
    try:
        response = chat_session.send_message(user_text)
        assistant_reply = response.text

        log_chat(user_text, assistant_reply)

        print(f"Assistant: {assistant_reply}")
        speak(assistant_reply)

        return assistant_reply  # return AFTER everything is done

    except Exception as e:
        error_msg = f"Brain Error: {str(e)}"
        print(error_msg)
        speak(error_msg)
        return error_msg
    

    
# while True:
#     user_input = input("You: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("Exiting assistant. Goodbye!")
#         break
#     process_input(user_input)
