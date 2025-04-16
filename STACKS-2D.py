# PYTHON GAME QUIT
# GAME OPTIMISED FOR 100FPS

import pygame
import random

pygame.init()
win = pygame.display.set_mode((1600,900))
pygame.display.set_caption("TEST")
loop = True

stacksArray = []
A,B,C,D = [600,850],[1000,850],[1000,900],[600,900]
timeElapsed = 0
fps = 100
timeDelay = 1000//fps
color=[100,100,100]

# COLOR UPDATE IS NICELY WORKING SO DON'T TOUCH :')
def colorUpdate (colorLs):
    x = random.randint(0,2)
    y = random.randint(0,1)
    if ((colorLs[x]+100)>255):
        colorLs[x] -= 100
    elif ((colorLs[x]-100)<0):
        colorLs[x] += 100
    else:
        colorLs[x] = colorLs[x] + ((y-((y+1)%2))*100) # CONVERTING 0/1 TO -1/1 :)
    return colorLs

while loop :
    pygame.time.delay(timeDelay)
    timeElapsed += timeDelay
    if timeElapsed <= 1000:
        if timeElapsed % 250 == 0:
            A[1]-=50
            B[1]-=50
            C[1]-=50
            D[1]-=50
        pygame.draw.polygon(win,list(color),(A,B,C,D))
        color = colorUpdate(color)

    # GAME LOGIC
    
    x = pygame.event.get()
    for event in x :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                print("SPACEBAR")
        if event.type == pygame.QUIT :
            loop = False
    pygame.display.update()
pygame.quit()
