import sys
import pygame


class GameEngine:
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 640
        self.resolution = self.screen_width, self.screen_height

    def inititalize(self):
        pygame.init()
        pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("TemporaryGameName")


game = GameEngine()
game.inititalize()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
