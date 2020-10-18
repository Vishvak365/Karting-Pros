# import pygame module in this program
import pygame
import screen
import track


# import Track
def main():
    pygame.init()
    window = screen.Screen()
    display_surface = window.get_display()
    track1 = track.Track()
    white = (0, 128, 0)
    while True:
        pad_group = track1.getPads()
        display_surface.fill(white)
        pad_group.draw(display_surface)
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
