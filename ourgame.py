import sys
import math
import pygame
import pygame.locals
from Game.Entity import Entity


# Classes
class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen_width = 640
        self.screen_height = 640
        self.resolution = self.screen_width, self.screen_height
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Sean's Simple Stat Gain Game")
        pygame.display.set_icon(pygame.image.load("Assets/SSSGG_icon.png"))


class Player(Entity):
    def __init__(self, *args):
        super().__init__(*args)
        self.health = 64


def HorizontalMovementHandler(keys):
    returnModifier = 0

    if keys[pygame.K_a]:
        returnModifier -= 1
    if keys[pygame.K_d]:
        returnModifier += 1

    return returnModifier


def VerticalMovementHandler(keys):
    returnModifier = 0

    if keys[pygame.K_w]:
        returnModifier -= 1
    if keys[pygame.K_s]:
        returnModifier += 1

    return returnModifier


def isShowingStats(keys):
    if keys[pygame.K_e]:
        return True
    else:
        return False


# Initializing
game = GameEngine()

black = 0, 0, 0

testPlayer = Player("Assets/Sprites/TestBox.png")

showStats = False
# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()

        horizontalAxis = HorizontalMovementHandler(keys)
        verticalAxis = VerticalMovementHandler(keys)
        showStats = isStatsShowTrue(keys)

        testPlayer.x_velocity = horizontalAxis * 0.15
        testPlayer.y_velocity = verticalAxis * 0.15

    testPlayer.update_location()

    game.screen.fill(black)  # Fills the background with black

    # Adds the player onto screen
    game.screen.blit(testPlayer.sprite, testPlayer.get_coordinate())

    if(showStats):
        font = pygame.font.Font(None, 28)
        text = font.render(str(testPlayer.health), True, (255, 255, 255))
        game.screen.blit(text, text.get_rect())

    pygame.display.flip()  # Updates the full display Surface to the screen
