# import pygame module in this program
import pygame
import screen
import track
import time
from car import Car
from pygame.locals import *
import sys


def two_player():
    window = screen.Screen()
    display_surface = window.get_display()
    track1 = track.Track()
    white = (0, 128, 0)

    clock = pygame.time.Clock()
    t0 = time.time()

    car = Car('images/f1sprite.png', (719, 144))
    car_group = pygame.sprite.Group(car)

    car2 = Car('images/f1sprite.png', (800, 144))
    car_group2 = pygame.sprite.Group(car2)

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

            if event.key == K_d:
                car2.k_right = down * -5
            elif event.key == K_SPACE:
                car2.speed = 0
            elif event.key == K_a:
                car2.k_left = down * 5
            elif event.key == K_w:
                car2.k_up = down * 2
            elif event.key == K_s:
                car2.k_down = down * -2
            elif event.key == K_ESCAPE:
                sys.exit(0)  # quit the game

        # Update car and draw track
        car_group.update(deltat)
        car_group.draw(display_surface)
        pygame.draw.rect(display_surface, (255, 0, 0), car.hitbox, 2)
        car_group2.update(deltat)
        car_group2.draw(display_surface)
        pygame.draw.rect(display_surface, (255, 0, 0), car2.hitbox, 2)
        if (car.hitbox[1] < (car2.hitbox[1] + 48)) and (car.hitbox[1] > (car2.hitbox[1] - 48)):
            if(car.hitbox[0] < (car2.hitbox[0] + 45)) and (car.hitbox[0] > (car2.hitbox[0] - 45)):
                print("collision")
                print(car.hitbox)
        pygame.display.flip()
        pygame.draw.rect(display_surface, (255, 255, 255), (960, 0, 30, 125))
        pygame.display.update()


def main():
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
        pygame.draw.rect(display_surface, (255, 0, 0), car.hitbox, 2)
        pygame.display.update()


if __name__ == '__main__':
   two_player()
