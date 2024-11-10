import mss
import time
import numpy as np 
import cv2 
import pytesseract
from gtts import gTTS
import pygame
import keyboard
import TexttoSpeech
import screenRecog
import os

previous_text = ''
def main(previous_text, x=0,y=0,width=1280, height=800):

    image = screenRecog.getImage(x,y,width,height)
    text = image.screenshot()
    print(text)
    if text == previous_text:
        exit()
    previous_text = text
    text_chunks = TexttoSpeech.split_text_into_chunks(str(text))

    #idk how this for loop works but it plays the audio
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
            #if not pygame.mixer.music.get_busy():
                #is_running = False
