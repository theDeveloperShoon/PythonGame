import sys
import pygame
from tmap.tile import Tile
from tmap.tmap import TMap


pygame.init()
resolution = 600, 600
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption('TMap Creator')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
