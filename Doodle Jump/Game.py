import pygame
import random

pygame.init()
win = pygame.display.set_mode((313, 500))  # Переменная, отвечающая за окно

pygame.display.set_caption("Doodle Jump")  # Название

walkRight = pygame.image.load('RightMini.png')
walkLeft = pygame.image.load('LeftMini.png')
background = pygame.image.load('Back.jpg')
plank_picture = pygame.image.load('PlankMini.png')


class Game:
    def __init__(self):
        self.run = True
        self.score = 0

    def play(self, doodler):
        global left, right, jumpCount

        while self.run:
            pygame.time.delay(50)  # Цикл выполняется каждую 0,1 секунды

            for event in pygame.event.get():  # Перебираем возможные события
                if event.type == pygame.QUIT:
                    self.run = False

            keys = pygame.key.get_pressed()  # Кнопки, на к-е нажимаем
            if keys[pygame.K_LEFT] and doodler.x > 5:
                doodler.x -= doodler.speed
                left = True
                right = False
            elif keys[pygame.K_RIGHT] and doodler.x < 313 - doodler.width - 5:
                doodler.x += doodler.speed
                left = False
                right = True
            vector = True
            if isJump:
                if jumpCount >= -20:
                    if jumpCount < 0:
                        doodler.y += (jumpCount ** 2) / 2
                        self.score += (jumpCount ** 2) / 2
                        vector = True
                    else:
                        if doodler.y <= 120:  # прокручиваем вниз
                            for platform in Plank.all_planks:
                                platform.y += (jumpCount ** 2) / 2
                        else:
                            doodler.y -= (jumpCount ** 2) / 2
                        vector = False
                    jumpCount -= 1
                else:
                    jumpCount = 10

            if doodler.get_contact(right) and vector:
                jumpCount = 10
            draw_window(doodler)
            for platform in Plank.all_planks:
                platform.render()
            pygame.display.update()


class Doodler:
    def __init__(self):
        self.x = 50
        self.y = 425
        self.width = 60
        self.height = 60
        self.speed = 10

    def get_contact(self, right):
        for platform in Plank.all_planks:
            if right:
                if (self.y + self.height - 40 <= platform.y <= self.y + self.height) and \
                        (platform.x <= self.x <= (platform.x + 50) or
                            platform.x + 10 <= self.x + self.width <= platform.x + platform.width):
                    self.y = platform.y - self.height
                    return True
            else:
                if (self.y + self.height - 40 <= platform.y <= self.y + self.height) and \
                        (platform.x <= self.x <= (platform.x + 50) or
                            platform.x + 10 <= self.x + self.width <= platform.x + platform.width):
                    self.y = platform.y - self.height
                    return True
        return False


doodle = Doodler()


class Plank:

    all_planks = []

    def __init__(self, x_plank, y_plank):
        self.x = x_plank
        self.y = y_plank
        self.width = 60
        self.height = 13
        Plank.all_planks.append(self)

    def render(self):
        if -13 <= self.y <= 513:
            win.blit(plank_picture, (self.x, self.y))


isJump = True
jumpCount = 10

left = False
right = False

label = 0


def draw_window(doodler):
    global label

    win.blit(background, (0, 0))

    if label == 0:
        win.blit(walkRight, (doodler.x, doodler.y))

    if left:
        win.blit(walkLeft, (doodler.x, doodler.y))
        label = 1
    elif right:
        win.blit(walkRight, (doodler.x, doodler.y))
        label = 1

    pygame.display.update()


for i in range(1000):
    plank = Plank(random.randint(5, 243), 500 - 100 * i - random.randint(40, 100))

game = Game()
game.play(doodle)

pygame.quit()  # Выход из приложения
