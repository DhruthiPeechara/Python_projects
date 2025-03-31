import math 
import random 
import pygame 

SCREEN_WIDTH = 800 
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380 
ENEMY_START_Y_MIN = 50 
ENEMY_START_Y_MAX = 150 
ENEMY_SPEED_X = 4 
ENEMY_SPEED_Y = 40 
BULLET_SPEED_Y = 10 
COLLISION_DISTANCE = 27 

pygame.init[]
screen = pygame.display.set_model((SCREEN_WIDTH,SCREEN_HEIGHT))

background= pygame.image.load("https://t3.ftcdn.net/jpg/00/88/98/18/360_F_88981880_YjJManMJ6hJmKr5CZteFJAkEzXIh8mxW.jpg")

pygame.display.set_caption("Space Invader")
icon = pygame.image.load("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRQiyCZTqeZ-yttYdAfBiHA-FnnD1AsrLDxg&s")

pygame.display.set_icon(icon)

#Players 

playerImg = pygame.image.load("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8bBRwxa4Em853Nw89YjD3Q8fbP82UJzGhx6Zxx8NWTlp9mHwht3UvVc5kVJuanrNxULU&usqp=CAU")

playerX = PLAYER_START_X 
playerY = PLAYER_START_Y 
playerX_change = 0 

# Enemy 

enemyImg = []
enemyX = []
enemyY = []

enemyX_change = []
enemyY_change = []
num_of_enemies = 6 
for _i in range(num_of_enemies):
    enemyImg.append(pygame.image.load("https://cdn2.iconfinder.com/data/icons/icontober/64/Inkcontober_Misterious-512.png"))
    enemyX.append(random.randit(0, SCREEN_WIDTH-64)) 
    enemyY.append(ENEMY_SPEED_Y )

    #BULLET 

    bulletImg = pygame.image.load("https://freepngimg.com/thumb/categories/3007.png")
    bulletX = 0 
    bulletY = PLAYER_START_Y 
    bulletX_change = 0 
    bulletY_change = BULLET_SPEED_Y 
    bullet_state = "ready "

    # score 

    score_value = 0 
    font = pygame.font.Font("freesansbold.ttf",32)
    textX = 10 
    textY = 10 

    over_font = pygame.font.Font("freesansbold.ttf",64)
    def show_score(x,y): 

        score = font.render("Score:" + str(score_value),True(255,255,255))
        screen.blit(score,(x,y))

    def game_over_text(): 

        over_text = over_font.render("GAME OVER")