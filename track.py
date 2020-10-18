import pygame
import math


class Track:

    def __init__(self):
        self.pads = []
        self.pads = self.makePads()

    def update(self):
        pass
# 1920 v 1080
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
                    (math.sin(radian) * (400 + 32 * r) + center_y))
                # print(pad_x)
                # print(pad_y)
                pads.append(RoadSquares((pad_x, pad_y)))

        return pygame.sprite.RenderPlain(*pads)

    def getPads(self):
        return self.pads


class RoadSquares(pygame.sprite.Sprite):
    black = pygame.image.load('images/track_black.png')

    def __init__(self, position):
        super(RoadSquares, self).__init__()
        self.image = self.black
        self.rect = pygame.Rect(self.black.get_rect())
        self.rect.center = position

    def update(self):
        pass


# for i in range(int(128)):
#     for x in range(int(72)):
#         x_val = 10 * i
#         y_val = 10 * x
#         if (y_val > 80 and x_val > 80):
#             continue
#         else:
#             pads.append(Track((x_val, y_val)))
#
# for i in range(int(128)):
#     for x in range(int(72)):
#         x_val = 10 * i
#         y_val = 10 * x
#         if (y_val < 640 and x_val < 1200):
#             continue
#         else:
#             pads.append(Track((x_val, y_val)))
#
# pad_group = pygame.sprite.RenderPlain(*pads)
