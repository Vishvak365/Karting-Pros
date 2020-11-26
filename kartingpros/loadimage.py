import os
import pygame
from pygame.locals import *
from pygame import mixer


def _load_image(relative_image_path, colorkey=False):
    """ Utility method to load the images. It handles if the images contain
    transparency, and relative paths.
    """
    current_path = os.path.abspath(os.path.dirname(__file__))
    absolute_image_path = os.path.join(current_path, relative_image_path)

    image = pygame.image.load(absolute_image_path)
    return image


def _load_font(relative_font_path, size):
    current_path = os.path.abspath(os.path.dirname(__file__))
    absolute_font_path = os.path.join(current_path, relative_font_path)
    return pygame.font.Font(absolute_font_path, size)


def _load_sound(relative_sound_path):
    current_path = os.path.abspath(os.path.dirname(__file__))
    absolute_image_path = os.path.join(current_path, relative_image_path)
    return pygame.font.Font(absolute_image_path, size)
