import pygame
import time
import math
import sys
import track
import mainmenu
from car import Car
from pygame.locals import *


def timeTrial(display_surface):
    # display_surface = screen
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

        deltat = clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
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
                mainmenu.main_menu(display_surface)
                # sys.exit(0)  # quit the game

        # Update car and draw track
        car_group.update(deltat)
        car_group.draw(display_surface)
        pygame.draw.rect(display_surface, (255, 0, 0), car.hitbox, 2)
        pygame.display.flip()
        pygame.display.update()

    # # pygame.init()
    # # screen = pygame.display.set_mode((1920, 1080))
    # # GAME CLOCK
    # clock = pygame.time.Clock()
    # t0 = time.time()

    # car = Car('images/f1sprite.png', (719, 144))
    # car_group = pygame.sprite.Group(car)

    # track = pygame.image.load('images/track.png')

    # # car_surf = pygame.Surface((car._x, car._y))
    # while 1:
    #     # USER INPUT
    #     t1 = time.time()
    #     dt = t1-t0
    #     print(dt)
    #     deltat = clock.tick(30)
    #     for event in pygame.event.get():
    #         if not hasattr(event, 'key'):
    #             continue
    #         down = event.type == KEYDOWN
    #         if event.key == K_RIGHT:
    #             car.k_right = down * -5
    #         elif event.key == K_SPACE:
    #             car.speed = 0
    #             print('asdf')
    #         elif event.key == K_LEFT:
    #             car.k_left = down * 5
    #         elif event.key == K_UP:
    #             car.k_up = down * 2
    #         elif event.key == K_DOWN:
    #             car.k_down = down * -2
    #         elif event.key == K_ESCAPE:
    #             sys.exit(0)  # quit the game
    #     # RENDERING
    #     screen.fill((255, 255, 255))
    #     screen.blit(track, (0, 0))
    #     # screen.blit(track, [0, 0])
    #     print(car.position)
    #     car_group.update(deltat)
    #     car_group.draw(screen)
    #     pygame.display.flip()


# timeTrial()
