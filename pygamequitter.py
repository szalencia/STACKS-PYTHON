# PYTHON GAME QUIT

import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("TEST")
loop = True
while loop :
    pygame.time.delay(100)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            loop = False
pygame.quit()
