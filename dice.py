import random
import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500


class Dice(pygame.sprite.Sprite):
    _type = "dice"

#       CONSTRUCTOR
    def __init__(self, widhtpos, heightpos):
        super(Dice, self).__init__()
        self._faces = 6

        self.images_still = []

        self.images_still.append(pygame.image.load('Assets\Dice\dice_still1.png'))
        self.images_still.append(pygame.image.load('Assets\Dice\dice_still2.png'))
        self.images_still.append(pygame.image.load('Assets\Dice\dice_still3.png'))
        self.images_still.append(pygame.image.load('Assets\Dice\dice_still4.png'))
        self.images_still.append(pygame.image.load('Assets\Dice\dice_still5.png'))
        self.images_still.append(pygame.image.load('Assets\Dice\dice_still6.png'))
        
        for i in range(0, len(self.images_still)):
            self.images_still[i] = pygame.transform.scale(self.images_still[i], (50, 50))


        self.index = 0
        self.image = self.images_still[self.index]
        self.rect = self.image.get_rect(center=(widhtpos, heightpos))



#       OVERRIDES
    def __str__(self):
        return f"A {self._faces} faces {self._type}"

    def __repr__(self):
        return self.__str__()

#       GETTERS
    def get_faces(self):
        return self._faces

    def get_index(self):
        return self.index

#       SETTERS
    def set_faces(self, new_faces):
        self._faces = new_faces

    def set_index(self, new_index):
        self.index = new_index

#       METHODS
    def roll(self):
        return random.randint(1, self._faces)

    def update(self):
        roll = self.roll()

        self.image = self.images_still[roll - 1]

        return roll





class RiggedDice(Dice):
    _type = "rigged dice"

#       CONSTRUCTOR
    def roll(self, rigged=False):
        return self._faces if rigged else super().roll()
