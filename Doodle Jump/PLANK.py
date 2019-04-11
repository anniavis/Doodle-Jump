import pygame


class Plank:
    """ This class contains information about our planks. """

    def __init__(self, x_plank, y_plank):
        self.x_coord = x_plank
        self.y_coord = y_plank
        self.width = 60
        self.height = 13
        self.plank_picture = pygame.image.load('PlankMini.png')

    def render(self, win):
        """ This method is used for drawing planks. """
        if -13 <= self.y_coord <= 513:
            win.blit(self.plank_picture, (self.x_coord, self.y_coord))
