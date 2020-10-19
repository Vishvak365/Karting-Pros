import pygame
from pygame import *
import timetrial
import two_player
import sys

track = pygame.image.load('images/track.png')
background = pygame.image.load('images/Gui_background.png')
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


def text(text, color1, surface, x, y):
    title = pygame.font.SysFont(None, 36)
    textobj = title.render(text, 1, color1)
    textrec = textobj.get_rect()
    textrec.topleft = (x, y)
    surface.blit(textobj, textrec)


# -------- Main Program Loop -----------


def main_menu(screen):
    pygame.font.init()
    carryOn = True
    click = False
    while carryOn:
        # --- Main event loop

        mx, my = pygame.mouse.get_pos()
        button1col = RED
        button2col = RED
        button3col = RED
        button4col = RED
        button1 = pygame.Rect(50, 100, 200, 50)
        button2 = pygame.Rect(50, 200, 200, 50)
        button3 = pygame.Rect(50, 300, 200, 50)
        button4 = pygame.Rect(50, 400, 200, 50)

        if button1.collidepoint((mx, my)):
            button1col = YELLOW
            if click:
                if pick_track(screen):
                    break
        if button2.collidepoint((mx, my)):
            button2col = YELLOW
            if click:
                if pick_track_2player(screen):
                    break

        if button3.collidepoint((mx, my)):
            button3col = YELLOW
            if click:
                tutorial(screen)

        if button4.collidepoint((mx, my)):
            button4col = YELLOW
            if click:
                options(screen)

        screen.blit(background, (0, 0))
        text('Race Menu', YELLOW, screen, 310, 20)
        pygame.draw.rect(screen, button1col, button1)
        pygame.draw.rect(screen, button2col, button2)
        pygame.draw.rect(screen, button3col, button3)
        pygame.draw.rect(screen, button4col, button4)
        text('Time Trial', BLACK, screen, 80, 120)
        text('Two-Player', BLACK, screen, 80, 220)
        text('Tutorial', BLACK, screen, 80, 320)
        text('Options', BLACK, screen, 80, 420)
        click = False
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                sys.exit()
                # carryOn = False  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    carryOn = False
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
                two_player.two_player(screen)
                return True

        draw.rect(screen, track_select_col, trackCollide)
        screen.blit(track, (50, 80))
        pygame.display.update()
        clock.tick(60)
    return False


def options(screen):
    in_opts = True
    screen.blit(background, (0, 0))
    text('Options', YELLOW, screen, 20, 20)
    while in_opts:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_opts = False

        pygame.display.update()

        clock.tick(60)


def tutorial(screen):
    in_opts = True
    screen.blit(background, (0, 0))
    text('Tutorial', YELLOW, screen, 20, 20)
    image = pygame.image.load('images/tutorial.png')
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
