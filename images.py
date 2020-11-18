import pygame
from screen_config import width, height, screenx, screeny

kitten = pygame.image.load("assets/kitten.jpg")
kitten = pygame.transform.scale(kitten, (width, height))

pooch = pygame.image.load("assets/dog.jpg")
pooch = pygame.transform.scale(pooch, (width, height))

cock = pygame.image.load("assets/chiken.jpg")
cock = pygame.transform.scale(cock, (width, height))

viper = pygame.image.load("assets/dragon.jpg")
viper = pygame.transform.scale(viper, (width, height))

tigress = pygame.image.load("assets/tiger.jpg")
tigress = pygame.transform.scale(tigress, (width, height))

white_square = pygame.image.load("assets/square_white.png")
white_square = pygame.transform.scale(white_square, (width, height))

background = pygame.image.load("assets/bricks.jpg")
background = pygame.transform.scale(background, (screenx, screeny))

ayaya = pygame.image.load("assets/ayaya.jpg")
ayaya = pygame.transform.scale(ayaya, (width, height))

unknown = pygame.image.load("assets/unknown.jpg")
unknown = pygame.transform.scale(unknown, (width, height))

up = pygame.image.load("assets/up.jpg")

down = pygame.image.load("assets/down.jpg")

left = pygame.image.load("assets/left.jpg")

right = pygame.image.load("assets/right.jpg")

assassin = pygame.image.load("assets/assasin.jpg")

warrior = pygame.image.load("assets/warrior.jpg")

prophet = pygame.image.load("assets/prophet.jpg")
