import pygame
import random
from PLANK import Plank
from PLANK import BluePlank
from DOODLER import Doodler


class Game:
    """ This is the main class of our project. """

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Doodle Jump")
        self.run = True
        self.all_planks = []
        self.doodle = Doodler()
        self.win = pygame.display.set_mode((313, 500))
        self.walkRight = pygame.image.load('RightMini.png')
        self.walkLeft = pygame.image.load('LeftMini.png')
        self.background = pygame.image.load('Back.jpg')
        self.label = 0
        pygame.font.init()
        self.font_size = 20
        self.font_size_end = 50
        self.font = pygame.font.Font('15695.ttf', self.font_size)
        self.font_end = pygame.font.Font('15695.ttf', self.font_size_end)
        self.best_score = 0

    def HandleKeyPressures(self):
        """ This method is used for keyboard processing. """

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.doodle.x_coord > 5:
            self.doodle.x_coord -= self.doodle.speed
            self.doodle.left = True
            self.doodle.right = False
        elif keys[pygame.K_RIGHT] and self.doodle.x_coord < 313 - self.doodle.width - 5:
            self.doodle.x_coord += self.doodle.speed
            self.doodle.left = False
            self.doodle.right = True

    def draw_window(self):
        """ This method is used for drawing the background, the doodler and the score. """

        self.win.blit(self.background, (0, 0))
        self.win.blit(self.font.render(str(int(self.doodle.score)), True, (0, 0, 0)), (5, 5))

        if self.label == 0:
            self.win.blit(self.walkRight, (self.doodle.x_coord, self.doodle.y_coord))

        if self.doodle.left:
            self.win.blit(self.walkLeft, (self.doodle.x_coord, self.doodle.y_coord))
            self.label = 1
        elif self.doodle.right:
            self.win.blit(self.walkRight, (self.doodle.x_coord, self.doodle.y_coord))
            self.label = 1

        pygame.display.update()

    def play(self):
        """ This method contains the main loop. If you loose, you can start again. """

        while self.run:
            done = True
            self.Generate_Planks()
            while done:
                pygame.time.delay(50)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False

                self.HandleKeyPressures()

                vector = self.doodle.UpdateDoodlerCoordinates(self.all_planks)

                if self.doodle.get_contact(self.all_planks) and vector:
                    self.doodle.jumpCount = 10
                self.draw_window()
                for platform in self.all_planks:
                    platform.render(self.win)
                pygame.display.update()

                if self.doodle.y_coord > 500:
                    done = False

            self.win.fill((0, 0, 0))
            end_screen = True
            self.doodle.speed = 0
            self.all_planks.clear()
            self.win.blit(self.background, (0, 0))

            if self.doodle.score > self.best_score:
                self.best_score = self.doodle.score

            self.win.blit(self.font.render("Best score:", True, (0, 0, 0)), (10, 205 - self.font_size))
            self.win.blit(self.font_end.render(str(int(self.best_score)), True, (0, 0, 0)), (10, 210))
            self.win.blit(self.font.render("Your score:", True, (0, 0, 0)), (10, 405 - self.font_size))
            self.win.blit(self.font_end.render(str(int(self.doodle.score)), True, (0, 0, 0)), (10, 410))
            self.win.blit(self.font.render("Press Enter to play again!", True, (0, 0, 0)), (25, 55))
            pygame.display.update()
            while end_screen:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.run = False
                        end_screen = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            end_screen = False
            self.doodle.speed = 10
            self.doodle.x_coord = 50
            self.doodle.y_coord = 425
            self.doodle.jumpCount = 10
            self.doodle.score = 0

    def Generate_Planks(self):
        """ This method generates planks. """

        for i in range(1000):
            plank = None
            if i % 10 == 0:
                plank = BluePlank(random.randint(5, 243), 500 - 100 * i - random.randint(40, 100))
            else:
                plank = Plank(random.randint(5, 243), 500 - 100 * i - random.randint(40, 100))
            self.all_planks.append(plank)
