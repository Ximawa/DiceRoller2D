import time
import pygame
import random
from dice import *
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

class Character(pygame.sprite.Sprite):
    _type = "character"

#       CONTRUCTOR 
    def __init__(self, name, hp_max, attack, defense, dice, player_two):

        # SPRITE INITIALIZATION
        super(Character, self).__init__()
        self.images_idle = []
        self.images_attack = []
        self.index = 0
        self.attacking = False
        self.attacked = False
        self.rolling = False
        self.idle = True
        self.interval = 0
        self.interval_max = 2
        




        # CHARACTER STATS
        self._name = name
        self._hp_max = hp_max
        self._hp = hp_max
        self._attack = attack
        self._defense = defense
        self._dice = dice

        # VARIABLES
        self._player_two = player_two
        self._last_damages = 0
        

#       SUPERMETHODS
    def __str__(self):
        return f"Hello, my name is {self._name}, i'm a {self._type} with {self._hp}/{self._hp_max} HP"

#       GETTERS
    def get_name(self):
        return f"@{self._name}[{self._type}]"

    def get_hp_max(self):
        return self._hp_max

    def get_hp(self):
        return self._hp

    def get_attack(self):
        return self._attack

    def get_defense(self):
        return self._defense

    def get_dice(self):
        return self._dice

    def get_last_damages(self):
        return self._last_damages

#       SETTERS
    def set_name(self, new_name):
        self._name = new_name

    def set_hp_max(self, new_hp_max):
        self._hp_max = new_hp_max

    def set_hp(self, new_hp):
        self._hp = new_hp

    def set_attack(self, new_attack):
        self._attack = new_attack

    def set_defense(self, new_defense):
        self._defense = new_defense

    def set_dice(self, new_dice):
        self._dice = new_dice

    def set_dmg(self, new_dmg):
        self._last_damages = new_dmg

#       METHODS
    def is_alive(self):
        return (self._hp > 0)

    def show_health(self):
        if(self._hp < 0):
            self.set_hp(0)
        print(f"[{'#' * self._hp}{' ' * (self._hp_max - self._hp)}]  {self._hp}/{self._hp_max}")

    def bonus_attack(self, dmg, character):
        return dmg

    def bonus_defense(self, dmg, attacker):
        return dmg

    def bonus_heal(self):
        return 0

    def attack(self, character, roll):
        if(self.is_alive() == True and character.is_alive() == True):
            if roll is None:
                roll = 0
            dmg = self._attack + roll
            dmg = self.bonus_attack(dmg, character)
            print(f"{self.get_name()} is attacking {character.get_name()} for {dmg} HP (Base attack : {self._attack} + Roll : {roll})")
            character.defense(dmg, self)

    def defense(self, dmg, attacker):
        roll = self.defense_roll()
        if roll is None:
            roll = 0
        wound = dmg - self._defense - roll
        wound = self.bonus_defense(wound, attacker)
        if(wound < 0):
            wound = 0
        attacker.set_dmg(wound)
        print(f"{self.get_name()} is wounded by {attacker.get_name()} for {wound} HP ((Damages received : {dmg}) - (Defense : {self._defense}) - (Roll : {roll}))")
        self._hp -= wound
        self.show_health()

    # Move the sprite based on user keypresses
    def update(self, pressed_keys, target):

        if pressed_keys[K_RIGHT]:
            self.index = 0
            self.attacking = True
            self.atk_roll = True
            target.def_roll = True
            self.idle = False

        if(self.idle == True):
            self.index += 1
            if self.index >= len(self.images_idle):
                self.index = 0
            self.image = self.images_idle[self.index]

        if self.attacking == True:
            self.attack_sequence(target)
            


    def attack_sequence(self, target): 
        if(self.is_alive() == True and target.is_alive() == True):
            self.attack_animation()
            
            if self.attacked == True:
                roll = self.attack_roll()
                self.attack(target, roll)
                self.attacked = False




    def attack_animation(self):
        if self.attacking:
            self.interval += 1
        if self.interval == self.interval_max:
            self.interval = 0
            self.index += 1
            if self.index >= len(self.images_attack):
                
                self.index = 0
                self.attacking = False
                self.attacked = True
                self.idle = True

            self.image = self.images_attack[self.index] 

    def attack_roll(self):
        if self.atk_roll == True:
            roll = self.get_dice().update()
            self.atk_roll = False    
            return roll

    def defense_roll(self):
        if self.def_roll == True:
            roll = self.get_dice().update()
            self.def_roll = False
            return roll
           



