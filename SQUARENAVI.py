# PYTHON GAME MOVE SQUARE

import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("SQUARE NAVIGATE")
x = 100
y = 10
width = 50
height = 50
vel = 1
loop = True
t = 0
while loop :
    pygame.time.delay(1)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            loop = False
    t = t + 1
    # Either you can overwrite the old rectangle
    # pygame.draw.rect(win,(0,0,0),(x,y,width,height))
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_RIGHT] and x<=450) :
            x = x + vel
    if (keys[pygame.K_DOWN] and y<=450) :
            y = y + vel
    if (keys[pygame.K_UP] and y>0) :
            y = y - vel
    if (keys[pygame.K_LEFT] and x>0) :
            x = x - vel
    # Or you can overwrite the whole screen with old Black Background
    win.fill((0,0,0))
    pygame.draw.rect(win,(255,0,0),(x,y,width,height))
    pygame.display.update()
    #print(keys)
print("WINDOW OPENED FOR ~",t," MILLISECONDS")
pygame.quit()
