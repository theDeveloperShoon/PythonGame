import sys
import pygame
import pygame.locals


class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen_width = 640
        self.screen_height = 640
        self.resolution = self.screen_width, self.screen_height
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("TemporaryGameName")


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
        self.xLoc = 32
        self.yLoc = 32

    def updateLocation(self):
        self.xLoc += self.x_velocity
        self.yLoc += self.y_velocity

    def get_coordinate(self):
        return (self.xLoc, self.yLoc)

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


game = GameEngine()

black = 0, 0, 0

testPlayer = Player("Assets/Sprites/TestBox.png")


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()

        horizontalAxis = HorizontalMovementHandler(keys)
        verticalAxis = VerticalMovementHandler(keys)

        testPlayer.x_velocity = horizontalAxis * 0.15
        testPlayer.y_velocity = verticalAxis * 0.15

    testPlayer.updateLocation()

    game.screen.fill(black)  # Fills the background with black

    # Adds the box onto screen
    game.screen.blit(testPlayer.sprite, testPlayer.get_coordinate())

    pygame.display.flip()  # Updates the full display Surface to the screen
