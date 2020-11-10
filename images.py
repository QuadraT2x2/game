import pygame
from screen_config import width, height, screenx, screeny

kitten = pygame.image.load("assets/kitten.jpg")
kitten = pygame.transform.scale(kitten, (width, height))

dog = pygame.image.load("assets/dog.jpg")
dog = pygame.transform.scale(dog, (width, height))

chiken = pygame.image.load("assets/chiken.jpg")
chiken = pygame.transform.scale(chiken, (width, height))

dragon = pygame.image.load("assets/dragon.jpg")
dragon = pygame.transform.scale(dragon, (width, height))

tiger = pygame.image.load("assets/tiger.jpg")
tiger = pygame.transform.scale(tiger, (width, height))

white_square = pygame.image.load("assets/square_white.png")
white_square = pygame.transform.scale(white_square, (width, height))

background = pygame.image.load("assets/bricks.jpg")
background = pygame.transform.scale(background, (screenx, screeny))

ayaya = pygame.image.load("assets/ayaya.jpg")
ayaya = pygame.transform.scale(ayaya, (width, height))

unknown = pygame.image.load("assets/unknown.jpg")
unknown = pygame.transform.scale(unknown, (width, height))
