# This is a sample Python script.
import pygame, sys
from pygame import *
#pygame.init()
pygame.font.init()
#size = (700, 500)
#pygame.display.set_caption("My Game")
#screen = pygame.display.set_mode(size)
title = pygame.font.SysFont(None, 36)
track = pygame.image.load('images/track.png')
track = transform.scale(track, (100, 100))
# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
YELLOW = (255, 211, 0)
# The loop will carry on until the user exit the game (e.g. clicks the close button).


# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
def text(text, font, color, surface, x, y):
    textobj = title.render(text, 1, color)
    textrec = textobj.get_rect()
    textrec.topleft = (x, y)
    surface.blit(textobj, textrec)
# -------- Main Program Loop -----------
def main_menu(screen):
    carryOn = True
    while carryOn:
        # --- Main event loop

        mx, my = pygame.mouse.get_pos()
        button1col = RED
        button2col = RED
        button1 = pygame.Rect(50, 100, 200, 50)
        button2 = pygame.Rect(50, 200, 200, 50)

        if button1.collidepoint((mx, my)):
            button1col = YELLOW
            if click:
                if pick_track(screen):
                    break
        if button2.collidepoint((mx, my)):
            button2col = YELLOW
            if click:
                options(screen)
        screen.fill(BLACK)
        text('Race Menu', title, YELLOW, screen, 310, 20)
        pygame.draw.rect(screen, button1col, button1)
        pygame.draw.rect(screen, button2col, button2)
        text('Time Trial', font, BLACK, screen, 80, 120)
        text('Options', font, BLACK, screen, 80, 220)
        click = False
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                carryOn = False  # Flag that we are done so we exit this loop
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
    screen.fill(BLACK)
    text('Pick Track', title, YELLOW, screen, 20, 20)
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

        trackCollide = pygame.Rect(40, 70, 120, 120);
        track_select_col = BLACK
        if trackCollide.collidepoint((mx, my)):
            track_select_col = YELLOW
            if click:
                in_opts = False
                return True

        draw.rect(screen, track_select_col, trackCollide)
        screen.blit(track, (50, 80))
        pygame.display.update()
        clock.tick(60)
    return False

def options(screen):
    in_opts = True
    screen.fill(BLACK)
    text('Options', title, YELLOW, screen, 20, 20)
    while in_opts:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                pygame.quit()  # Flag that we are done so we exit this loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_opts = False

        pygame.display.update()

        clock.tick(60)
