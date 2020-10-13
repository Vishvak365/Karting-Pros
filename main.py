import pygame
import time
import math
import sys
from pygame.locals import *


def timeTrial():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    # GAME CLOCK
    clock = pygame.time.Clock()
    t0 = time.time()

    class Car(pygame.sprite.Sprite):
        MAX_FORWARD_SPEED = 100
        MAX_REVERSE_SPEED = 50
        ACCELERATION = 10
        TURN_SPEED = 3

        def __init__(self, image, position):
            pygame.sprite.Sprite.__init__(self)
            self.src_image = pygame.image.load(image)
            self.position = position
            self.speed = self.direction = 0
            self.k_left = self.k_right = self.k_down = self.k_up = 0

        def update(self, deltat):
            # https://github.com/tdostilio/Race_Game
            # SIMULATION
            self.speed += (self.k_up + self.k_down)
            if self.speed > self.MAX_FORWARD_SPEED:
                self.speed = self.MAX_FORWARD_SPEED
            if self.speed < -self.MAX_REVERSE_SPEED:
                self.speed = -self.MAX_REVERSE_SPEED
            self.direction += (self.k_right + self.k_left)
            x, y = (self.position)
            rad = self.direction * math.pi / 180
            x += -self.speed*math.sin(rad)
            y += -self.speed*math.cos(rad)
            self.position = (x, y)
            self.src_image = pygame.transform.scale(self.src_image, (150, 200))
            self.image = pygame.transform.rotate(
                self.src_image, self.direction)
            self.rect = self.image.get_rect()
            self.rect.center = self.position

    car = Car('images/f1sprite.png', (10, 730))
    car_group = pygame.sprite.RenderPlain(car)
    while 1:
        # USER INPUT
        t1 = time.time()
        dt = t1-t0

        deltat = clock.tick(30)
        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue
            down = event.type == KEYDOWN
            if event.key == K_RIGHT:
                car.k_right = down * -5
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
        car_group.update(deltat)

        car_group.draw(screen)
        pygame.display.flip()


timeTrial()
