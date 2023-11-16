import pygame, sys

from pygame.locals import *

pygame.init()

dis_window = pygame.display.set_mode((800,500))

pygame.display.set_caption('Hello Man')

while True:
    for each_event in pygame.event.get():
        if each_event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()