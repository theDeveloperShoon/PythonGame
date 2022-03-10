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


class Player:
    def __init__(self, pathToSprite):
        self.sprite = pygame.image.load(pathToSprite)
        self.spriterect = self.sprite.get_rect()
        self.speed = [0, 0]


game = GameEngine()
game.inititalize()

black = 0, 0, 0

testPlayer = Player("Assets/Sprites/TestBox.png")

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    game.screen.fill(black)  # Fills the background with black

    # Adds the box onto screen
    game.screen.blit(testPlayer.sprite, testPlayer.spriterect)

    pygame.display.flip()  # Updates the full display Surface to the screen
