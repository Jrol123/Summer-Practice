"""
Место тестирования.
"""
from random import randrange, randint

import pygame as pg


class Ball(pg.sprite.Sprite):
    """
    Класс шара.

    В идеале нужно создать под него отдельную группу all_balls.

    """
    def __init__(self, radius: int, x: int, y: int):
        super().__init__(all_sprites)
        self.radius = radius
        self.image = pg.Surface((2 * radius, 2 * radius),
                                pg.SRCALPHA, 32)
        color = pg.Color('red')
        color.hsva = (randint(0, 360),  randint(0, 100), 100, 100)
        pg.draw.circle(self.image, color,
                       (radius, radius), radius)
        self.rect = pg.Rect(x, y, 2 * radius, 2 * radius)
        self.x = x
        self.y = y
        self.vx = speed_var[randint(0, 19)]
        self.vy = speed_var[randint(0, 19)]

    def update(self):
        """
        Обновление спрайта шара.

        Сначала проверяет коллизию со стенками, затем коллизию с мячами. (стенки не входят в all_sprites)

        """
        self.rect = self.rect.move(self.vx, self.vy)

        x1 = horizontal_borders.copy()
        x1.remove(list(x1)[0])
        x2 = horizontal_borders.copy()
        x2.remove(list(x2)[1])
        y1 = vertical_borders.copy()
        y1.remove(list(y1)[0])
        y2 = vertical_borders.copy()
        y2.remove(list(y2)[1])

        if pg.sprite.spritecollide(self, x1, 0) and self.vy > 0:  # Lower
            self.vy = -self.vy
            self.y += 20

        if pg.sprite.spritecollide(self, x2, 0) and self.vy < 0:  # Higher
            self.vy = -self.vy
            self.y -= 20

        if pg.sprite.spritecollide(self, y1, 0) and self.vx > 0:  # Right
            self.vx = -self.vx
            self.x -= 20

        if pg.sprite.spritecollide(self, y2, 0) and self.vx < 0:  # Left
            self.vx = -self.vx
            self.x += 20

        rest_balls = all_sprites.copy()
        rest_balls.remove(self)

        if pg.sprite.spritecollide(self, rest_balls, 0):
            self.vy = -self.vy
            self.vx = -self.vx


class Border(pg.sprite.Sprite):
    # строго вертикальный или строго горизонтальный отрезок
    def __init__(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        if x1 == x2:  # вертикальная стенка
            self.add(vertical_borders)
            self.image = pg.Surface([1, y2 - y1])
            self.rect = pg.Rect(x1, y1, 1, y2 - y1)
        else:  # горизонтальная стенка
            self.add(horizontal_borders)
            self.image = pg.Surface([x2 - x1, 1])
            self.rect = pg.Rect(x1, y1, x2 - x1, 1)


if __name__ == '__main__':

    match input("Введите\nНомер задания:\n"):
        case 'A':
            pg.init()
            width, height = map(int, input('\nwidth _ height:\n').split())
            pg.display.set_caption("Задача - A")
            screen = pg.display.set_mode((width, height))

            all_sprites = pg.sprite.Group()
            horizontal_borders = pg.sprite.Group()
            vertical_borders = pg.sprite.Group()
            sprite = pg.sprite.Sprite()

            clock = pg.time.Clock()

            fps = int(input('\nfps:\n'))

            speed_var = [i for i in range(-10, 11) if i != 0]

            Border(5, 5, width - 5, 5)
            Border(5, height - 5, width - 5, height - 5)
            Border(5, 5, 5, height - 5)
            Border(width - 5, 5, width - 5, height - 5)

            all_sprites.empty()  # Без очистки программа будет проверять коллизии со стенками неправильно
            for _ in range(int(input('\nstart count balls:\n'))):
                Ball(20, randint(25, width - 25), randint(25, height - 25))

            running = True
            while running:
                pos = pg.mouse.get_pos()
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    if event.type == pg.MOUSEBUTTONDOWN:
                        Ball(20, *pos)
                screen.fill((0, 0, 0))
                all_sprites.draw(screen)
                all_sprites.update()
                pg.display.flip()
                clock.tick(fps)

        case 'B':
            pass
        case _:
            print("Неправильный ввод.")
