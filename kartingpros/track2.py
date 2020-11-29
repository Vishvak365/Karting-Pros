import pygame
import math
import os
from kartingpros import loadimage
from kartingpros.loadimage import _load_image,_load_sound,_load_font
# Track class, makes surface of track

def checkpoint(surface):
    pygame.draw.rect(surface, (255, 255, 255), (960, 50, 20, 125))


class Track2:
    # Constructor calls static function to make track, track is list of extended sprite class objects
    def __init__(self):
        self.pads = []
        self.finish_line = (960, 50, 20, 125)
        # inner and outer track set in makePads
        self.inner_track = []
        self.outer_track = []
        self.pads = self.makePads()

    def update(self):
        pass

    def getFinishLine(self):
        return self.finish_line

    def getInnerTrack(self):
        return self.inner_track

    def getOuterTrack(self):
        return self.outer_track

    def makePads(self):
        center_x = 1980 / 2
        center_y = 1020 / 2
        pads = []
        # self.finish_line = (960, 50, 20, 125)
        lastx = 0
        lasty = 0
        for r in range(4):
            for i in range(16):
                pad_x = math.floor(
                    (960 + 16 + 32 * i))
                pad_y = math.floor(
                    (50 + 16 + 32 * r))
                pads.append(RoadSquares((pad_x, pad_y)))
                if r == 0 and i == 15:
                    lastx = pad_x
                    lasty = pad_y

        # last pad_x furthest to the right
        # last pad_y is shallowest
        curve_center_x = lastx
        curve_center_y = lasty + 3 * 32
        print(curve_center_x)
        print(curve_center_y)
        turn_pads = self.MakeTurn(curve_center_x, curve_center_y, -90, 0)
        pads.append(turn_pads)

        curve_center_x = curve_center_x + 4 * 32
        curve_center_y = curve_center_y + 32
        turn_pads = self.MakeTurn(curve_center_x, curve_center_y, -270, -180)
        pads.append(turn_pads)
        for r in range(4):
            for i in range(5):
                pad_x = math.floor(
                    (curve_center_x + 32 * i))
                pad_y = math.floor(
                    (curve_center_y + 32 * r))
                pads.append(RoadSquares((pad_x, pad_y)))
                if r == 0 and i == 4:
                    lastx = pad_x
                    lasty = pad_y
        curve_center_x = lastx + 32
        curve_center_y = lasty + 3 * 32
        turn_pads = self.MakeTurn(curve_center_x, curve_center_y, -90, 0)
        pads.append(turn_pads)
        for r in range(18):
            for i in range(5):
                pad_x = math.floor(
                    (curve_center_x + 32 * i))
                pad_y = math.floor(
                    (curve_center_y + 32 * r))
                pads.append(RoadSquares((pad_x, pad_y)))
                if r == 17 and i == 4:
                    lastx = pad_x
                    lasty = pad_y

        curve_center_x = lastx - 4 * 32
        curve_center_y = lasty + 32
        turn_pads = self.MakeTurn(curve_center_x, curve_center_y, -360, -270)
        pads.append(turn_pads)
        curve_center_x = lastx - 4 * 32
        curve_center_y = lasty + 32
        for r in range(40):
            for i in range(4):
                pad_x = math.floor(
                    (curve_center_x - 32 * r))
                pad_y = math.floor(
                    (curve_center_y + 32 * i))
                pads.append(RoadSquares((pad_x, pad_y)))
                if r == 39 and i == 0:
                    lastx = pad_x
                    lasty = pad_y

        curve_center_x = lastx
        curve_center_y = lasty
        turn_pads = self.MakeTurn(curve_center_x, curve_center_y, -270, -180)
        pads.append(turn_pads)
        curve_center_x = lastx - 4 * 32
        curve_center_y = lasty - 32
        turn_pads = self.MakeTurn(curve_center_x, curve_center_y, -90, 0)
        pads.append(turn_pads)
        curve_center_x = lastx - 4 * 32
        curve_center_y = lasty - 4 * 32
        turn_pads = self.MakeTurn(curve_center_x, curve_center_y, -270, -180)
        pads.append(turn_pads)

        curve_center_x = curve_center_x - 4 * 32
        curve_center_y = curve_center_y - 32
        turn_pads = self.MakeTurn(curve_center_x, curve_center_y, -90, 0)
        pads.append(turn_pads)
        curve_center_x = curve_center_x - 32
        curve_center_y = curve_center_y - 32 * 3
        turn_pads = self.MakeTurn(curve_center_x, curve_center_y, -271, -180)
        pads.append(turn_pads)
        curve_center_x = curve_center_x - 32 * 4
        curve_center_y = curve_center_y - 32
        for r in range(13):
            for i in range(4):
                pad_x = math.floor(
                    (curve_center_x + 32 * i))
                pad_y = math.floor(
                    (curve_center_y - 32 * r))
                pads.append(RoadSquares((pad_x, pad_y)))
                if r == 12 and i == 0:
                    lastx = pad_x
                    lasty = pad_y
        curve_center_x = lastx + 4*32
        curve_center_y = lasty -32
        turn_pads = self.MakeTurn(curve_center_x, curve_center_y, -180, -90)
        pads.append(turn_pads)

        for r in range(24):
            for i in range(4):
                pad_x = math.floor(
                    (curve_center_x + 32 * r))
                pad_y = math.floor(
                    (curve_center_y - 32 * i))
                pads.append(RoadSquares((pad_x, pad_y)))
                if r == 12 and i == 0:
                    lastx = pad_x
                    lasty = pad_y
        return pygame.sprite.RenderPlain(*pads)

    def MakeTurn(self, curve_center_x, curve_center_y, start_angle, end_angle):
        pads = []
        degree_angle = start_angle
        for r in range(4):
            while degree_angle <= end_angle:
                radian = math.radians(degree_angle)
                pad_x = math.floor(
                    (math.cos(radian) * (r * 32 + 32) + curve_center_x))
                pad_y = math.floor(
                    (math.sin(radian) * (r * 32) + curve_center_y))
                pads.append(RoadSquares((pad_x, pad_y)))
                degree_angle = degree_angle + 1
            degree_angle = start_angle
        return pads

    # Getter for list of road square objects
    def getPads(self):
        return self.pads


# Black 32x32 squares to make the road
class RoadSquares(pygame.sprite.Sprite):
    black = _load_image("./images/track_black.png")

    def __init__(self, position):
        super(RoadSquares, self).__init__()
        self.image = self.black
        self.rect = pygame.Rect(self.black.get_rect())
        self.rect.center = position

    def getPosition(self):
        return self.rect.center

    def update(self):
        pass