class Warrior(Character):
    _type = "Warrior"
    
    def __init__(self, name, hp_max, attack, defense, dice, player_two):
        super(Warrior, self).__init__(name, hp_max, attack, defense, dice, player_two)

        #       IDLE ANIMATION LOADING
        self.images_idle.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\idle\img_0.png').convert())
        self.images_idle.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\idle\img_1.png').convert())
        self.images_idle.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\idle\img_2.png').convert())
        self.images_idle.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\idle\img_3.png').convert())
        self.images_idle.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\idle\img_4.png').convert())
        self.images_idle.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\idle\img_5.png').convert())
        self.images_idle.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\idle\img_6.png').convert())
        self.images_idle.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\idle\img_7.png').convert())
        self.images_idle.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\idle\img_8.png').convert())
        self.images_idle.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\idle\img_9.png').convert())

        #       ATTACK ANIMATION LOADING
        self.images_attack.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\Attack\img_0.png').convert())
        self.images_attack.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\Attack\img_1.png').convert())
        self.images_attack.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\Attack\img_2.png').convert())
        self.images_attack.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\Attack\img_3.png').convert())
        self.images_attack.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\Attack\img_4.png').convert())
        self.images_attack.append(pygame.image.load('Assets\Warrior\Colour1\SplitAnimation\Attack\img_5.png').convert())

        if(self._player_two == False):
            for i in range(0, len(self.images_idle)):
                self.images_idle[i] = pygame.transform.scale(self.images_idle[i], (225, 297))

            for i in range(0, len(self.images_attack)):
                self.images_attack[i] = pygame.transform.scale(self.images_attack[i], (225, 297))
        else:
            for i in range(0, len(self.images_idle)):
                self.images_idle[i] = pygame.transform.scale(self.images_idle[i], (225, 297))
                self.images_idle[i] = pygame.transform.flip(self.images_idle[i], True, False)

            for i in range(0, len(self.images_attack)):
                self.images_attack[i] = pygame.transform.scale(self.images_attack[i], (225, 297))
                self.images_attack[i] = pygame.transform.flip(self.images_attack[i], True, False)

        self.image = self.images_idle[self.index]
        self.rect = self.image.get_rect(center=((SCREEN_WIDTH * 0.15), (SCREEN_HEIGHT * 0.50) ))

        if(self._player_two == True):
            self.rect = self.image.get_rect(center=((SCREEN_WIDTH * 0.85), (SCREEN_HEIGHT * 0.50)))


        

    
    def bonus_attack(self, dmg, character):
        return dmg + 3


class Mage(Character):
    _type = "Mage"

    def bonus_defense(self, dmg, attacker):
        return dmg - 5

class Rogue(Character):
    _type = "Rogue"

    def bonus_attack(self, dmg, character):
        print(f"Rogue bonus : armor of {character.get_name()} was ignored. (amount ignored {character.get_defense()})")
        dmg += character.get_defense()
        return dmg

class Druid(Character):
    _type = "Druid"


    def defense(self, dmg, attacker):
        super().defense(dmg, attacker)
        roll = self._dice.roll()
        if(self.get_hp() + roll > self.get_hp_max()):           
            print(f"Druid bonus : healed of {self.get_hp_max() - self.get_hp()} HP OVERHEAL")
            self._hp += self.get_hp_max() - self.get_hp()
        else:
            print(f"Druid bonus : healed of {roll} HP")
            self._hp += roll
        self.show_health()

class Necro(Character):
    _type = "Necromancer"

    def defense(self, dmg, attacker):
        super().defense(dmg, attacker)
        roll = self._dice.roll()
        if(self.get_hp() + roll > self.get_hp_max()):           
            print(f"Druid bonus : healed of {self.get_hp_max() - self.get_hp()} HP OVERHEAL")
            self._hp += self.get_hp_max() - self.get_hp()
            print(f"Druid bonus : Dealt {self.get_hp_max() - self.get_hp()} to {attacker.get_name}")
            attacker.set_hp( (attacker.get_hp) - (self.get_hp_max() - self.get_hp()))
        else:
            print(f"Druid bonus : healed of {roll} HP")
            self._hp += roll
            print(f"Druid bonus : Dealt {roll} to {attacker.get_name}")
            attacker.set_hp(attacker.get_hp - roll)
        self.show_health()
        attacker.show_health()






if __name__ == "__main__":
    dd = Dice()
    char1 = Warrior("Zebi", 10, 3, 3, dd)
    char2 = Necro("Toufik", 10, 3, 3, dd)
    game = True


    char1.attack(char2)
    char2.attack(char1)


