import pygame
import time
import math
import sys
import track
import mainmenu
import numpy as np
from numpy import save
from car import Car
from pygame.locals import *
from pygame import mixer
import pickle


def completeLap(car, finish_line):
    if (car.hitbox[1] < (finish_line[1] + 100)) and (car.hitbox[1] > (finish_line[1] - 100)):
        if (car.hitbox[0] < (finish_line[0] + 15)) and (car.hitbox[0] > (finish_line[0] - 15)):
            print("Lap finished")
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
            print("Lap finished")
            checkpoint_check = checkpoint_check + 1
    else:
        checkpoint_check = checkpoint_check

    return checkpoint_check


def timeTrial(display_surface):
    mixer.init()
    mixer.music.load('sounds/race_coundown.mp3')
    mixer.music.set_volume(0.7)

    best_lap_time = 30000
    # display_surface = screen
    track1 = track.Track()
    white = (0, 128, 0)
    clock = pygame.time.Clock()
    t0 = time.time()
    countdownTimerStart = time.time()
    countdownFinished = False
    start_position = (1010, 144)
    car = Car('images/f1sprite.png', start_position)
    car_group = pygame.sprite.Group(car)
    checkpoint_check = 0
    pad_group = track1.getPads()
    finish_line = (960, 50, 20, 125)
    checkpoint = (960, 845, 10, 125)

    mixer.music.play()

    # # Data collection for machine learning
    # features = []
    # labels = []
    # Import AI model
    model_filename = "knn_model.pkl"
    with open(model_filename, 'rb') as file:
        model = pickle.load(file)
    moves = np.load('labels.npy')
    right_press, left_press, up_press, down_press = 0, 0, 0, 0
    moveNum = 0
    while True:
        # Machine Learning Features
        # Direction (%360), Position.X, Position.Y
        feature = []
        # Label(right,left,up,down)(1 or 0 for all)
        # label = []

        # Draw the Track
        display_surface.fill(white)
        pad_group.draw(display_surface)
        font = pygame.font.Font('fonts/American Captain.ttf', 32)

        feature.append(car.direction % 360)
        feature.append(int(car.position[0]))
        feature.append(int(car.position[1]))
        feature = np.array(feature)
        feature = feature / feature.max(axis=0)
        # features.append(feature)

        # predicted_move = model.predict([feature])
        predicted_move = moves[moveNum]
        moveNum+=1
        print(predicted_move)
        track.checkpoint(display_surface)
        deltat = clock.tick(30)

        # Update Car and draw
        car_group.update(deltat)
        car_group.draw(display_surface)

        t1 = time.time()
        dt = t1-t0

        # car.k_right = predicted_move[0][0] * -5
        # car.k_left = predicted_move[0][1] * 5
        # car.k_up = predicted_move[0][2] * 2
        # car.k_down = predicted_move[0][3] * -2
        car.k_right = predicted_move[0] * -5
        car.k_left = 0 * 5
        car.k_up = 1 * 2
        car.k_down = 0 * -2

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            if not hasattr(event, 'key'):
                continue
            down = event.type == KEYDOWN
            if event.key == K_RIGHT:
                right_press = 1
                car.k_right = down * -5
            elif event.key == K_SPACE:
                car.speed = 0
            elif event.key == K_LEFT:
                left_press = 1
                car.k_left = down * 5
            elif event.key == K_UP:
                up_press = 1
                car.k_up = down * 2
            elif event.key == K_DOWN:
                down_press = 1
                car.k_down = down * -2
            if event.key == K_ESCAPE:
                mainmenu.main_menu(display_surface)

        if(countdownFinished):
            # Timer
            timer_text = font.render("Time: " + str(dt), True, (255, 255, 255))
            display_surface.blit(timer_text, (0, 0))

            # Time to Beat
            if best_lap_time != 30000:
                best_lap_text = font.render(
                    "Time to Beat: "+str(best_lap_time), True, (255, 255, 255))
                display_surface.blit(best_lap_text, (0, 30))

        # Check if car is on track
        on_track = pygame.sprite.groupcollide(
            car_group, pad_group, False, False)

        # Slow down car if not on track
        if not on_track:
            car.MAX_FORWARD_SPEED = 3
        else:
            car.MAX_FORWARD_SPEED = 20

        # OPTIONAL car hitbox
        pygame.draw.rect(display_surface, (255, 0, 0), car.hitbox, 2)

        pygame.display.flip()

        checkpoint_check = checkpoint1(car, checkpoint, checkpoint_check)

        if checkpoint_check >= 1:
            if completeLap(car, finish_line):
                if dt < best_lap_time:
                    # print("Best Lap Time: "+str(dt))
                    # win_font = font.render(
                    #     "Best Lap Time! " + str(dt), True, (255, 255, 255))
                    # display_surface.blit(win_font, (1920/2, 50))
                    best_lap_time = dt
                else:
                    pass
                    # win_font = font.render(
                    #     "Time to Beat: " + str(best_lap_time) + "\n Your lap time:" + str(dt), True, (255, 255, 255))
                    # display_surface.blit(win_font, (1920/2, 50))
                # time.sleep(3000)
                t0, t1 = time.time(), time.time()
                checkpoint_check = 0
        if checkOutOfBounds(car):
            car.reset(start_position)
        while(time.time()-countdownTimerStart < 4):
            fontBig = pygame.font.Font('fonts/American Captain.ttf', 64)
            countdown_text = font.render(
                "Time: " + str(4-t0), True, (255, 255, 255))
            display_surface.blit(countdown_text, (0, 0))
            t0 = time.time()
            t1 = time.time()
            dt = t1-t0
            countdownFinished = True
            # pygame.display.update()
        pygame.display.update()
