import json
import pygame
from pygame.locals import *
JSON_FILE_NAME = "settings.json"


def getMaxForwardSpeed():
    f = open(JSON_FILE_NAME)
    data = json.load(f)
    print(data["max_forward_speed"])
    f.close()


def getSetting(settingName):
    f = open(JSON_FILE_NAME)
    data = json.load(f)
    f.close()
    return(data[settingName])


def displaySettings(display_surface):
    white = (0, 128, 0)
    while True:
        # Draw the Track
        display_surface.fill(white)
        font = pygame.font.Font('fonts/American Captain.ttf', 32)
    # getMaxForwardSpeed()
