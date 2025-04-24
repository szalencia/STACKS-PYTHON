# STACKS 2D THURSDAY

import pygame
import random
import copy

def colorUpdate (colorLs):
    x = random.randint(0,2)
    y = random.randint(0,1)
    if ((colorLs[x]+75)>255):
        colorLs[x] -= 75
    elif ((colorLs[x]-75)<0):
        colorLs[x] += 75
    else:
        colorLs[x] = colorLs[x] + ((y-((y+1)%2))*75) # CONVERTING 0/1 TO -1/1 :)
    return colorLs

def fadeIn (x, colorSet):
    # colorSet = [present,target]
    for i in range (3):
        step = ((colorSet[1][i] - colorSet[0][i])//x)
        colorSet[0][i] += step
    return colorSet[0] # Returning the Updated colorSet[0] = present
'''
def push (vertices, x): # x=1 is DOWN(+ve) x=0 is UP(-ve)
    vertices[0][1] += ((x-((x+1)%2))*50)
    vertices[1][1] += ((x-((x+1)%2))*50)
    vertices[2][1] += ((x-((x+1)%2))*50)
    vertices[3][1] += ((x-((x+1)%2))*50)
    return vertices
'''
def pushUp (vertices):
    vertices[0][1] -= 50
    vertices[1][1] -= 50
    vertices[2][1] -= 50
    vertices[3][1] -= 50
    return vertices

def pushDn (vertices):
    vertices[0][1] += 50
    vertices[1][1] += 50
    vertices[2][1] += 50
    vertices[3][1] += 50
    return vertices

def renderAll ():
    for i in range (len(stackArray)):
        pygame.draw.polygon(win,colorArray[i],stackArray[i])
        pygame.display.update()
        

stackArray = []
colorArray = []
stackVertices = [[600,900],[1000,900],[1000,950],[600,950]]
timeElapsed = 0
fps = 100
timeDelay = 1000//fps
color=[255,255,255]
colorPresent = [0,0,0]
colorStep = 0
movementStack = "rev"

pygame.init()
win = pygame.display.set_mode((1600,900))
pygame.display.set_caption("TEST")
x = 0
loop = True
while loop :
    pygame.time.delay(timeDelay)

    # GAME INITIALISATION
    if timeElapsed < 2250: #2250/250 = 9, which is no. of initial stacks :)
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
    else: # Enters right when timeElapsed becomes 2250 at 9th stack :)
        if timeElapsed == 2250: # First instance
            stackArray.pop()
            colorArray.pop()
        pygame.draw.polygon(win,(0,0,0),stackVertices)
        if (movementStack == "rev"):
            stackVertices[0][0]-= 10
            stackVertices[1][0]-= 10
            stackVertices[2][0]-= 10
            stackVertices[3][0]-= 10
            if stackVertices[1][0]<=(stackArray[-1][0][0]-50):
                movementStack = "fwd"
        elif (movementStack == "fwd"):
            stackVertices[0][0]+= 10
            stackVertices[1][0]+= 10
            stackVertices[2][0]+= 10
            stackVertices[3][0]+= 10
            if stackVertices[0][0]>=(stackArray[-1][1][0]+50):
                movementStack = "rev"
        pygame.draw.polygon(win,color,stackVertices)

    
    # GAME LOGICS ENGINE
    x = pygame.event.get()
    for event in x :
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE :
                stackArray.append(copy.deepcopy(stackVertices))
                colorArray.append(copy.deepcopy(color))
                stackArray=list(map(pushDn,stackArray))
                color = colorUpdate(color)
                win.fill((0,0,0))
                renderAll()
            elif event.key == pygame.K_x:
                win.fill((0,0,0))
            elif event.key == pygame.K_v:
                renderAll()
                
        if event.type == pygame.QUIT :
            loop = False
    pygame.display.update()
    timeElapsed += timeDelay
pygame.quit()
