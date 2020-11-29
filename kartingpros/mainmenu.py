import json
from pathlib import Path
import pygame
from pygame import *
from kartingpros import timetrial, timetrial2, two_player, two_player2, T1_AI as track1_AI, T2_AI as track2_AI, race_computer, loadimage
from kartingpros.loadimage import _load_image, _load_sound, _load_font
import sys
from kartingpros.car import Car
from pygame import mixer
import os

track = _load_image('./images/track1.png')
track1 = _load_image('./images/track2b.png')
background = _load_image('./images/Gui_background.png')
track = transform.scale(track, (100, 100))
track1 = transform.scale(track1, (100, 100))
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
    start_position = (1105, 400)
    car = Car('images/f1sprite.png', start_position)
    car.direction = 0
    car_group = pygame.sprite.Group(car)
    current_path = os.path.abspath(os.path.dirname(__file__))
    absolute_path = os.path.join(
        current_path, './sounds/menu.mp3')
    mixer.init()
    mixer.music.load(absolute_path)
    mixer.music.set_volume(0.7)
    mixer.music.play(-1)

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
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(60)
    # once main loop exits


def pick_track(screen):
    offset = 0
    start_position = (1105, 400)
    car = Car('images/f1sprite.png', start_position)
    car.direction = 0
    car_group = pygame.sprite.Group(car)
    click = False
    in_opts = True
    while in_opts:
        deltat = clock.tick(30)
        screen.fill(BLACK)
        if offset == 99:
            offset = 0
        else:
            offset = offset + 1
        drawroad(screen, offset)
        car_group.update(deltat)
        car_group.draw(screen)
        text('Pick Track', YELLOW, screen, 20, 20)
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

        trackCollide2 = pygame.Rect(190, 70, 120, 120)
        track_select_col2 = BLACK

        if trackCollide.collidepoint((mx, my)):
            track_select_col = YELLOW
            if click:
                mixer.music.stop()
                timetrial.timeTrial(screen)
                in_opts = False
                return True

        if trackCollide2.collidepoint((mx, my)):
            track_select_col2 = YELLOW
            if click:
                mixer.music.stop()
                timetrial2.timeTrial(screen)
                in_opts = False
                return True

        draw.rect(screen, track_select_col, trackCollide)
        screen.blit(track, (50, 80))
        draw.rect(screen, track_select_col2, trackCollide2)
        screen.blit(track1, (200, 80))
        pygame.display.update()
        clock.tick(60)
    return False


def pick_track_2player(screen):
    offset = 0
    start_position = (1105, 400)
    car = Car('images/f1sprite.png', start_position)
    car.direction = 0
    car_group = pygame.sprite.Group(car)
    click = False
    in_opts = True
    while in_opts:
        deltat = clock.tick(30)
        screen.fill(BLACK)
        if offset == 99:
            offset = 0
        else:
            offset = offset + 1
        drawroad(screen, offset)
        car_group.update(deltat)
        car_group.draw(screen)
        text('Pick Track', YELLOW, screen, 20, 20)
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

        trackCollide2 = pygame.Rect(190, 70, 120, 120)
        track_select_col2 = BLACK

        if trackCollide.collidepoint((mx, my)):
            track_select_col = YELLOW
            if click:
                mixer.music.stop()
                two_player.RaceCars(screen)
                in_opts = False
                return True

        if trackCollide2.collidepoint((mx, my)):
            track_select_col2 = YELLOW
            if click:
                mixer.music.stop()
                two_player2.RaceCars(screen)
                in_opts = False
                return True

        draw.rect(screen, track_select_col, trackCollide)
        screen.blit(track, (50, 80))
        draw.rect(screen, track_select_col2, trackCollide2)
        screen.blit(track1, (200, 80))
        pygame.display.update()
        clock.tick(60)
    return False


def pick_track_AI(screen):
    offset = 0
    start_position = (1105, 400)
    car = Car('images/f1sprite.png', start_position)
    car.direction = 0
    car_group = pygame.sprite.Group(car)
    click = False
    in_opts = True
    while in_opts:
        deltat = clock.tick(30)
        screen.fill(BLACK)
        if offset == 99:
            offset = 0
        else:
            offset = offset + 1
        drawroad(screen, offset)
        car_group.update(deltat)
        car_group.draw(screen)
        text('Pick Track', YELLOW, screen, 20, 20)
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

        trackCollide2 = pygame.Rect(190, 70, 120, 120)
        track_select_col2 = BLACK

        if trackCollide.collidepoint((mx, my)):
            track_select_col = YELLOW
            if click:
                mixer.music.stop()
                track1_AI.T1_AI(screen)
                in_opts = False
                return True

        if trackCollide2.collidepoint((mx, my)):
            track_select_col2 = YELLOW
            if click:
                mixer.music.stop()
                track2_AI.T2_AI(screen)
                in_opts = False
                return True

        draw.rect(screen, track_select_col, trackCollide)
        screen.blit(track, (50, 80))
        draw.rect(screen, track_select_col2, trackCollide2)
        screen.blit(track1, (200, 80))
        pygame.display.update()
        clock.tick(60)
    return False


