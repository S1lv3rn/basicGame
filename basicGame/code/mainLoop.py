## TODO:
## display a back ground colour (done)
## display bg objs
## make objs clickable ((-> change bg col to test))
## make room object
## display room objs
## put objs in bag ((add obj icons))

import pygame, time
from random import randint
from obj import Obj
from room import Room


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

def loadRooms():
    #porchDef = {"id": "porch", "art": ["obj1", "obj2"], "bjCol": BLUE}
    #get stuff from files
    pass

def displayRoom():
    #fill bg colour
    #draw each obj at certain pos
    pass

def loadObj():
    #for every line in objData.csv
    #1st ele is image, 2nd name
    pass

def gameLoop():
    # init variables
    # set room to porch
    # sprList is list of objects in the room

    gameExit = False
    #loadObj{
    box1 = Obj('../art/obj1.png', "obj1")
    box2 = Obj('../art/obj2.png', "obj2")
    #}
    uniqueObj = pygame.sprite.Group()
    #load obj {
    uniqueObj.add(box1)
    uniqueObj.add(box2)
    #}

    #loadRooms{
    intro = Room("porch", BLUE)
    intro.addObj("obj1", "obj1", (0, 0), 0)
    intro.addObj("obj2", "obj2", (200, 200), 0)

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     pos = event.pos
            #
            #     for sprite in uniqueObj:
            #        if sprite.rect.collidepoint(pos):
            #              print("OPEN")
                         #stuff happens here
            print(event)

        #displayRoom{
        #change bg colour
        gameDisplay.fill(intro.col)
        for o in intro.roomObj:
            print()
            print("ST - ", o)
            for s in uniqueObj.sprites():
                print("ST2 - ", s.name)
                if o.startswith(s.name):
                    print("FOUND")
                    s.rect.x, s.rect.y = intro.roomObj[o]
                    s.update()
                    s.draw(gameDisplay)
                    break
        #}

        pygame.display.update()
        clock.tick(60)

gameLoop()
pygame.quit()
quit()
