# import pygame module in this program
import pygame
import screen
import track


# import Track
def main():
    pygame.init()
    window = screen.Screen()
    display_surface = window.get_display()
    white = (255, 255, 255)
    while True:

        display_surface.fill(white)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()

                # quit the program.
                quit()

            # Draws the surface object to the screen.
            pygame.display.update()


if __name__ == '__main__':
    main()
