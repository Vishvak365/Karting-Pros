import pygame
import screen
import mainmenu

def main():
    pygame.init()
    window = screen.Screen()
    display_surface = window.get_display()
    mainmenu.main_menu(display_surface)