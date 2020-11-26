import pygame
import math
import os
from kartingpros import loadimage
from kartingpros.loadimage import _load_image,_load_sound,_load_font
# Track class, makes surface of track

def checkpoint(surface):
    pygame.draw.rect(surface, (255, 255, 255), (960, 50, 20, 125))

def _load_image(relative_image_path, colorkey=False):
    """ Utility method to load the images. It handles if the images contain
    transparency, and relative paths.
    """
    current_path = os.path.abspath(os.path.dirname(__file__))
    absolute_image_path = os.path.join(current_path, relative_image_path)

    image = pygame.image.load(absolute_image_path)
    return image

class Track:
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

    # Static method creates oval track using sin, cos
    def makePads(self):
        center_x = 1980 / 2
        center_y = 1020 / 2
        pads = []
        for r in range(4):
            for i in range(int(360)):
                radian = math.radians(i)
                pad_x = math.floor(
                    (math.cos(radian) * (650 + 32 * r) + center_x))
                pad_y = math.floor(
                    (math.sin(radian) * (350 + 32 * r) + center_y))
                pads.append(RoadSquares((pad_x, pad_y)))
                if r == 1:
                    self.inner_track.append((pad_x, pad_y))
                elif r == 4:
                    self.outer_track.append((pad_x, pad_y))

        return pygame.sprite.RenderPlain(*pads)

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

    def update(self):
        pass