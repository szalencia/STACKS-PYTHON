# PYTHON GAME QUIT
# GAME OPTIMISED FOR 100FPS

import pygame
import random
import copy

pygame.init()
win = pygame.display.set_mode((1600,900))
pygame.display.set_caption("TEST")
loop = True

stackArray = []
colorArray = []
stackVertices = [[600,900],[1000,900],[1000,950],[600,950]]
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

def pushUp (vertices):
    vertices[0][1]-=50
    vertices[1][1]-=50
    vertices[2][1]-=50
    vertices[3][1]-=50
    return vertices

def renderAll (allcolors,allvertices):
    for i in range (len(allcolors)):
        pygame.draw.polygon(win,allcolors[i],allvertices[i])
        pygame.display.update()

while loop :
    pygame.time.delay(timeDelay)

    # GAME INITIALISATION
    if timeElapsed < 1250: #1250/250 = 5, which is no. of initial stacks :)
        if timeElapsed % 250 == 0:
            stackVertices = pushUp (stackVertices)
            stackArray.append(copy.deepcopy(stackVertices))
            color = colorUpdate(color)
            colorArray.append(color.copy())
            colorPresent = [0,0,0]
            colorStep = 25 # 250 miliseconds but 25 steps in total
        colorPresent = fadeIn(colorStep, [colorPresent,color])
        colorStep = colorStep-1
        pygame.draw.polygon(win,colorPresent,stackVertices)

    # GAME LOGICS RENDER
    else: # Enters right when timeElapsed becomes 1250 at 5th stack :)
        pygame.draw.polygon(win,color,stackVertices)
    
    # GAME LOGICS ENGINE
    x = pygame.event.get()
    for event in x :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                # pushUp (stackVertices)
                # win.fill((0,0,0))
                colorArray.pop(0)
                # stackArray.pop(0)
                color = colorUpdate(color)
                colorArray.append(color.copy())
                # stackArray.append(stackVertices)
                renderAll(colorArray,stackArray)
                print("SPACEBAR") # WILL BE USED LATER FOR GAMEPLAY
        if event.type == pygame.QUIT :
            loop = False
    pygame.display.update()
    timeElapsed += timeDelay
pygame.quit()
