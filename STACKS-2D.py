# STACKS 2D THURSDAY

import pygame
import random
import copy


def colorUpdate(colorLs):
    x = random.randint(0, 2)
    y = random.randint(0, 1)
    if ((colorLs[x] + 100) > 255):
        colorLs[x] -= 100
    elif ((colorLs[x] - 100) < 0):
        colorLs[x] += 100
    else:
        colorLs[x] = colorLs[x] + ((y - ((y + 1) % 2)) * 100)  # CONVERTING 0/1 TO -1/1 :)
    return colorLs


def fadeIn(x, colorSet):
    # colorSet = [present,target]
    for i in range(3):
        step = ((colorSet[1][i] - colorSet[0][i]) // x)
        colorSet[0][i] += step
    return colorSet[0]  # Returning the Updated colorSet[0] = present


'''
def push (vertices, x): # x=1 is DOWN(+ve) x=0 is UP(-ve)
    vertices[0][1] += ((x-((x+1)%2))*50)
    vertices[1][1] += ((x-((x+1)%2))*50)
    vertices[2][1] += ((x-((x+1)%2))*50)
    vertices[3][1] += ((x-((x+1)%2))*50)
    return vertices
'''


def pushUp(vertices):
    vertices[0][1] -= 50
    vertices[1][1] -= 50
    vertices[2][1] -= 50
    vertices[3][1] -= 50
    return vertices


def pushDn(vertices):
    vertices[0][1] += 50
    vertices[1][1] += 50
    vertices[2][1] += 50
    vertices[3][1] += 50
    return vertices


def renderAll():
    win.fill((0, 0, 0))
    for i in range(len(stackArray)):
        pygame.draw.polygon(win, colorArray[i], stackArray[i])
        pygame.display.update()


stackArray = []
colorArray = []
stackVertices = [[600, 900], [1000, 900], [1000, 950], [600, 950]]
timeElapsed = 0
fps = 100
timeDelay = 1000 // fps
color = [255, 255, 255]
colorPresent = [0, 0, 0]
colorStep = 0
movementStack = "rev"
vel = 10
toughness = 5
colorFont = [0, 0, 0]
pointer = (0, 0)

pygame.init()
win = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("TEST")
x = 0
font = pygame.font.Font(None, 48)
menu = True

loop = True


class MenuItem:
    def __init__(self, s):
        y = int(s[0])
        y = 150 + 50 * (y)
        r = s[-1] * 255
        s = s[1:-1:1]  # 1Start Game1 = 1st option, Start Game, Red
        selfText = font.render(s, True, (r, 0, 0), (100, y))
        rect = selfText.get_rect(topleft=(100, y))

    def renderText(self, ):
        win.blit(selfText, (100, y))


while menu:
    pygame.time.delay(timeDelay)
    # GAME INITIALISATION
    if timeElapsed < 2250:  # 2250/250 = 9, which is no. of initial stacks :)
        if timeElapsed % 250 == 0:
            stackVertices = pushUp(stackVertices)
            # stackVertices = push (stackVertices,0 )
            stackArray.append(copy.deepcopy(stackVertices))
            color = colorUpdate(color)
            colorArray.append(color.copy())
            colorPresent = [0, 0, 0]
            colorStep = 25  # 250 miliseconds but 25 steps in total
        colorPresent = fadeIn(colorStep, [colorPresent, color])
        colorStep = colorStep - 1
        pygame.draw.polygon(win, colorPresent, stackVertices)
        pygame.display.update()
    else:
        if timeElapsed == 2250:  # Menu Fading in at first instance
            stackArray.pop()
            colorArray.pop()
            for i in range(100):
                colorFont = fadeIn(100 - i, [colorFont, (255, 255, 255)])
                pygame.time.delay(timeDelay)
                timeElapsed += timeDelay
                win.blit(font.render("STACKS 2D", True, colorFont), (100, 100))
                win.blit(font.render("New Game", True, colorFont), (100, 200))
                win.blit(font.render("Level", True, colorFont), (100, 250))
                win.blit(font.render("Quit Game", True, colorFont), (100, 300))
                pygame.display.update()
        else:  # Normal Menu in Continuation
            menuGame = font.render("New Game", True, (255, 255, 255))
            menuLevel = font.render("Level", True, (255, 255, 255))
            menuQuit = font.render("Quit Game", True, (255, 255, 255))

            win.blit(font.render("STACKS 2D", True, (255, 255, 255)), (100, 100))

            menuGameRect = menuGame.get_rect(topleft=(100, 200))
            menuLevelRect = menuLevel.get_rect(topleft=(100, 250))
            menuQuitRect = menuQuit.get_rect(topleft=(100, 300))

            pygame.display.update()

            pointer = pygame.mouse.get_pos()
            menuEvents = pygame.event.get()
            # '''
            for event in menuEvents:
                if menuGameRect.collidepoint(pointer):
                    win.blit(font.render("New Game", True, (255, 0, 0)), (100, 200))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pointer)
                        menu = False
                        win.fill((0, 0, 0))
                        renderAll()

                elif menuLevelRect.collidepoint(pointer):
                    win.blit(font.render("Level", True, (255, 0, 0)), (100, 250))

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        win.fill((0, 0, 0))
                        win.blit(font.render("STACKS 2D", True, colorFont), (100, 100))
                        win.blit(font.render("Easy", True, colorFont), (100, 200))
                        win.blit(font.render("Medium", True, colorFont), (100, 250))
                        win.blit(font.render("Hard", True, colorFont), (100, 300))
                        pygame.display.update()
                        pygame.time.delay(2000)  # DELAY ADDED TESTING
                        win.fill((0, 0, 0))


                elif menuQuitRect.collidepoint(pointer):
                    win.blit(font.render("Quit Game", True, (255, 0, 0)), (100, 300))
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        print(pointer)
                        menu = False
                        loop = False
                        win.fill((0, 0, 0))
                        win.blit(font.render("STACKS 2D", True, colorFont), (100, 100))
                        win.blit(font.render("Game Quitting", True, colorFont), (100, 200))
                        pygame.display.update()
                        pygame.time.delay(500)  # GAME QUITTING DELAY
                else:
                    win.blit(menuGame, (100, 200))
                    win.blit(menuLevel, (100, 250))
                    win.blit(menuQuit, (100, 300))

            pygame.display.update()
    timeElapsed += timeDelay

