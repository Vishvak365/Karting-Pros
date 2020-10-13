import pygame

class Track(pygame.sprite.Sprite):

    black = pygame.image.load('images/track_black.png')

    def __init__(self, position):
        super(Track, self).__init__()
        self.rect = pygame.Rect(self.normal.get_rect())
        self.rect.center = position

        pads = [
            Track((0, 10)),
            Track((600, 10)),
            Track((1100, 10)),
            Track((100, 150)),
            Track((600, 150)),
        ]

        pad_group = pygame.sprite.RenderPlain(*pads)