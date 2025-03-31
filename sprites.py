import pygame 
import random 

pygame.init()

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1 
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT  + 2 

BLUE = pygame.Color('blue')
LIGHTBLUE = pygame.Color ('light blue ')
DARKBLUE = pygame.Color('dark blue')

#SPRITE COLORS 

YELLOW = pygame.Color ('yellow ')
MAGENTA = pygame.Color('magenta')
ORANGE = pygame.Color('orange')
WHITE = pygame.Color('white')

class Sprite (pygame.sprite.Sprite):
    