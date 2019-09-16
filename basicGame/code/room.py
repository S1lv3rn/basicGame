import pygame
WHITE = (255, 255, 255)
#clamC = pygame.image.load('arts/clamClose.png')

class Room():
    #This class represents a car. It derives from the "Sprite" class in Pygame.


    def __init__(self, name, bgRBG):
        # Call the parent class (Sprite) constructor

        self.col = bgRBG
        self.name = name
        self.visible = False
        self.roomObj = {}
        #self.descript
        #self.id
        #self.grabbable

    def addObj(self, s, name, pos, num):
        #add obj to objList
        if name in self.roomObj:
            self.addObj(s, s + str(num), pos, (num + 1))
        else:
            self.roomObj[name] = pos
