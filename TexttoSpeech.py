from gtts import gTTS
import pygame
import time 
import fitz  
#import keyboard

def split_text_into_chunks(text, max_length=500):
    words = text.split()
    chunks = []
    current_chunk = []
    current_length = 0
    for word in words:
        current_length += len(word) + 1 
        if current_length > max_length:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = len(word) + 1
        current_chunk.append(word)
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

pdf_path = input("Enter the path to your PDF file: ") 
try:
    doc = fitz.open(pdf_path)
except Exception as e:
    print(f"Error opening file: {e}")
    exit() 
texts = ''
for page_num in range(doc.page_count):
    page = doc.load_page(page_num) 
    texted = page.get_text() 
    print(f"Page {page_num + 1}:")
    print(texted)
    print("\n" + "-"*50 + "\n") 
    texts += texted + ' '  
doc.close()

text_chunks = split_text_into_chunks(texts)
language = 'en'
pygame.mixer.init()

def playAudio():
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def pauseAudio():
    pygame.mixer.music.pause()

def resumeAudio():
    pygame.mixer.music.unpause() 

for i, chunk in enumerate(text_chunks): 
    textToRead = gTTS(text=chunk, lang=language, slow=False)
    filename = f'text_chunk_{i}.mp3'
    textToRead.save(filename)

    playAudio()
    time.sleep(4)
    pauseAudio()
    print("Paused for 2 seconds...")
    time.sleep(2)
    resumeAudio()
    print("Resumed playing...")

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