def options(screen):
    offset = 0
    start_position = (1105, 400)
    car = Car('images/f1sprite.png', start_position)
    car.direction = 0
    car_group = pygame.sprite.Group(car)
    in_opts = True
    JSON_FILE_NAME = "./settings.json"
    current_path = os.path.abspath(os.path.dirname(__file__))
    absolute_settings_path = os.path.join(current_path, JSON_FILE_NAME)

    set_file = open(Path(absolute_settings_path), "r")
    set_json = json.load(set_file)
    set_file.close()
    # print(set_json)

    max_speed = int(set_json["max_forward_speed"])
    rev_speed = int(set_json["max_reverse_speed"])
    acc = int(set_json["acceleration"])
    turn_speed = int(set_json["turn_speed"])
    ot_speed = int(set_json["off_track_speed"])
    ot_speed = int(set_json["off_track_speed"])
    collision = bool(set_json["collision"])
    hitbox = bool(set_json["draw_hitbox"])
    aiDifficulty = bool(set_json["ai_difficulty_hard"])

    while in_opts:
        deltat = clock.tick(30)
        screen.fill(BLACK)
        if offset == 99:
            offset = 0
        else:
            offset = offset + 1
        drawroad(screen, offset)
        car_group.update(deltat)
        car_group.draw(screen)
        click = False
        # screen.blit(BLACK, (0, 0))
        text('Options', YELLOW, screen, 20, 20)

        text("Max Forward Speed: ", YELLOW, screen, 20, 100)
        max_speed_up = pygame.Rect(300, 75, 30, 20)
        max_speed_down = pygame.Rect(300, 125, 30, 20)


        text("Max Reverse Speed: ", YELLOW, screen, 20, 200)
        rev_speed_up = pygame.Rect(300, 175, 30, 20)
        rev_speed_down = pygame.Rect(300, 225, 30, 20)


        text("Acceleration Speed: ", YELLOW, screen, 20, 300)
        acc_up = pygame.Rect(300, 275, 30, 20)
        acc_down = pygame.Rect(300, 325, 30, 20)


        text("Turn Speed: ", YELLOW, screen, 20, 400)
        ts_up = pygame.Rect(300, 375, 30, 20)
        ts_down = pygame.Rect(300, 425, 30, 20)

        text("Off-Track Speed: ", YELLOW, screen, 20, 500)
        ot_up = pygame.Rect(300, 475, 30, 20)
        ot_down = pygame.Rect(300, 525, 30, 20)

        text("Collisions: ", YELLOW, screen, 20, 600)
        col_toggle = pygame.Rect(300, 585, 50, 50)

        text("Draw Hitboxes: ", YELLOW, screen, 20, 700)
        hb_toggle = pygame.Rect(300, 685, 50, 50)

        text("AI Difficulty Hard?: ", YELLOW, screen, 20, 800)
        ai_toggle = pygame.Rect(300, 785, 67, 50)

        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    set_json["max_forward_speed"] = max_speed
                    set_json["max_reverse_speed"] = rev_speed
                    set_json["acceleration"] = acc
                    set_json["turn_speed"] = turn_speed
                    set_json["off_track_speed"] = ot_speed
                    set_json["collision"] = collision
                    set_json["draw_hitbox"] = hitbox
                    set_json["ai_difficulty_hard"] = aiDifficulty
                    JSON_FILE_NAME = "./settings.json"
                    current_path = os.path.abspath(os.path.dirname(__file__))
                    absolute_settings_path = os.path.join(current_path, JSON_FILE_NAME)
                    set_file = open(absolute_settings_path, "w")
                    json.dump(set_json, set_file)
                    set_file.close()
                    in_opts = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        mx, my = pygame.mouse.get_pos()

        speedupcol = YELLOW
        speeddowncol = YELLOW
        revupcol = YELLOW
        revdowncol = YELLOW
        accupcol = YELLOW
        accdowncol = YELLOW
        tsupcol = YELLOW
        tsdowncol = YELLOW
        otupcol = YELLOW
        otdowncol = YELLOW

        if(collision):
            coll_col = RED
        else:
            coll_col = YELLOW

        if (hitbox):
            hb_col = RED
        else:
            hb_col = YELLOW

        if (aiDifficulty):
            ai_col = RED
        else:
            ai_col = YELLOW

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

        if rev_speed_up.collidepoint((mx, my)):
            revupcol = RED
            if click:
                if rev_speed < 99:
                    pygame.draw.rect(screen, BLACK, (300, 175, 50, 50))
                    rev_speed = rev_speed + 1

        if rev_speed_down.collidepoint((mx, my)):
            revdowncol = RED
            if click:
                if rev_speed > 1:
                    pygame.draw.rect(screen, BLACK, (300, 175, 50, 50))
                    rev_speed = rev_speed - 1

        if acc_up.collidepoint((mx, my)):
            accupcol = RED
            if click:
                if acc < 99:
                    pygame.draw.rect(screen, BLACK, (300, 275, 50, 50))
                    acc = acc + 1

        if acc_down.collidepoint((mx, my)):
            accdowncol = RED
            if click:
                if acc > 1:
                    pygame.draw.rect(screen, BLACK, (300, 275, 50, 50))
                    acc = acc - 1

        if ts_up.collidepoint((mx, my)):
            tsupcol = RED
            if click:
                if turn_speed < 99:
                    pygame.draw.rect(screen, BLACK, (300, 375, 50, 50))
                    turn_speed = turn_speed + 1

        if ts_down.collidepoint((mx, my)):
            tsdowncol = RED
            if click:
                if turn_speed > 1:
                    pygame.draw.rect(screen, BLACK, (300, 375, 50, 50))
                    turn_speed = turn_speed - 1

        if ot_up.collidepoint((mx, my)):
            otupcol = RED
            if click:
                if ot_speed < 99:
                    pygame.draw.rect(screen, BLACK, (300, 475, 50, 50))
                    ot_speed = ot_speed + 1

        if ot_down.collidepoint((mx, my)):
            otdowncol = RED
            if click:
                if ot_speed > 1:
                    pygame.draw.rect(screen, BLACK, (300, 475, 50, 50))
                    ot_speed = ot_speed - 1

        if col_toggle.collidepoint((mx, my)):
            if click:
                collision = not collision

        if hb_toggle.collidepoint((mx, my)):
            if click:
                hitbox = not hitbox

        if ai_toggle.collidepoint((mx, my)):
            if click:
                aiDifficulty = not aiDifficulty

        pygame.draw.rect(screen, speedupcol, max_speed_up)
        pygame.draw.rect(screen, speeddowncol, max_speed_down)
        text("^", BLACK, screen, 307, 77)
        text("v", BLACK, screen, 307, 122)

        pygame.draw.rect(screen, revupcol, rev_speed_up)
        pygame.draw.rect(screen, revdowncol, rev_speed_down)
        text("^", BLACK, screen, 307, 177)
        text("v", BLACK, screen, 307, 222)

        pygame.draw.rect(screen, accupcol, acc_up)
        pygame.draw.rect(screen, accdowncol, acc_down)
        text("^", BLACK, screen, 307, 277)
        text("v", BLACK, screen, 307, 322)

        pygame.draw.rect(screen, tsupcol, ts_up)
        pygame.draw.rect(screen, tsdowncol, ts_down)
        text("^", BLACK, screen, 307, 377)
        text("v", BLACK, screen, 307, 422)

        pygame.draw.rect(screen, otupcol, ot_up)
        pygame.draw.rect(screen, otdowncol, ot_down)
        text("^", BLACK, screen, 307, 477)
        text("v", BLACK, screen, 307, 522)

        pygame.draw.rect(screen, coll_col, col_toggle)

        pygame.draw.rect(screen, hb_col, hb_toggle)

        pygame.draw.rect(screen, ai_col, ai_toggle)

        text(str(max_speed), YELLOW, screen, 300, 100)
        text(str(rev_speed), YELLOW, screen, 300, 200)
        text(str(acc), YELLOW, screen, 300, 300)
        text(str(turn_speed), YELLOW, screen, 300, 400)
        text(str(ot_speed), YELLOW, screen, 300, 500)

        if(collision):
            text("ON", BLACK, screen, 300, 600)
        else:
            text("OFF", BLACK, screen, 300, 600)

        if (hitbox):
            text("ON", BLACK, screen, 300, 700)
        else:
            text("OFF", BLACK, screen, 300, 700)

        if (aiDifficulty):
            text("HARD", BLACK, screen, 300, 800)
        else:
            text("EASY", BLACK, screen, 300, 800)

        pygame.display.update()

        clock.tick(60)


def tutorial(screen):
    offset = 0
    start_position = (1105, 400)
    car = Car('images/f1sprite.png', start_position)
    car.direction = 0
    car_group = pygame.sprite.Group(car)
    in_opts = True
    while in_opts:
        deltat = clock.tick(30)
        screen.fill(BLACK)
        if offset == 99:
            offset = 0
        else:
            offset = offset + 1
        drawroad(screen, offset)
        car_group.update(deltat)
        car_group.draw(screen)
        text('Tutorial', YELLOW, screen, 20, 20)
        image = _load_image('./images/tutorial.png')
        screen.blit(image, (30, 100))
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
