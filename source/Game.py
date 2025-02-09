# pouzite balicky
import sys
import math

import pygame # pridani balicku (frameworku) Pygame
pygame.init() # priprava frameowrku k praci

# PRIPRAVA APLIKACE

ROZLISENI_OKNA_X = 800
ROZLISENI_OKNA_Y = 600

okno = pygame.display.set_mode((ROZLISENI_OKNA_X, ROZLISENI_OKNA_Y)) # vytvoreni okna pro vykreslovani
pygame.display.set_caption('Pong')

casovac_FPS = pygame.time.Clock()

# priprava promennych
velikost_x = 200
velikost_y = 50

stred_obrazovky = (ROZLISENI_OKNA_X//2) - velikost_x//2, ROZLISENI_OKNA_Y//2 - velikost_y//2
poloha_x = stred_obrazovky[0]
poloha_y = stred_obrazovky[1]

rychlost = 5 # pixely / frame
uhel = 30    # uhel pohybu ve stupnich

font = pygame.font.Font(None, 50)

# vykreslovaci smycka
while True:
    # OVLADANI APLIKACE
    
    # detekce udalosti v aplikaci
    for udalost in pygame.event.get():
        # detekce udalosti vypnuti aplikace (krizkem nebo ALT+F4)
        if udalost.type == pygame.QUIT:
            pygame.quit() # vypnuti frameworku
            sys.exit()    # vypnuti cele aplikace
        # detekce stisku klavesy Escape
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
    
    # VYKRESLOVANI APLIKACE
    
    okno.fill((0, 200, 250)) # prebarveni okna jednolitou barvou
    
    #pozice mysi
    pozice_mysi = pygame.mouse.get_pos()
button_rect = pygame.Rect(poloha_x, poloha_y, velikost_x, velikost_y)

# Check for mouse click
for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:  # When mouse button is pressed
        if button_rect.collidepoint(pozice_mysi):  # If mouse is over button
            print("Button was clicked!")
            # You can add any action you want here
            
# Draw the button (red when hovered, gray normally)
if button_rect.collidepoint(pozice_mysi):
    pygame.draw.rect(okno, (255, 0, 0), button_rect)  # Red when hovered
else:
    pygame.draw.rect(okno, (128, 128, 128), button_rect)  # Gray normally

    # menu
    pygame.draw.rect(okno, (100, 100, 100), (poloha_x, (poloha_y), velikost_x, velikost_y))


    pygame.display.update() # prehozeni framebufferu na displej
    
    casovac_FPS.tick(60) # omezeni FPS
