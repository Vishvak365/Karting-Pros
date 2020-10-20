import pygame
import math


# Track class, makes surface of track

def checkpoint(surface):
    pygame.draw.rect(surface, (255, 255, 255), (960, 50, 20, 125))


class Track:
    # Constructor calls static function to make track, track is list of extended sprite class objects
    def __init__(self):
        self.pads = []
        self.pads = self.makePads()

    def update(self):
        pass

    # Static method creates oval track using sin, cos
    @staticmethod
    def makePads():
        center_x = 1980 / 2
        center_y = 1020 / 2
        width = 50
        pads = []
        for r in range(4):
            for i in range(int(360)):
                radian = math.radians(i)
                pad_x = math.floor(
                    (math.cos(radian) * (650 + 32 * r) + center_x))
                pad_y = math.floor(
                    (math.sin(radian) * (350 + 32 * r) + center_y))
                pads.append(RoadSquares((pad_x, pad_y)))

        return pygame.sprite.RenderPlain(*pads)

    # Getter for list of road square objects
    def getPads(self):
        return self.pads


# Black 32x32 squares to make the road
class RoadSquares(pygame.sprite.Sprite):
    black = pygame.image.load(r'../KartingPros/images/track_black.png')

    def __init__(self, position):
        super(RoadSquares, self).__init__()
        self.image = self.black
        self.rect = pygame.Rect(self.black.get_rect())
        self.rect.center = position

    def update(self):
        pass
