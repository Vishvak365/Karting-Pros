# # import pygame module in this program
import pygame
import screen
import mainmenu


def main():
    print('asdf')
    pygame.init()
    window = screen.Screen()
    display_surface = window.get_display()
    mainmenu.main_menu(display_surface)


if __name__ == '__main__':
    main()
    # print('adsf')