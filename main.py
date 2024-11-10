import mss
import time
import numpy as np 
import cv2 
import pytesseract
from gtts import gTTS
import pygame
import keyboard
import TexttoSpeech
import scroll_page

def main():
    previous_text = ''
    with open("screenRecog.py") as file:
        code = file.read()
        text = exec(code)
        print(text)
        #checks if we're at the end of the file by comparing the pervious results.
        if text == previous_text:
            exit()
        previous_text = text
        text_chunks = TexttoSpeech.split_text_into_chunks(str(text))
    file.close()

    audio_paused = False
    for i, chunk in enumerate(text_chunks): 
        textToRead = gTTS(text=chunk, lang='en', slow=False)
        filename = f'text_chunk_{i}.mp3'
        textToRead.save(filename)

        TexttoSpeech.playAudio(filename)
        if keyboard.is_pressed("spacebar") and not audio_paused:
            TexttoSpeech.pauseAudio()
            audio_paused = True
        elif keyboard.is_pressed("spacebar") and audio_paused:
            TexttoSpeech.resumeAudio()
            audio_paused = False

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    scroll_page.turn_page()
    main()
main()
