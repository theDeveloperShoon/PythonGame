import sys
import pygame
import pygame.locals


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


class GameObject:
    def __init__(self, sprite, speed):
        self.speed = speed
        self.sprite = sprite


class Player:
    def __init__(self, pathToSprite):
        self.sprite = pygame.image.load(pathToSprite)
        self.speed = [0, 0]
        self.x_velocity = 0
        self.y_velocity = 0
        self.xLoc = 64
        self.yLoc = 64
        self.x_offset = 0
        self.y_offset = 0

    def set_offset(self, horizontal_offset, vertical_offset):
        self.x_offset = horizontal_offset
        self.y_offset = vertical_offset

    def update_location(self):
        self.xLoc += self.x_velocity
        self.yLoc += self.y_velocity

    def get_coordinate(self):
        return (self.xLoc + self.x_offset, self.yLoc + self.y_offset)


# Functions
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


def isStatsShowTrue(keys):
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
