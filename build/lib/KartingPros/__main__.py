import pygame
from KartingPros import screen, track, time, mainmenu, timetrial
# import track
# import time
# import mainmenu
from KartingPros import car
from car import Car
from pygame.locals import *
import sys
# import timetrial


def main():
    pygame.init()
    window = screen.Screen()
    display_surface = window.get_display()
    mainmenu.main_menu(display_surface)
