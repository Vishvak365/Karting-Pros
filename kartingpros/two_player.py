# import pygame module in this program
import pygame
from kartingpros import screen, track, mainmenu, car, settings
import time
from kartingpros.car import Car
from pygame.locals import *
from pygame import mixer
import sys


def win(display_surface, msg):
    font = pygame.font.Font(r'kartingpros/fonts/American Captain.ttf', 32)
    win_image = pygame.image.load(r'kartingpros/images/win.png')
    car_lap = font.render(msg, True, (255, 255, 255))
    display_surface.blit(win_image, (700, 300))
    display_surface.blit(car_lap, (1050, 500))
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
    if car.position[0] > x or car.position[0] < 0 or car.position[1] > y or car.position[1] < 0:
        return True
    else:
        return False


def collision(car, car2, display_surface):
    if (car.hitbox[1] < (car2.hitbox[1] + 35)) and (car.hitbox[1] > (car2.hitbox[1] - 35)):
        if (car.hitbox[0] < (car2.hitbox[0] + 35)) and (car.hitbox[0] > (car2.hitbox[0] - 35)):
            car2.speed = 0
            car.speed = 0
            crash = pygame.image.load(r'kartingpros/images/crash.png')
            display_surface.blit(crash, (600, 250))
            pygame.display.update()
            pygame.time.delay(2500)
            mainmenu.main_menu(display_surface)


def carLap(car, finish_line, lap, msg):
    if (car.hitbox[1] < (finish_line[1] + 100)) and (car.hitbox[1] > (finish_line[1] - 100)):
        if (car.hitbox[0] < (finish_line[0] + 15)) and (car.hitbox[0] > (finish_line[0] - 15)):
            print(msg)
            lap = lap + 1
            return lap
        else:
            return lap
    else:
        return lap


def RaceCars(display_surface):
    track1 = track.Track()
    white = (0, 128, 0)

    # Official timer
    clock = pygame.time.Clock()
    t0 = time.time()

    # Setup car objects
    start_car1 = (1010, 144)
    car = Car(r'kartingpros/images/f1sprite.png', start_car1)
    car_group = pygame.sprite.Group(car)

    start_car2 = (1010, 75)
    car2 = Car(r'kartingpros/images/f1sprite.png', start_car2)
    car_group2 = pygame.sprite.Group(car2)

    # Groups for pads and finish line
    pad_group = track1.getPads()
    finish_line = track1.getFinishLine()

    # Setup lap logic
    checkpoint = (960, 845, 10, 125)
    lap_car1 = 0
    checkpoint_car1 = 0
    lap_car2 = 0
    checkpoint_car2 = 0

    # Collision Check
    collisions = settings.getSetting('collision')
    draw_hitbox = settings.getSetting('draw_hitbox')

    # Countdown timer logic
    countdownTimerStart = time.time()
    countdownFinished = False

    # Music for countdown sound
    mixer.init()
    mixer.music.load(r'kartingpros/sounds/race_coundown.mp3')
    mixer.music.set_volume(0.7)
    mixer.music.play()
    while True:
        # Draw the Track
        display_surface.fill(white)
        pad_group.draw(display_surface)
        track.checkpoint(display_surface)
        delta_t = clock.tick(30)
        font = pygame.font.Font(r'kartingpros/fonts/American Captain.ttf', 32)
        for event in pygame.event.get():
            if not hasattr(event, 'key'):
                continue
            getEvent1(car, event, display_surface)
            getEvent2(car2, event, display_surface)

        # Update car and draw track
        carlap1 = font.render("Car 1 Laps completed: " +
                              str(lap_car1) + "/5", True, (255, 255, 255))
        carlap2 = font.render("Car 2 Laps completed: " +
                              str(lap_car2) + "/5", True, (255, 255, 255))
        # Lap count for Cars
        display_surface.blit(carlap1, (0, 0))
        display_surface.blit(carlap2, (0, 30))

        # Update and draw car
        car_group.update(delta_t)
        car_group.draw(display_surface)

        # Update and draw car
        car_group2.update(delta_t)
        car_group2.draw(display_surface)

        if draw_hitbox:
            pygame.draw.rect(display_surface, (255, 0, 0), car.hitbox, 2)
            pygame.draw.rect(display_surface, (255, 0, 0), car2.hitbox, 2)

        # Check if car is on track
        SetCarMaxSpeed(car, pad_group, car_group)
        SetCarMaxSpeed(car2, pad_group, car_group2)

        pygame.display.flip()
        # Check for collisions only if enabled
        if collisions:
            collision(car, car2, display_surface)

        if checkOutOfBounds(car):
            car.reset(start_car1)
        if checkOutOfBounds(car2):
            car2.reset(start_car2)
        checkpoint_car1 = checkpoint1(car, checkpoint, checkpoint_car1)
        checkpoint_car2 = checkpoint1(car2, checkpoint, checkpoint_car2)
        if checkpoint_car1 >= 1:
            previouslapcar1 = lap_car1
            lap_car1 = carLap(car, finish_line, lap_car1,
                              "Lap finished for car 1!")
            if lap_car1 > previouslapcar1:
                if lap_car1 == 5:
                    win(display_surface, "Car 1 Wins!")
                checkpoint_car1 = 0
        if checkpoint_car2 >= 1:
            previouslapcar2 = lap_car2
            lap_car2 = carLap(car2, finish_line, lap_car2,
                              "Lap finished for car 2!")
            if lap_car2 > previouslapcar2:
                if lap_car2 == 5:
                    win(display_surface, "Car 2 Wins!")
                checkpoint_car2 = 0

        while(time.time()-countdownTimerStart < 4):
            # Ability to close out mid countdown
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)

            image = pygame.image.load(
                r'kartingpros/images/starting_lights/lights'+str(int(time.time()-countdownTimerStart)+1)+'.png')
            display_surface.blit(image, ((1920/2)-(768/2), 50))
            print(int(time.time()-countdownTimerStart))
            fontBig = pygame.font.Font(r'kartingpros/fonts/American Captain.ttf', 64)
            countdown_text = font.render(
                "Time: " + str(4-t0), True, (255, 255, 255))
            display_surface.blit(countdown_text, (0, 0))
            t0 = time.time()
            t1 = time.time()
            dt = t1-t0
            countdownFinished = True
            pygame.display.update()
        # pygame.draw.rect(display_surface, (255, 255, 255), (960, 0, 30, 125))
        pygame.display.update()


def SetCarMaxSpeed(car, pad_group, car_group):
    on_track = pygame.sprite.groupcollide(
        car_group, pad_group, False, False)

    # Slow down car if not on track
    if not on_track:
        car.MAX_FORWARD_SPEED = 3
    else:
        car.MAX_FORWARD_SPEED = 20


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


def getEvent2(car2, event, display_surface):
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
