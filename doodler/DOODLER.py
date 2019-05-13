import pygame


class Doodler:
    """ This class contains information about the doodler. """
    def __init__(self):
        self.x_coord = 50
        self.y_coord = 425
        self.width = 60
        self.height = 60
        self.speed = 10
        self.jumpCount = 10
        self.right = False
        self.left = False
        self.score = 0

    def get_contact(self, all_planks):
        """ This method checks if any plank intersects with the doodler. """
        for platform in all_planks:
            if self.right:
                if (self.y_coord + self.height - 40 <= platform.y_coord <= self.y_coord + self.height) and \
                        (platform.x_coord <= self.x_coord <= (platform.x_coord + 50) or
                            platform.x_coord + 10 <= self.x_coord + self.width <= platform.x_coord + platform.width):
                    self.y_coord = platform.y_coord - self.height
                    return True
            else:
                if (self.y_coord + self.height - 40 <= platform.y_coord <= self.y_coord + self.height) and \
                        (platform.x_coord <= self.x_coord <= (platform.x_coord + 50) or
                            platform.x_coord + 10 <= self.x_coord + self.width <= platform.x_coord + platform.width):
                    self.y_coord = platform.y_coord - self.height
                    return True
        return False

    def UpdateDoodlerCoordinates(self, all_planks):
        """ This method updates the coordinates of the doodler. """
        vector = True

        if self.jumpCount >= -20:
            if self.jumpCount < 0:
                self.y_coord += (self.jumpCount ** 2) / 2

                vector = True
            else:
                if self.y_coord <= 120:
                    for platform in all_planks:
                        platform.y_coord += (self.jumpCount ** 2) / 2
                    self.score += (self.jumpCount ** 2) / 2
                else:
                    self.y_coord -= (self.jumpCount ** 2) / 2
                vector = False
            self.jumpCount -= 1
        else:
            self.jumpCount = 10

        return vector
