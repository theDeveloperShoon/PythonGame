import sys
import pygame


class GameEngine:
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 640
        self.resolution = self.screen_width, self.screen_height

    def inititalize(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("TemporaryGameName")


game = GameEngine()
game.inititalize()

speed = [1, 2]
black = 0, 0, 0

box = pygame.image.load("Assets/Sprites/TestBox.png")
boxrect = box.get_rect(center=(32, 32))

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.screen.fill(black)  # Fills the background with black
    game.screen.blit(box, boxrect)  # Adds the box onto screen
    pygame.display.flip()  # Updates the full display Surface to the screen
