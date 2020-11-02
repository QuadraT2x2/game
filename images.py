import pygame
from screen_config import width, height, screenx, screeny

kitten = pygame.image.load("kitten.jpg")
kitten = pygame.transform.scale(kitten, (width, height))

dog = pygame.image.load("dog.jpg")
dog = pygame.transform.scale(dog, (width, height))

chiken = pygame.image.load("chiken.jpg")
chiken = pygame.transform.scale(chiken, (width, height))

dragon = pygame.image.load("dragon.jpg")
dragon = pygame.transform.scale(dragon, (width, height))

tiger = pygame.image.load("tiger.jpg")
tiger = pygame.transform.scale(tiger, (width, height))

white_square = pygame.image.load("square_white.png")
white_square = pygame.transform.scale(white_square, (width, height))

background = pygame.image.load("bricks.jpg")
background = pygame.transform.scale(background, (screenx, screeny))

ayaya = pygame.image.load("ayaya.jpg")
ayaya = pygame.transform.scale(ayaya, (width, height))
