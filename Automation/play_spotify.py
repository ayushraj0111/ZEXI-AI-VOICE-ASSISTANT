import webbrowser
import pyautogui as ui
import time

def play_music_on_spotify(song_name):
    webbrowser.open("https://open.spotify.com/")
    time.sleep(5)  
    ui.click(300, 150) 
    time.sleep(1)
    ui.write(song_name)
    time.sleep(2)
    ui.press("enter")
    time.sleep(2)
    ui.leftClick(1150,390)
    # ui.leftClick(1150,390)