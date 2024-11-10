import pygame as pyg
import sys
import main

pyg.init()

screen = pyg.display.set_mode((600, 600))
background = pyg.image.load("UiDesign1.png").convert_alpha()
backgroundRect = background.get_rect(topleft=(0, 0))

playRect = pyg.Rect(160, 300, 280, 60) # 160, 300, 280, 60
pauseRect = pyg.Rect(160, 380, 280, 60) # 160, 380, 280, 60

playButton = pyg.Surface((150, 50), pyg.SRCALPHA)  # Transparent button surface
playButton.fill((0, 0, 0, 0)) 

pauseButton = pyg.Surface((150, 50), pyg.SRCALPHA)
pauseButton.fill((0, 0, 0, 0)) 

running = True
running_main = False
while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        elif event.type == pyg.MOUSEBUTTONDOWN:
            if playRect.collidepoint(event.pos) and not running_main:
                main.main()
                running_main = True
            elif pauseRect.collidepoint(event.pos) and running_main:
                running = False

    screen.blit(background, backgroundRect)

    pyg.display.flip()


pyg.quit()

#source myenv/bin/activate