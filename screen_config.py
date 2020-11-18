import pygame

width = height = 110
columns = rows = 6
margin = 25

screenx = (width * columns) + (margin * (columns + 1))
status_bar = 360
screenx_new = screenx + status_bar
screeny = (height * rows) + margin * (rows + 1)

screen = pygame.display.set_mode((screenx_new, screeny))
