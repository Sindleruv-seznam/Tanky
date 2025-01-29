# pouzite balicky
import sys

import pygame # pridani balicku (frameworku) Pygame
pygame.init() # priprava frameowrku k praci

pygame.display.set_mode((800, 600)) # vytvoreni okna pro vykreslovani

# vykreslovaci smycka
while True:
    # detekce udalosti v aplikaci
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit() # vypnuti frameworku
            sys.exit()    # vypnuti cele aplikace
    
    pygame.display.update() # prehozeni framebufferu na displej
