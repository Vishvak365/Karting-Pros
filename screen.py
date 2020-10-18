import pygame


class Screen:
    def __init__(self):
        self.width = 1920
        self.height = 1080
        self.display_surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Race-Karts')

    @property
    def get_width(self):
        return self.width

    @property
    def get_height(self):
        return self.height

    def get_display(self):
        return self.display_surface
