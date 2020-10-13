# import pygame module in this program
import pygame
# import Track
import time
# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value
# for white colour
white = (255, 255, 255)

# assigning values to X and Y variable
X = 1280
Y = 720

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Image')

# create a surface object, image is drawn on it.
image = pygame.image.load(
    r'images\car.png')
car_y = 100
# infinite loop

class Track(pygame.sprite.Sprite):
    black = pygame.image.load('images/track_black.png')

    def __init__(self, position):
        super(Track, self).__init__()
        self.image = self.black
        self.rect = pygame.Rect(self.black.get_rect())
        self.rect.center = position

    def update(self):
        pass

# pads = [
#             Track((0, 10)),
#             Track((10, 10)),
#             Track((20, 10)),
#             Track((30, 10)),
#             Track((40, 10)),
#         ]
pads = []
for i in range(int(128)):
    for x in range(int(72)):
        x_val = 10*i
        y_val = 10 * x
        if (y_val > 80 and x_val >80) :
            continue
        else:
            pads.append(Track((x_val, y_val)))

for i in range(int(128)):
    for x in range(int(72)):
        x_val = 10*i
        y_val = 10 * x
        if (y_val < 640 and x_val <1200) :
            continue
        else:
            pads.append(Track((x_val, y_val)))

pad_group = pygame.sprite.RenderPlain(*pads)

while True:

    # completely fill the surface object
    # with white colour
    display_surface.fill(white)

    # copying the image surface object
    # to the display surface object at
    # (0, 0) coordinate.

    display_surface.blit(image, (0, car_y))
    pad_group.draw(display_surface)
    # if car_y < 500:
    #     time.sleep(1000)
    #     car_y += 10
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():

        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:

            # deactivates the pygame library
            pygame.quit()

            # quit the program.
            quit()

        # Draws the surface object to the screen.
        pygame.display.update()
