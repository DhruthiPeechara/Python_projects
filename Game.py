import pygame 
import random 

SCREEN_WIDTH, SCREEN_HEIGHT = 500,400
MOVEMENT_SPEED = 5 
FONT_SIZE = 72

pygame.init()

background_image = pygame.transform.scale(pygame.image.load("https://t3.ftcdn.net/jpg/00/88/98/18/360_F_88981880_YjJManMJ6hJmKr5CZteFJAkEzXIh8mxW.jpg"))

font = pygame.font.SysFont("Times New Roman",FONT_SIZE)

class Sprite (pygame)