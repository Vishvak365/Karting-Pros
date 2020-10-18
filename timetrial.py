import pygame
import time
import math
import sys
from car import Car
from pygame.locals import *


def timeTrial():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    # GAME CLOCK
    clock = pygame.time.Clock()
    t0 = time.time()

    car = Car('images/f1sprite.png', (719, 144))
    car_group = pygame.sprite.Group(car)

    track = pygame.image.load('images/track.png')

    # car_surf = pygame.Surface((car._x, car._y))
    while 1:
        # USER INPUT
        t1 = time.time()
        dt = t1-t0
        print(dt)
        deltat = clock.tick(30)
        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue
            down = event.type == KEYDOWN
            if event.key == K_RIGHT:
                car.k_right = down * -5
            elif event.key == K_SPACE:
                car.speed = 0
                print('asdf')
            elif event.key == K_LEFT:
                car.k_left = down * 5
            elif event.key == K_UP:
                car.k_up = down * 2
            elif event.key == K_DOWN:
                car.k_down = down * -2
            elif event.key == K_ESCAPE:
                sys.exit(0)  # quit the game
        # RENDERING
        screen.fill((255, 255, 255))
        screen.blit(track, (0, 0))
        # screen.blit(track, [0, 0])
        print(car.position)
        car_group.update(deltat)
        car_group.draw(screen)
        pygame.display.flip()


# timeTrial()
