import pygame


class GameWindow():
    def __init__(self, width=640, height=640):
        self.window_width = width
        self.window_height = height
        self.resolution = self.window_width, self.window_height

    def create_window(self):
        screen = pygame.display.set_mode(self.resolution)
        return screen
