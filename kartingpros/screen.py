import pygame
from kartingpros import settings
# Common screen class for game -- height and width set, create display


class Screen:
    def __init__(self):
        self.width = settings.getSetting('screen_size')[0]
        self.height = settings.getSetting('screen_size')[1]
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
