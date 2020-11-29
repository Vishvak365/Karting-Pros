import pygame
import time
import math
import sys
from kartingpros import track, mainmenu, car, settings, loadimage
from kartingpros.loadimage import _load_image, _load_sound, _load_font
import numpy as np
from numpy import save
from kartingpros.car import Car
from pygame.locals import *
from pygame import mixer
import os


def completeLap(car, finish_line):
    if (car.hitbox[1] < (finish_line[1] + 100)) and (car.hitbox[1] > (finish_line[1] - 100)):
        if (car.hitbox[0] < (finish_line[0] + 15)) and (car.hitbox[0] > (finish_line[0] - 15)):
            return True


def checkOutOfBounds(car):
    x, y = 1920, 1080
    if (car.position[0] > x or car.position[0] < 0 or car.position[1] > y or car.position[1] < 0):
        return True
    else:
        return False


def checkpoint1(car, checkpoint, checkpoint_check):
    if (car.hitbox[1] < (checkpoint[1] + 110)) and (car.hitbox[1] > (checkpoint[1] - 110)):
        if (car.hitbox[0] < (checkpoint[0] + 15)) and (car.hitbox[0] > (checkpoint[0] - 15)):
            checkpoint_check = checkpoint_check + 1
    else:
        checkpoint_check = checkpoint_check

    return checkpoint_check


def timeTrial(display_surface):

    best_lap_time = 30000

    trackImg = _load_image('./images/track1-min.png')
    track1 = track.Track()
    white = (0, 128, 0)

    clock = pygame.time.Clock()
    t0 = time.time()

    # Car Setup
    start_position = (1010, 144)
    car = Car('./images/f1sprite.png', start_position)

    car_group = pygame.sprite.Group(car)

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
        pygame.display.flip()
        if data_collection:
            # Machine Learning Features
            # Direction (%360), Position.X, Position.Y
            feature = []
            # Label(right,left,up,down)(1 or 0 for all)
            label = []

        # Draw the Track
        # display_surface.fill(white)
        display_surface.blit(trackImg, (0, 0))
        # pad_group.draw(display_surface)

        font = _load_font('./fonts/American Captain.ttf', 32)

        if data_collection:
            feature.append(car.direction % 360)
            feature.append(int(car.position[0]))
            feature.append(int(car.position[1]))
            feature = np.array(feature)
            feature = feature / feature.max(axis=0)
            features.append(feature)

        track.checkpoint(display_surface)
        deltat = clock.tick(30)

        # Update Car and draw
        car_group.update(deltat)
        car_group.draw(display_surface)

        t1 = time.time()
        dt = t1-t0
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if not hasattr(event, 'key'):
                continue
            if event.key == K_RIGHT:
                right_press = 1
            elif event.key == K_SPACE:
                car.speed = 0
            elif event.key == K_LEFT:
                left_press = 1
            elif event.key == K_UP:
                up_press = 1
            elif event.key == K_DOWN:
                down_press = 1
            elif event.key == K_ESCAPE:
                if data_collection:
                    np.save('features.npy', np.array(features))
                    np.save('labels.npy', np.array(labels))
                mainmenu.main_menu(display_surface)
            if event.type == KEYUP:
                if event.key == pygame.K_RIGHT:
                    right_press = 0
                elif event.key == pygame.K_LEFT:
                    left_press = 0
                elif event.key == pygame.K_UP:
                    up_press = 0
                elif event.key == pygame.K_DOWN:
                    down_press = 0

        car.k_right = right_press * -5
        car.k_left = left_press * 5
        car.k_up = up_press * 2
        car.k_down = down_press * -2

        if up_press == 0 and down_press == 0 and int(car.speed) != 0:
            car.k_down = -.2
            car.k_up = 0

        if data_collection:
            labels.append([right_press, left_press, up_press, down_press])

        # Check if car is on track
        on_track = pygame.sprite.groupcollide(
            car_group, pad_group, False, False)

        # Slow down car if not on track
        if not on_track:
            car.setOffTrackSpeed()
        else:
            car.setRegularSpeed()

        if draw_hitbox:
            pygame.draw.rect(display_surface, (255, 0, 0), car.hitbox, 2)

        checkpoint_check = checkpoint1(car, checkpoint, checkpoint_check)

        # Countdown Timer Logic (program does not move forward until this is finished)
        while(time.time()-countdownTimerStart < 4):
            image = _load_image('./images/starting_lights/lights' +
                                str(int(time.time()-countdownTimerStart)+1)+'.png')
            display_surface.blit(image, ((1920/2)-(768/2), 50))
            fontBig = _load_font('./fonts/American Captain.ttf', 64)
            t0 = time.time()
            t1 = time.time()
            dt = t1-t0
            countdownFinished = True
            pygame.display.update()

        if(countdownFinished):
            # Timer
            timer_text = font.render(
                "Time: " + str(round(dt, 3)), True, (255, 255, 255))
            display_surface.blit(timer_text, (0, 0))

            # Time to Beat
            if best_lap_time != 30000:
                best_lap_text = font.render(
                    "Time to Beat: "+str(best_lap_time), True, (255, 255, 255))
                display_surface.blit(best_lap_text, (0, 30))

        if checkpoint_check >= 1:
            if completeLap(car, finish_line):
                if dt < best_lap_time:
                    best_lap_time = round(dt, 3)
                t0, t1 = time.time(), time.time()
                checkpoint_check = 0

        # If car is out of screen
        if checkOutOfBounds(car):
            car.reset(start_position)

        pygame.display.update()
