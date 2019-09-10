import pygame
WHITE = (255, 255, 255)
clamC = pygame.image.load('arts/clamClose.png')

class Obj(pygame.sprite.Sprite):
    #This class represents a car. It derives from the "Sprite" class in Pygame.


    def __init__(self, image):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self, )

        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()
        #self.descript
        #self.id
        #self.grabbable
        
