import pygame
from kartingpros import screen, mainmenu


def main():
    pygame.init()
    window = screen.Screen()
    display_surface = window.get_display()
    mainmenu.main_menu(display_surface)
