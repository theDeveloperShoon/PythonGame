import pygame


class Entity:
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
