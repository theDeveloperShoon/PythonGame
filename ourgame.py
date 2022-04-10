import sys
import math
import pygame
import pygame.locals
from Game.Entity import Entity
from Game.GameWindow import GameWindow


# Classes
class GameEngine:
    def __init__(self):
        pygame.init()
        self.gameWindow = GameWindow()
        self.resolution = self.gameWindow.resolution
        self.screen = self.gameWindow.create_window()
        pygame.display.set_caption("Sean's Simple Stat Gain Game")
        pygame.display.set_icon(pygame.image.load("Assets/SSSGG_icon.png"))


class GameManager:
    def __init__(self):
        self.debugShow = False


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


# Initializing
game = GameEngine()
gameManager = GameManager()

black = 0, 0, 0

testPlayer = Player("Assets/Sprites/TestBox.png")

clock = pygame.time.Clock()

# Game Loop
while True:
    # pygame.time.Clock().tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()

        horizontalAxis = HorizontalMovementHandler(keys)
        verticalAxis = VerticalMovementHandler(keys)

        testPlayer.x_velocity = horizontalAxis * 4
        testPlayer.y_velocity = verticalAxis * 4

    testPlayer.update_location()

    game.screen.fill(black)  # Fills the background with black

    # Adds the player onto screen
    game.screen.blit(testPlayer.sprite, testPlayer.get_coordinate())

    if(gameManager.debugShow):
        font = pygame.font.Font(None, 28)
        healthText = font.render(
            'Health - ' + str(testPlayer.health), True, (255, 255, 255))
        game.screen.blit(healthText, healthText.get_rect())
        fpsText = font.render(
            'FPS - ' + str(math.floor(clock.get_fps())), True, (255, 255, 255))
        game.screen.blit(fpsText, (0, 100))

    clock.tick(144)

    pygame.display.flip()  # Updates the full display Surface to the screen