# menu above

while loop:
    pygame.time.delay(timeDelay)
    # Enters right when timeElapsed becomes 2250 at 9th stack :)
    vel = ((stackVertices[1][0] - stackVertices[0][0]) / 40) + toughness
    pygame.draw.polygon(win, (0, 0, 0), stackVertices)
    if (movementStack == "rev"):
        stackVertices[0][0] -= vel
        stackVertices[1][0] -= vel
        stackVertices[2][0] -= vel
        stackVertices[3][0] -= vel
        if stackVertices[1][0] <= 550:
            movementStack = "fwd"
    elif (movementStack == "fwd"):
        stackVertices[0][0] += vel
        stackVertices[1][0] += vel
        stackVertices[2][0] += vel
        stackVertices[3][0] += vel
        if stackVertices[0][0] >= 1050:
            movementStack = "rev"
    pygame.draw.polygon(win, color, stackVertices)

    # GAME LOGICS ENGINE
    x = pygame.event.get()
    for event in x:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if ((stackVertices[1][0] - stackVertices[0][0]) < 2):
                    print("GAME ENDS HERE")
                    pygame.time.delay(1000)
                    loop = False
                elif ((stackVertices[0][0] < stackArray[-1][0][0]) and (stackVertices[1][0] > stackArray[-1][0][0])):
                    # LEFT SIDE EXTRA
                    stackVertices[0][0] = stackArray[-1][0][0]
                    stackVertices[3][0] = stackArray[-1][3][0]
                elif ((stackVertices[1][0] > stackArray[-1][1][0]) and (stackVertices[0][0] < stackArray[-1][1][0])):
                    # RIGHT SIDE EXTRA
                    stackVertices[1][0] = stackArray[-1][1][0]
                    stackVertices[2][0] = stackArray[-1][2][0]
                else:
                    print("GAME ENDS HERE")
                    pygame.time.delay(1000)
                    loop = False
                stackArray.append(copy.deepcopy(stackVertices))
                colorArray.append(copy.deepcopy(color))
                stackArray = list(map(pushDn, stackArray))
                color = colorUpdate(color)
                win.fill((0, 0, 0))
                renderAll()
            elif event.key == pygame.K_x:
                win.fill((0, 0, 0))
            elif event.key == pygame.K_v:
                renderAll()

        if event.type == pygame.QUIT:
            loop = False
    pygame.display.update()
    timeElapsed += timeDelay
pygame.quit()
