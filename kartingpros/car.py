import pygame
import time
import math
from kartingpros import settings
from kartingpros.loadimage import _load_image,_load_sound,_load_font
from pygame.locals import *


class Car(pygame.sprite.Sprite):
    MAX_FORWARD_SPEED = settings.getSetting('max_forward_speed')
    MAX_REVERSE_SPEED = settings.getSetting('max_reverse_speed')
    ACCELERATION = settings.getSetting('acceleration')
    TURN_SPEED = settings.getSetting('turn_speed')

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = _load_image(image)
        # self.src_image = pygame.transform.rotate(self.src_image, 90)
        self.position = position
        self.speed = 0
        self.direction = -90
        self.k_left = self.k_right = self.k_down = self.k_up = 0
        # self._x, self._y = 0, 0
        self.hitbox = (0, 0, 0, 0)

    def update(self, deltat):
        # https://github.com/tdostilio/Race_Game
        # SIMULATION
        self.speed += (self.k_up + self.k_down)
        if self.speed > self.MAX_FORWARD_SPEED:
            self.speed = self.MAX_FORWARD_SPEED
        if self.speed < -self.MAX_REVERSE_SPEED:
            self.speed = -self.MAX_REVERSE_SPEED
        self.direction += (self.k_right + self.k_left)
        x, y = self.position
        rad = self.direction * math.pi / 180
        x += -self.speed*math.sin(rad)
        y += -self.speed*math.cos(rad)
        self.position = (x, y)
        # print(self.position)
        xScale = 40
        yScale = math.ceil(xScale + (xScale*(1/3)))
        self.src_image = pygame.transform.scale(
            self.src_image, (xScale, yScale))
        self.image = pygame.transform.rotate(
            self.src_image, self.direction)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        self.x, self.y = x, y
        self.hitbox = (int(x) - 20, int(y) - 20, xScale-5, xScale-5)

    def setOffTrackSpeed(self):
        self.MAX_FORWARD_SPEED = settings.getSetting('off_track_speed')

    def setRegularSpeed(self):
        self.MAX_FORWARD_SPEED = settings.getSetting('max_forward_speed')
    
    def setDefaultValues(self):
        self.MAX_FORWARD_SPEED = 20
        self.MAX_REVERSE_SPEED = 3
        self.ACCELERATION = 1
        self.TURN_SPEED = 4

    def setRegularSpeedAI(self):
        self.MAX_FORWARD_SPEED = 20

    def setOffTrackSpeedAI(self):
        self.MAX_FORWARD_SPEED = 4

    def setRegularSpeedAIT2(self):
        self.MAX_FORWARD_SPEED = 10

    def setOffTrackSpeedAIT2(self):
        self.MAX_FORWARD_SPEED = 4

    def reset(self, position):
        self.position = position
        self.speed = 0
        self.direction = -90
        self.k_left = self.k_right = self.k_down = self.k_up = 0
        # self._x, self._y = 0, 0
        self.hitbox = (0, 0, 0, 0)
        # @property
        # def getX(self):
        #     return self._x

        # @property
        # def getY(self):
        #     return self._y
