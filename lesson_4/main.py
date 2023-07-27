"""
Пространство для тестов.
"""
import pygame as pg

bgc = (255, 255, 255)


class Board:
    def __int__(self, width: int, height: int):
        """

        Единицы измерения — пиксели.
        :param width: ширина
        :param height: высота
        """
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


if __name__ == '__main__':
    size = width, height = (400, 300)
    screen = pg.display.set_mode(size)
    pg.init()

    # board = Board(5, 7)
    running = True
    x_pos = 0
    speed = 20  # pix per sec
    delta_speed = 10
    max_speed = 500
    radius = 20
    clock = pg.time.Clock()
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                speed = (speed + delta_speed) % max_speed
        screen.fill(bgc)
        pg.draw.circle(screen, (255, 0, 0), (x_pos, 200), radius)
        x_pos = (x_pos + speed * clock.tick() / 1000) % (width + radius)
        pg.display.flip()

    pg.quit()
