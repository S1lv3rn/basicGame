## TODO:
## display a back ground colour (done)
## display bg objs
## make objs clickable ((-> change bg col to test))
## make room object
## display room objs
## put objs in bag ((add obj icons))

import pygame, time
from random import randint
#from clamObj import Clam


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


def gameLoop():
    # init variables
    # set room to porch
    # sprList is list of objects in the room

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                # for sprite in sprList:
                #    if sprite.rect.collidepoint(pos):
                #          print("OPEN")
                #          sprite.change()
                         #stuff happens here
            print(event)
        #change bg colour
        gameDisplay.fill(BLUE)

        ##sprList.update()
        ##sprList.draw(gameDisplay)
        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()
