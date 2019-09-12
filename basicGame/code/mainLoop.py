## TODO:
## display a back ground colour (done)
## display bg objs
## make objs clickable ((-> change bg col to test))
## make room object
## display room objs
## put objs in bag ((add obj icons))

import pygame, time
from random import randint
from roomObj import Obj


pygame.init()
display_width = 700
display_height = 400

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (62, 114, 165)
RED = (255,0,0)
ORE = (248, 192, 58)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Basic Game')
clock = pygame.time.Clock()

## load in objs

def changeRoom(nuRoom):
    pass

def displayRoom(room):
    pass

def loadRooms():
    #porchDef = {"id": "porch", "art": ["obj1", "obj2"], "bjCol": BLUE}
    pass

def gameLoop():
    # init variables
    # set room to porch
    # sprList is list of objects in the room

    gameExit = False
    box1 = Obj(pygame.image.load('arts/obj1.png'))
    box2 = Obj(pygame.image.load('arts/obj2.png'))
    sprList.add(box1)
    sprList.add(box2)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                for sprite in sprList:
                   if sprite.rect.collidepoint(pos):
                         print("OPEN")
                         #stuff happens here
            print(event)
        #change bg colour
        gameDisplay.fill(BLUE)
        box1.update()
        box2.update()
        box1.draw(gameDisplay)
        box2.draw(gameDisplay)

        ##sprList.update()
        ##sprList.draw(gameDisplay)
        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()
