# import pygame module in this program
import pygame
import screen
import track
import time
from car import Car
from pygame.locals import *
import sys


def main():
    pygame.init()
    window = screen.Screen()
    display_surface = window.get_display()
    track1 = track.Track()
    white = (0, 128, 0)

    clock = pygame.time.Clock()
    t0 = time.time()

    car = Car('images/f1sprite.png', (719, 144))
    car_group = pygame.sprite.Group(car)

    pad_group = track1.getPads()

    while True:
        # Draw the Track
        display_surface.fill(white)
        pad_group.draw(display_surface)

        deltat = clock.tick(30)
        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue
            down = event.type == KEYDOWN
            if event.key == K_RIGHT:
                car.k_right = down * -5
            elif event.key == K_SPACE:
                car.speed = 0
            elif event.key == K_LEFT:
                car.k_left = down * 5
            elif event.key == K_UP:
                car.k_up = down * 2
            elif event.key == K_DOWN:
                car.k_down = down * -2
            elif event.key == K_ESCAPE:
                sys.exit(0)  # quit the game

        # Update car and draw track
        car_group.update(deltat)
        car_group.draw(display_surface)
        pygame.display.flip()
        pygame.display.update()

if __name__ == '__main__':
    main()
