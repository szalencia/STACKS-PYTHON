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
color=[255,255,255]
colorPresent = [0,0,0]
colorStep = 0

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


def fadeIn (x, colorSet):
    # colorSet = [present,target]
    for i in range (3):
        step = ((colorSet[1][i] - colorSet[0][i])//x)
        colorSet[0][i] += step
    return colorSet[0] # Returning the Updated colorSet[0] = present


while loop :
    pygame.time.delay(timeDelay)

    # GAME INITIALISATION
    if timeElapsed <= 1000:
        if timeElapsed % 250 == 0:
            A[1]-=50
            B[1]-=50
            C[1]-=50
            D[1]-=50
            color = colorUpdate(color)
            colorPresent = [0,0,0]
            colorStep = 25 # 250 miliseconds but 25 steps in total
        colorPresent = fadeIn(colorStep, [colorPresent,color])
        colorStep = colorStep-1
        pygame.draw.polygon(win,colorPresent,(A,B,C,D))
    
    # GAME LOGICS
    x = pygame.event.get()
    for event in x :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                print("SPACEBAR") # WILL BE USED LATER FOR GAMEPLAY
        if event.type == pygame.QUIT :
            loop = False
    pygame.display.update()
    timeElapsed += timeDelay
    
pygame.quit()
