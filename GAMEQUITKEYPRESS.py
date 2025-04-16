# PYTHON GAME QUIT

import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("TEST")
loop = True
while loop :
    pygame.time.delay(100)
    x = pygame.event.get()
    for event in x :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                print("SPACEBAR")
        if event.type == pygame.QUIT :
            loop = False
pygame.quit()
