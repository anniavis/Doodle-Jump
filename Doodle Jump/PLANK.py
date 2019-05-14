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


class BluePlank(Plank):
    """ This class contains information about blue planks. """

    def __init__(self, x_plank, y_plank):
        super().__init__(x_plank, y_plank)
        self.plank_picture = pygame.image.load('BluePlankMini.png')
        self.speed = 5
        self.width = 54

    def moving(self):
        if self.x_coord > 5 and self.speed < 0:
            self.x_coord += self.speed
        elif self.speed < 0:
            self.speed *= -1
            self.x_coord += self.speed

        if self.x_coord < 313 - self.width - 5 and self.speed > 0:
            self.x_coord += self.speed
        elif self.speed > 0:
            self.speed *= -1
            self.x_coord += self.speed

    def render(self, win):
        self.moving()
        if -13 <= self.y_coord <= 513:
            win.blit(self.plank_picture, (self.x_coord, self.y_coord))
