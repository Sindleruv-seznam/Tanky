# pouzite balicky 
import os
import sys 
import math 
import random
import copy
import pygame # pridani balicku (frameworku) Pygame 
pygame.init() # priprava frameowrku k praci 
 
# PRIPRAVA APLIKACE 

velikost_x = 200
velikost_y = 50

ROZLISENI_OKNA_X = 2560
ROZLISENI_OKNA_Y = 1440
 
okno = pygame.display.set_mode((ROZLISENI_OKNA_X, ROZLISENI_OKNA_Y)) # vytvoreni okna pro vykreslovani 
pygame.display.set_caption('Tank trouble') 
 
casovac_FPS = pygame.time.Clock()

#priprava textur

#nacteni obrazku
aktualni_dir = os.path.dirname(__file__)
obrazek_cesta_tank_r = os.path.join(aktualni_dir, 'textures', 'red_tank.png')
tank_r_small = pygame.image.load(obrazek_cesta_tank_r).convert_alpha()
obrazek_cesta_cannon_ball = os.path.join(aktualni_dir, 'textures', 'canon_shot.png')
cannon_ball = pygame.image.load(obrazek_cesta_cannon_ball).convert_alpha()

#velikost obrazku
tank_r_x, tank_r_y = tank_r_small.get_size()
tank_r_x = tank_r_x * 2
tank_r_y = tank_r_y * 2
tank_r = pygame.transform.scale(tank_r_small, (tank_r_x, tank_r_y))
strela_r_x, strela_r_y = cannon_ball.get_size()
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
tank_r_poloha = [stred_obrazovky[0] - tank_r_x//2, stred_obrazovky[1] - tank_r_y//2]

tank_r_uhel = 90
tank_r_rotace_rychlost = 3

strela_r_rychlost = 5
strela_r_poloha = [tank_r_poloha[0], tank_r_poloha[1]]
strela_r_1 = False
strela_r_1_duration = 0

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
        if udalost.type == pygame.KEYDOWN and b_active[0] == False and b_active[1] == False and b_active[2] == False :  
            if udalost.key == pygame.K_ESCAPE:  
                pygame.quit()  
                sys.exit()  
 

    if stisknute_klavesy[pygame.K_ESCAPE]:
        b_active[0] = False 
        b_active[1] = False 
        b_active[2] = False
        tank_r_poloha[0] = (stred_obrazovky[0] - tank_r_x//2)
        tank_r_poloha[1] = (stred_obrazovky[1] - tank_r_y//2)
        tank_r_uhel = 90
        strela_r_poloha[0] = (tank_r_poloha[0] + tank_r_x//2)
        strela_r_poloha[1] = (tank_r_poloha[1] + tank_r_y//2)
        strela_r_1 = False


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
    
#strelba
    if stisknute_klavesy[pygame.K_SPACE] and strela_r_1 == False and (b_active[0] == True or b_active[1] == True or b_active[2] == True):
        strela_r_1 = True
        strela_r_1_duration = 0
        strela_r_uhel = copy.copy(tank_r_uhel)
        strela_r_poloha[0] = (tank_r_poloha[0] + tank_r_x//2) - strela_r_x//2
        strela_r_poloha[1] = (tank_r_poloha[1] + tank_r_y//2) - strela_r_y//2

    if stisknute_klavesy[pygame.K_SPACE] and strela_r_1 == False and (b_active[0] == True or b_active[1] == True or b_active[2] == True):
        strela_r_1 = True
        strela_r_uhel = copy.copy(tank_r_uhel)

    if strela_r_1_duration == 600:
        strela_r_1 = False
    elif strela_r_1 == True and (b_active[0] == True or b_active[1] == True or b_active[2] == True):
        okno.blit(cannon_ball, (strela_r_poloha[0], strela_r_poloha[1]))
        strela_r_poloha[0] += math.cos(math.radians(strela_r_uhel)) * strela_r_rychlost
        strela_r_poloha[1] -= math.sin(math.radians(strela_r_uhel)) * strela_r_rychlost
        strela_r_1_duration += 1
    
    if strela_r_poloha[0] > ROZLISENI_OKNA_X - strela_r_x:
        strela_r_uhel = (180 - strela_r_uhel) % 360
    if strela_r_poloha[0] < 0:
        strela_r_uhel = (180 - strela_r_uhel) % 360
    if strela_r_poloha[1] > ROZLISENI_OKNA_Y - strela_r_y:
        strela_r_uhel = (360 - strela_r_uhel) % 360
    if strela_r_poloha[1] < 0:
        strela_r_uhel = (360 - strela_r_uhel) % 360
        
    #Tank
    if b_active[0] == True or b_active[1] == True or b_active[2] == True:
        # Rotace tanku
        if stisknute_klavesy[pygame.K_LEFT]:
            tank_r_uhel = (tank_r_uhel + tank_r_rotace_rychlost) % 360
        if stisknute_klavesy[pygame.K_RIGHT]:
            tank_r_uhel = (tank_r_uhel - tank_r_rotace_rychlost) % 360
            
        # Vytvoreni rotovaneho obrazku
        rotovany_tank = pygame.transform.rotate(tank_r, tank_r_uhel)
        # Ziskani noveho obdelniku pro rotovany obrazek
        tank_rect = rotovany_tank.get_rect(center=(tank_r_poloha[0] + tank_r_x//2, tank_r_poloha[1] + tank_r_y//2))
        # Vykresleni rotovaneho tanku
        okno.blit(rotovany_tank, tank_rect.topleft)

    #pohyb
    if stisknute_klavesy[pygame.K_UP]:
        tank_r_rychlost = 3
        tank_r_poloha[0] += math.cos(math.radians(tank_r_uhel)) * tank_r_rychlost
        tank_r_poloha[1] -= math.sin(math.radians(tank_r_uhel)) * tank_r_rychlost
    else:
        tank_r_rychlost = 0
        tank_r_poloha[1] = tank_r_poloha[1] - tank_r_rychlost

    if stisknute_klavesy[pygame.K_DOWN]:
        tank_r_rychlost = 2
        tank_r_poloha[0] -= math.cos(math.radians(tank_r_uhel)) * tank_r_rychlost
        tank_r_poloha[1] += math.sin(math.radians(tank_r_uhel)) * tank_r_rychlost
    else:
        tank_r_rychlost = 0
        tank_r_poloha[1] = tank_r_poloha[1] - tank_r_rychlost

    #kolize s hranou okna
    if tank_r_poloha[0] > ROZLISENI_OKNA_X - tank_r_x:
        tank_r_poloha[0] = ROZLISENI_OKNA_X - tank_r_x
    if tank_r_poloha[0] < 0:
        tank_r_poloha[0] = 0
    if tank_r_poloha[1] > ROZLISENI_OKNA_Y - tank_r_y:
        tank_r_poloha[1] = ROZLISENI_OKNA_Y - tank_r_y
    if tank_r_poloha[1] < 0:
        tank_r_poloha[1] = 0
    pygame.display.update() # prehozeni framebufferu na displej

    casovac_FPS.tick(60) # omezeni FPS