import pygame

width = height = 110
columns = rows = 6
margin = 25

screenx = (width * columns) + (margin * (columns + 1))
screeny = (height * rows) + margin * (rows + 1)

screen = pygame.display.set_mode((screenx, screeny))
