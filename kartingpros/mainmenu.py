import json
from pathlib import Path
import os
import pygame
from pygame import *
from kartingpros import timetrial, two_player, T1_AI as track1_AI, race_computer,loadimage
from kartingpros.loadimage import _load_image,_load_sound,_load_font
import sys
from kartingpros.car import Car

track = _load_image('./images/track.png')
background = _load_image('./images/Gui_background.png')
track = transform.scale(track, (100, 100))
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 211, 0)
# The loop will carry on until the user exit the game (e.g. clicks the close button).


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()


def text(print_string, color1, surface, x, y):
    title = pygame.font.SysFont(None, 36)
    textobj = title.render(print_string, 1, color1)
    textrec = textobj.get_rect()
    textrec.topleft = (x, y)
    surface.blit(textobj, textrec)


# -------- Main Program Loop -----------


def main_menu(screen):
    pygame.font.init()
    click = False

    offset = 0
    start_position = (1120, 400)
    car = Car('images/f1sprite.png', start_position)
    car.direction = 0
    car_group = pygame.sprite.Group(car)

    while True:
        # --- Main event loop
        deltat = clock.tick(30)
        mx, my = pygame.mouse.get_pos()
        button1col = YELLOW
        button2col = YELLOW
        button3col = YELLOW
        button4col = YELLOW
        button5col = YELLOW
        button1 = pygame.Rect(50, 100, 500, 50)
        button2 = pygame.Rect(50, 200, 500, 50)
        button3 = pygame.Rect(50, 300, 500, 50)
        button4 = pygame.Rect(50, 400, 500, 50)
        button5 = pygame.Rect(50, 500, 500, 50)

        if button1.collidepoint((mx, my)):
            button1col = RED
            if click:
                if pick_track(screen):
                    break
        if button2.collidepoint((mx, my)):
            button2col = RED
            if click:
                if pick_track_2player(screen):
                    break

        if button3.collidepoint((mx, my)):
            button3col = RED
            if click:
                if pick_track_AI(screen):
                    break

        if button4.collidepoint((mx, my)):
            button4col = RED
            if click:
                tutorial(screen)

        if button5.collidepoint((mx, my)):
            button5col = RED
            if click:
                options(screen)

        #screen.blit(background, (0, 0))
        screen.fill(BLACK)
        if offset == 99:
            offset = 0
        else:
            offset = offset + 1
        drawroad(screen, offset)
        car_group.update(deltat)
        car_group.draw(screen)

        text('KARTING PROS', YELLOW, screen, 310, 20)
        pygame.draw.rect(screen, button1col, button1)
        pygame.draw.rect(screen, button2col, button2)
        pygame.draw.rect(screen, button3col, button3)
        pygame.draw.rect(screen, button4col, button4)
        pygame.draw.rect(screen, button5col, button5)

        text('Time Trial', BLACK, screen, 80, 120)
        text('Two-Player', BLACK, screen, 80, 220)
        text('AI_Versus', BLACK, screen, 80, 320)
        text('Tutorial', BLACK, screen, 80, 420)
        text('Options', BLACK, screen, 80, 520)
        click = False
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)
    # once main loop exits


def pick_track(screen):
    click = False
    in_opts = True
    screen.blit(background, (0, 0))
    text('Pick Track', YELLOW, screen, 20, 20)
    while in_opts:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_opts = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        trackCollide = pygame.Rect(40, 70, 120, 120)
        track_select_col = BLACK
        if trackCollide.collidepoint((mx, my)):
            track_select_col = YELLOW
            if click:
                timetrial.timeTrial(screen)
                in_opts = False
                return True

        draw.rect(screen, track_select_col, trackCollide)
        screen.blit(track, (50, 80))
        pygame.display.update()
        clock.tick(60)
    return False


def pick_track_2player(screen):
    click = False
    in_opts = True
    screen.blit(background, (0, 0))
    text('Pick Track', YELLOW, screen, 20, 20)
    while in_opts:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_opts = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        trackCollide = pygame.Rect(40, 70, 120, 120)
        track_select_col = BLACK
        if trackCollide.collidepoint((mx, my)):
            track_select_col = YELLOW
            if click:
                two_player.RaceCars(screen)
                return True

        draw.rect(screen, track_select_col, trackCollide)
        screen.blit(track, (50, 80))
        pygame.display.update()
        clock.tick(60)
    return False


def pick_track_AI(screen):
    click = False
    in_opts = True
    screen.blit(background, (0, 0))
    text('Pick Track', YELLOW, screen, 20, 20)
    while in_opts:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_opts = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        trackCollide = pygame.Rect(40, 70, 120, 120)
        track_select_col = BLACK
        if trackCollide.collidepoint((mx, my)):
            track_select_col = YELLOW
            if click:
                track1_AI.T1_AI(screen)
                # two_player.RaceCars(screen)
                return True

        draw.rect(screen, track_select_col, trackCollide)
        screen.blit(track, (50, 80))
        pygame.display.update()
        clock.tick(60)
    return False


def options(screen):
    in_opts = True
    #screen.blit(BLACK, (0, 0))
    screen.fill(BLACK)
    text('Options', YELLOW, screen, 20, 20)
    set_file = open(Path("kartingpros/settings.json"), "r")
    set_json = json.load(set_file)
    set_file.close()
    print(set_json)

    max_speed = int(set_json["max_forward_speed"])
    text("Max Forward Speed: ", YELLOW, screen, 20, 100)
    max_speed_up = pygame.Rect(300, 75, 30, 20)
    max_speed_down = pygame.Rect(300, 125, 30, 20)

    while in_opts:
        click = False
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    set_json["max_forward_speed"] = max_speed
                    set_file = open(Path("kartingpros/settings.json"), "w")
                    json.dump(set_json, set_file)
                    set_file.close()
                    in_opts = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        mx, my = pygame.mouse.get_pos()

        speedupcol = YELLOW
        speeddowncol = YELLOW

        if max_speed_up.collidepoint((mx, my)):
            speedupcol = RED
            if click:
                if max_speed < 99:
                    pygame.draw.rect(screen, BLACK, (300, 75, 50, 50))
                    max_speed = max_speed + 1

        if max_speed_down.collidepoint((mx, my)):
            speeddowncol = RED
            if click:
                if max_speed > 1:
                    pygame.draw.rect(screen, BLACK, (300, 75, 50, 50))
                    max_speed = max_speed - 1

        pygame.draw.rect(screen, speedupcol, max_speed_up)
        pygame.draw.rect(screen, speeddowncol, max_speed_down)
        text("^", BLACK, screen, 307, 77)
        text("v", BLACK, screen, 307, 122)


        text(str(max_speed), YELLOW, screen, 300, 100)


        pygame.display.update()

        clock.tick(60)


def tutorial(screen):
    in_opts = True
    screen.blit(background, (0, 0))
    text('Tutorial', YELLOW, screen, 20, 20)
    image = _load_image('./images/tutorial.png')
    screen.blit(image, (0, 100))
    while in_opts:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_opts = False

        pygame.display.update()

        clock.tick(60)


def drawroad(screen, offset):
    left = 1000
    right = 1200
    middle = left + ((right - left) / 2)
    leftSide = pygame.Rect(left, 0, 10, screen.get_height())
    rightSide = pygame.Rect(right, 0, 10, screen.get_height())
    pygame.draw.rect(screen, YELLOW, leftSide)
    pygame.draw.rect(screen, YELLOW, rightSide)
    for i in range(-100, screen.get_height() + 100, 100):
        pygame.draw.rect(screen, YELLOW, (middle, i + offset, 10, 60))