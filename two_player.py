# import pygame module in this program
import pygame
import screen
import track
import time
import mainmenu
from car import Car
from pygame.locals import *
import sys


def collision(car,car2,display_surface):
    if (car.hitbox[1] < (car2.hitbox[1] + 48)) and (car.hitbox[1] > (car2.hitbox[1] - 48)):
        if (car.hitbox[0] < (car2.hitbox[0] + 45)) and (car.hitbox[0] > (car2.hitbox[0] - 45)):
            car2.speed = 0
            car.speed = 0
            crash = pygame.image.load('images/crash.png')
            display_surface.blit(crash, (600, 250))
            pygame.display.update()
            pygame.time.delay(5000)
            print("collision")
            print(car.hitbox)
            mainmenu.main_menu(display_surface)


def carOneLap(car, finish_line):
    if (car.hitbox[1] < (finish_line[1] + 100)) and (car.hitbox[1] > (finish_line[1] - 100)):
        if (car.hitbox[0] < (finish_line[0] + 5)) and (car.hitbox[0] > (finish_line[0] - 5)):
            print("Lap finished for car 1!")


def carTwoLap(car, finish_line):
    if (car.hitbox[1] < (finish_line[1] + 100)) and (car.hitbox[1] > (finish_line[1] - 100)):
        if (car.hitbox[0] < (finish_line[0] + 5)) and (car.hitbox[0] > (finish_line[0] - 5)):
            print("Lap finished for car 2!")


def two_player(display_surface):
    # window = screen.Screen()
    track1 = track.Track()
    white = (0, 128, 0)

    clock = pygame.time.Clock()
    t0 = time.time()

    car = Car('images/f1sprite.png', (800, 80))
    car_group = pygame.sprite.Group(car)

    car2 = Car('images/f1sprite.png', (800, 170))
    car_group2 = pygame.sprite.Group(car2)

    pad_group = track1.getPads()
    finish_line = (960, 50, 20, 125)
    while True:
        # Draw the Track
        display_surface.fill(white)
        pad_group.draw(display_surface)
        track.checkpoint(display_surface)
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
                mainmenu.main_menu(display_surface)
                # sys.exit(0)  # quit the game

            if event.key == K_d:
                car2.k_right = down * -5
            elif event.key == K_LSHIFT:
                car2.speed = 0
            elif event.key == K_a:
                car2.k_left = down * 5
            elif event.key == K_w:
                car2.k_up = down * 2
            elif event.key == K_s:
                car2.k_down = down * -2
            elif event.key == K_ESCAPE:
                mainmenu.main_menu(display_surface)
                # sys.exit(0)  # quit the game

        # Update car and draw track
        car_group.update(deltat)
        car_group.draw(display_surface)
        pygame.draw.rect(display_surface, (255, 0, 0), car.hitbox, 2)
        car_group2.update(deltat)
        car_group2.draw(display_surface)
        pygame.draw.rect(display_surface, (255, 0, 0), car2.hitbox, 2)
        pygame.display.flip()
        collision(car,car2,display_surface)
        carOneLap(car, finish_line)
        carTwoLap(car2, finish_line)
        # pygame.draw.rect(display_surface, (255, 255, 255), (960, 0, 30, 125))
        pygame.display.update()