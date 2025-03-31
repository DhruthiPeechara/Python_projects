import pygame

pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500,500

display_surface = pygame.display.set_model((SCREEN_WIDTH , SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image ')

background_image = pygame.transform.scale(
    pygame.image.load('background.png').convert(),
    (SCREEN_WIDTH, SCREEN_HEIGHT)

    pengiun_image = pygame.transform.scale(
        
    )