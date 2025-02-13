# pouzite balicky 
import os
import sys 
import math 
import random
import pygame # pridani balicku (frameworku) Pygame 
pygame.init() # priprava frameowrku k praci 
 
# PRIPRAVA APLIKACE 

velikost_x = 200
velikost_y = 50

ROZLISENI_OKNA_X = 800 
ROZLISENI_OKNA_Y = 600 
 
okno = pygame.display.set_mode((ROZLISENI_OKNA_X, ROZLISENI_OKNA_Y)) # vytvoreni okna pro vykreslovani 
pygame.display.set_caption('Tanky') 
 
casovac_FPS = pygame.time.Clock()

#priprava textur

#nacteni obrazku
aktualni_dir = os.path.dirname(__file__)
obrazek_cesta = os.path.join(aktualni_dir, 'textures', 'red_tank.png')
tank_r_small = pygame.image.load(obrazek_cesta)

#velikost obrazku
tank_r_x, tank_r_y = tank_r_small.get_size()
tank_r = pygame.transform.scale(tank_r_small, (tank_r_x * 3, tank_r_y * 3))
 
# priprava promennych 

stred_obrazovky = (ROZLISENI_OKNA_X//2, ROZLISENI_OKNA_Y//2)
stred_obrazovky_b = (ROZLISENI_OKNA_X//2 - velikost_x//2), (ROZLISENI_OKNA_Y//2 - velikost_y//2)

poloha_x = stred_obrazovky_b[0] 
poloha_y = stred_obrazovky_b[1] 

font = pygame.font.Font(None, 32) 

white = (255, 255, 255)
grey = (200, 200, 200)
red = (255, 0, 0)
blue = (0, 0, 255)

b_barva = [blue, blue, blue]
b_active = [False, False, False]

tank_r_rychlost = 0
tank_r_poloha_x = stred_obrazovky[0] - tank_r_x//2
tank_r_poloha_y = stred_obrazovky[1] - tank_r_y//2

# vykreslovaci smycka 
while True: 
    # OVLADANI APLIKACE 
    stisknute_klavesy = pygame.key.get_pressed()
    pozice_mysi = pygame.mouse.get_pos()
    LMB_active = pygame.mouse.get_pressed()[0]

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
     
    okno.fill((white)) # prebarveni okna jednolitou barvou 

    # menu
    def menu():
        button1 = pygame.Rect(poloha_x, (poloha_y - 100), velikost_x, velikost_y)
        pygame.draw.rect(okno, b_barva[0], button1)
        
        if button1.collidepoint(pozice_mysi):
            b_barva[0] = red
        else:
            b_barva[0] = blue

        if button1.collidepoint(pozice_mysi) and LMB_active == True:
            b_active[1] = True

        text1 = font.render("PvE", True, grey)
        text1_rect = text1.get_rect(center=button1.center)
        okno.blit(text1, text1_rect)

        button2 = pygame.Rect(poloha_x, (poloha_y), velikost_x, velikost_y)
        pygame.draw.rect(okno, b_barva[1], button2)
        
        if button2.collidepoint(pozice_mysi):
            b_barva[1] = red
        else:
            b_barva[1] = blue
        
        if button2.collidepoint(pozice_mysi) and LMB_active == True:
            b_active[1] = True

        text2 = font.render("PvP", True, grey)
        text2_rect = text2.get_rect(center=button2.center)
        okno.blit(text2, text2_rect)

        button3 = pygame.Rect(poloha_x, (poloha_y + 100), velikost_x, velikost_y)
        pygame.draw.rect(okno, b_barva[2], button3)
        
        if button3.collidepoint(pozice_mysi):
            b_barva[2] = red
        else:
            b_barva[2] = blue
        
        if button3.collidepoint(pozice_mysi) and LMB_active == True:
            b_active[2] = True

        text3 = font.render("Bossfight???", True, grey)
        text3_rect = text3.get_rect(center=button3.center)
        okno.blit(text3, text3_rect)

    if b_active[0] == False and b_active[1] == False and b_active[2] == False:
        menu()
    
    #Tank
    if b_active[0] == True or b_active[1] == True or b_active[2] == True:
        okno.blit(tank_r, (tank_r_poloha_x, tank_r_poloha_y))

    #pohyb
    if stisknute_klavesy[pygame.K_UP]:
        tank_r_rychlost = 2
        tank_r_poloha_y = tank_r_poloha_y - tank_r_rychlost
    else:
        tank_r_rychlost = 0
        tank_r_poloha_y = tank_r_poloha_y - tank_r_rychlost

    if stisknute_klavesy[pygame.K_DOWN]:
        tank_r_rychlost = -2
        tank_r_poloha_y = tank_r_poloha_y - tank_r_rychlost
    else:
        tank_r_rychlost = 0
        tank_r_poloha_y = tank_r_poloha_y - tank_r_rychlost
    
    pygame.display.update() # prehozeni framebufferu na displej

    casovac_FPS.tick(60) # omezeni FPS 