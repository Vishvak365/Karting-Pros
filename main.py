# import pygame module in this program
import pygame
import screen
import track
import time
import mainmenu
from car import Car
from pygame.locals import *
import sys
import timetrial


def main():
    pygame.init()
    window = screen.Screen()
    display_surface = window.get_display()
    
    mainmenu.main_menu(display_surface)


if __name__ == '__main__':
    main()
    # timetrial
