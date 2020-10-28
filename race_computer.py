# import pygame module in this program
import pygame
import screen
import track
import time
import mainmenu
from car import Car
from pygame.locals import *
import sys

def win(display_surface):
    font = pygame.font.Font('fonts/American Captain.ttf', 32)
    win = pygame.image.load('images/win.png')
    carlap1 = font.render("Car 1 Wins!", True, (255, 255, 255))
    display_surface.blit(win, (700,300))
    display_surface.blit(carlap1, (1050, 500))
    pygame.display.update()
    pygame.time.delay(5000)
    mainmenu.main_menu(display_surface)


def win2(display_surface):
    font = pygame.font.Font('fonts/American Captain.ttf', 32)
    win = pygame.image.load('images/win.png')
    carlap2 = font.render("Car 2 Wins!", True, (255, 255, 255))
    display_surface.blit(win, (700, 300))
    display_surface.blit(carlap2, (1050, 500))
    pygame.display.update()
    pygame.time.delay(5000)
    mainmenu.main_menu(display_surface)


def checkpoint1(car, checkpoint, checkpoint_check):
    if (car.hitbox[1] < (checkpoint[1] + 110)) and (car.hitbox[1] > (checkpoint[1] - 110)):
        if (car.hitbox[0] < (checkpoint[0] + 15)) and (car.hitbox[0] > (checkpoint[0] - 15)):
            print("Lap finished")
            checkpoint_check = checkpoint_check + 1
    else:
        checkpoint_check = checkpoint_check

    return checkpoint_check


def checkOutOfBounds(car):
    x, y = 1920, 1080
    if (car.position[0] > x or car.position[0] < 0 or car.position[1] > y or car.position[1] < 0):
        return True
    else:
        return False


def collision(car,car2,display_surface):
    if (car.hitbox[1] < (car2.hitbox[1] + 35)) and (car.hitbox[1] > (car2.hitbox[1] - 35)):
        if (car.hitbox[0] < (car2.hitbox[0] + 35)) and (car.hitbox[0] > (car2.hitbox[0] - 35)):
            car2.speed = 0
            car.speed = 0
            crash = pygame.image.load('images/crash.png')
            display_surface.blit(crash, (600, 250))
            pygame.display.update()
            pygame.time.delay(2500)
            mainmenu.main_menu(display_surface)


def carOneLap(car, finish_line, lap):
    if (car.hitbox[1] < (finish_line[1] + 100)) and (car.hitbox[1] > (finish_line[1] - 100)):
        if (car.hitbox[0] < (finish_line[0] + 15)) and (car.hitbox[0] > (finish_line[0] - 15)):
            print("Lap finished for car 1!")
            lap = lap + 1
            return lap
        else:
            return lap
    else:
        return lap


def carTwoLap(car, finish_line, lap):
    if (car.hitbox[1] < (finish_line[1] + 100)) and (car.hitbox[1] > (finish_line[1] - 100)):
        if (car.hitbox[0] < (finish_line[0] + 15)) and (car.hitbox[0] > (finish_line[0] - 15)):
            print("Lap finished for car 2!")
            lap = lap + 1
            return lap
        else:
            return lap
    else:
        return lap

def computer_race(display_surface):
    # window = screen.Screen()
    track1 = track.Track()
    white = (0, 128, 0)
    startcar = (1010, 144)
    startcar2 = (1010, 75)
    clock = pygame.time.Clock()
    t0 = time.time()

    car = Car('images/f1sprite.png', startcar)
    car_group = pygame.sprite.Group(car)

    car2 = Car('images/f1sprite.png', startcar2)
    car_group2 = pygame.sprite.Group(car2)

    pad_group = track1.getPads()
    finish_line = (960, 50, 20, 125)
    checkpoint = (960, 845, 10, 125)
    lapcar1 = 0
    checkpointcar1 = 0
    lapcar2 = 0
    checkpointcar2 = 0
    while True:
        # Draw the Track
        display_surface.fill(white)
        pad_group.draw(display_surface)
        track.checkpoint(display_surface)
        deltat = clock.tick(30)
        font = pygame.font.Font('fonts/American Captain.ttf', 32)
        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue
            getEvent1(car,event,display_surface)
            getEvent2(car2,event,display_surface)



        # Update car and draw track
        carlap1 = font.render("Car 1 Laps completed: " + str(lapcar1) + "/5", True, (255, 255, 255))
        carlap2 = font.render("Car 2 Laps completed: " + str(lapcar2) + "/5", True, (255, 255, 255))
        display_surface.blit(carlap1, (0, 0))
        display_surface.blit(carlap2, (0, 30))
        car_group.update(deltat)
        car_group.draw(display_surface)
        pygame.draw.rect(display_surface, (255, 0, 0), car.hitbox, 2)
        car_group2.update(deltat)
        car_group2.draw(display_surface)
        pygame.draw.rect(display_surface, (255, 0, 0), car2.hitbox, 2)
        # Check if car is on track
        on_track = pygame.sprite.groupcollide(
            car_group, pad_group, False, False)

        # Slow down car if not on track
        if not on_track:
            car.MAX_FORWARD_SPEED = 3
        else:
            car.MAX_FORWARD_SPEED = 20
        # Check if car is on track
        on_track2 = pygame.sprite.groupcollide(
            car_group2, pad_group, False, False)

        # Slow down car if not on track
        if not on_track2:
            car2.MAX_FORWARD_SPEED = 3
        else:
            car2.MAX_FORWARD_SPEED = 20

        pygame.display.flip()
        collision(car,car2,display_surface)
        if checkOutOfBounds(car):
            car.reset(startcar)
        if checkOutOfBounds(car2):
            car2.reset(startcar2)
        checkpointcar1 = checkpoint1(car, checkpoint, checkpointcar1)
        checkpointcar2 = checkpoint1(car2, checkpoint, checkpointcar2)
        if checkpointcar1 >= 1:
            previouslapcar1 = lapcar1
            lapcar1 = carOneLap(car, finish_line, lapcar1)
            if lapcar1 > previouslapcar1:
                if lapcar1 == 5:
                    win(display_surface)
                checkpointcar1 = 0
        if checkpointcar2 >= 5:
            previouslapcar2 = lapcar2
            lapcar2 = carTwoLap(car2, finish_line, lapcar2)
            if lapcar2 > previouslapcar2:
                if lapcar2 == 1:
                    win2(display_surface)
                checkpointcar2 = 0
        # pygame.draw.rect(display_surface, (255, 255, 255), (960, 0, 30, 125))
        pygame.display.update()


def getEvent1(car, event, display_surface):
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


def getEvent2(car2,event,display_surface):
    down = event.type == KEYDOWN
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