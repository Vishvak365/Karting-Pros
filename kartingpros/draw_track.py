import pygame
import time
import math
import sys
from kartingpros import track2, mainmenu, car, settings, loadimage
from kartingpros.loadimage import _load_image, _load_sound, _load_font
import numpy as np
from numpy import save
from kartingpros.car import Car
from pygame.locals import *
from pygame import mixer
import os



def timeTrial(display_surface):

    best_lap_time = 30000

    track1 = track2.Track2()
    white = (0, 128, 0)

    clock = pygame.time.Clock()
    t0 = time.time()


    # Lap logic
    checkpoint_check = 0
    pad_group = track1.getPads()
    finish_line = (960, 50, 20, 125)
    checkpoint = (960, 845, 10, 125)

    # Countdown timer logic
    countdownTimerStart = time.time()
    countdownFinished = False

    # Music for countdown sound
    current_path = os.path.abspath(os.path.dirname(__file__))
    absolute_path = os.path.join(
        current_path, './sounds/race_coundown.mp3')
    print(absolute_path)
    mixer.init()
    mixer.music.load(absolute_path)
    mixer.music.set_volume(0.7)
    mixer.music.play()

    data_collection = settings.getSetting('collect_data_for_AI')
    draw_hitbox = settings.getSetting('draw_hitbox')
    i = 0
    if data_collection:
        # Data collection for machine learning
        features = []
        labels = []
    right_press, left_press, up_press, down_press = 0, 0, 0, 0
    while True:

        # Draw the Track
        display_surface.fill(white)
        pad_group.draw(display_surface)

        pygame.display.flip()


