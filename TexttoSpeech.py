from gtts import gTTS
import pygame
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

"""pdf_path = input("Enter the path to your PDF file: ") 
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
doc.close()"""

pygame.mixer.init()

def playAudio(filename):
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

def pauseAudio():
    pygame.mixer.music.pause()

def resumeAudio():
    pygame.mixer.music.unpause() 


