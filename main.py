import pygame
import time
import math
import sys
from pygame.locals import *


def timeTrial():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    # GAME CLOCK
    clock = pygame.time.Clock()
    t0 = time.time()

    class Car(pygame.sprite.Sprite):
        MAX_FORWARD_SPEED = 4
        MAX_REVERSE_SPEED = 1
        ACCELERATION = 1
        TURN_SPEED = 4

        def __init__(self, image, position):
            pygame.sprite.Sprite.__init__(self)
            self.src_image = pygame.image.load(image)
            self.position = position
            self.speed = self.direction = 0
            self.k_left = self.k_right = self.k_down = self.k_up = 0
            self._x, self._y = 0, 0

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
            xScale = 40
            yScale = math.ceil(xScale + (xScale*(1/3)))
            self.src_image = pygame.transform.scale(
                self.src_image, (xScale, yScale))
            self.image = pygame.transform.rotate(
                self.src_image, self.direction)
            self.rect = self.image.get_rect()
            self.rect.center = self.position
            self.x, self.y = x, y

        @property
        def getX(self):
            return self._x

        @property
        def getY(self):
            return self._y

    car = Car('images/f1sprite.png', (719, 144))
    car_group = pygame.sprite.Group(car)

    track = pygame.image.load('images/track.png')

    # car_surf = pygame.Surface((car._x, car._y))
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


timeTrial()
