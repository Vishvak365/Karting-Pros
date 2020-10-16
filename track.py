import pygame


class Track(pygame.sprite.Sprite):
    black = pygame.image.load('images/track_black.png')

    def __init__(self, position):
        super(Track, self).__init__()
        self.image = self.black
        self.rect = pygame.Rect(self.black.get_rect())
        self.rect.center = position
        self.pads = []

    def update(self):
        pass

        pads = [
            Track((0, 10)),
            Track((600, 10)),
            Track((1100, 10)),
            Track((100, 150)),
            Track((600, 150)),
        ]

        pad_group = pygame.sprite.RenderPlain(*pads)

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