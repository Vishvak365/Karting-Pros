import pygame
import time
import math
import sys
from KartingPros import track, mainmenu
from KartingPros import car
from pygame.locals import *
# from car import Car


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
    best_lap_time = 30000
    # display_surface = screen
    track1 = track.Track()
    white = (0, 128, 0)
    clock = pygame.time.Clock()
    t0 = time.time()
    start_position = (1010, 144)
    car = Car(r'../KartingPros/images/f1sprite.png', start_position)
    car_group = pygame.sprite.Group(car)
    checkpoint_check = 0
    pad_group = track1.getPads()
    finish_line = (960, 50, 20, 125)
    checkpoint = (960, 845, 10, 125)
    while True:
        # Draw the Track
        display_surface.fill(white)
        pad_group.draw(display_surface)
        track.checkpoint(display_surface)
        deltat = clock.tick(30)
        font = pygame.font.Font('fonts/American Captain.ttf', 32)
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
        t1 = time.time()
        dt = t1-t0
        # Timer
        timer_text = font.render("Time: " + str(dt), True, (255, 255, 255))
        display_surface.blit(timer_text, (0, 0))

        # Time to Beat
        if best_lap_time != 30000:
            best_lap_text = font.render(
                "Time to Beat: "+str(best_lap_time), True, (255, 255, 255))
            display_surface.blit(best_lap_text, (0, 30))
        # Update Car and draw
        car_group.update(deltat)
        car_group.draw(display_surface)

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

        pygame.display.update()
