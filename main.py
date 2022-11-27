# Import and initialize the pygame library
import pygame
import time
from character import *
from dice import *
from background import *

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize pygame
pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

# define the RGB value for white,
#  green, blue colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (255, 0, 0)
black = (255, 255, 255)

# Set up the drawing window
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# TESTING
dd1 = Dice((SCREEN_WIDTH * 0.35), (SCREEN_HEIGHT * 0.55))
dd2 = Dice((SCREEN_WIDTH * 0.65), (SCREEN_HEIGHT * 0.55))
char1 = Warrior("zebi", 20, 5, 3, dd1, False)
char2 = Warrior("zebi", 150, 5, 3, dd2, True)

# DISPLAY HEALTHPOINTS
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf', 16)
hp_p1 = font.render(str(char1.get_hp()), True, green, blue)
hp_p2 = font.render(str(char2.get_hp()), True, green, blue)
dmg_1 = font.render("-"+str(char1.get_last_damages()), True, red, black)

textRect1 = hp_p1.get_rect()
textRect1.center = ((SCREEN_WIDTH * 0.15), (SCREEN_HEIGHT * 0.40) )
textRect2 = hp_p2.get_rect()
textRect2.center = (((SCREEN_WIDTH * 0.85), (SCREEN_HEIGHT * 0.40) ))
textRect3 = dmg_1.get_rect()
textRect3.center = ((SCREEN_WIDTH * 0.85), (SCREEN_HEIGHT * 0.50) )
# CREATE GROUPS TO HOLD SPRITES
all_sprites = pygame.sprite.Group()
all_sprites.add(char1)
all_sprites.add(char2)
all_sprites.add(dd1)
all_sprites.add(dd2)

# SETUP CLOCK FOR FRAMERATE
clock = pygame.time.Clock()

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            # Close the windows if escape key pressed
            if event.key == K_ESCAPE:
                running = False
        # Close the windows if window close button has been pressed
        elif event.type == pygame.QUIT:
            running = False

   

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    char1.update(pressed_keys, char2)
    #char2.update(pressed_keys, char1)

    # Fill the background with sky blue
    screen.fill(white)    

    hp_p1 = font.render(str(char1.get_hp()), True, green, blue)
    hp_p2 = font.render(str(char2.get_hp()), True, green, blue)
    dmg_p1 = font.render("-"+str(char1.get_last_damages()), True, red, black)
    screen.blit(hp_p1, textRect1)
    screen.blit(hp_p2, textRect2)
    if char1.get_last_damages() != 0:
        screen.blit(dmg_p1, textRect3)

    # DRAW ALL SPRITES
    all_sprites.draw(screen)
    pygame.display.update()

    # Flip the display
    #pygame.display.flip()

    # ENSURE PROGRAMS MAINTAINS A RATE OF 15 FRAMES PER SECOND
    clock.tick(20)

# Done! Time to quit.
pygame.quit()