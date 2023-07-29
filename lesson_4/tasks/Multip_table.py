"""
E. Таблица умножения.
"""
import pygame as pg
from math import sin, cos, radians


class Table:
    def __init__(self, len_screen: int, count_nums: int, start_multip: float = 2.0, step_mul: float = 0.001):
        self.len_screen = len_screen
        self.radius = len_screen // 2 - len_screen // 15
        self.step_mul = step_mul
        self.step_rad = 360 // count_nums
        # count_nums <= 360. else — error
        # Хотя, если переделать range в draw...
        self.cur_multip = float(start_multip)

        self.list_nums = []

    def draw(self, screen: pg.Surface,
             color: pg.Color | tuple[int, int, int] = (0, 191, 255),
             bgc: pg.Color | tuple[int, int, int] = (0, 0, 0),
             width: int = 1) -> None:
        """
        Отрисовывание таблицы умножения.

        :param bgc: Цвет фона.
        :type bgc: pg.Color | tuple[int, int, int]
        :param color: Цвет всего.
        :type color: pg.Color | tuple[int, int, int]
        :param width: Ширина границ круга.
        :type width: int
        :param screen: Экран, на котором будет выведен текст.
        :type screen: pg.Surface

        """

        for rad in range(0, 360, self.step_rad):
            pg.draw.circle(screen, color, (self.len_screen // 2, self.len_screen // 2), self.radius, width)
            start_pos = (int(cos(radians(rad)) * self.radius) + self.len_screen // 2,
                         int(sin(radians(rad)) * self.radius) + self.len_screen // 2)
            end_pos = (int(cos(radians(rad * self.cur_multip)) * self.radius) + self.len_screen // 2,
                       int(sin(radians(rad * self.cur_multip)) * self.radius) + self.len_screen // 2)
            pg.draw.line(screen, color, start_pos, end_pos)

    def draw_stat(self, screen: pg.Surface, color: pg.Color | tuple[int, int, int] = (0, 191, 255)) -> None:
        """
        Отрисовывание текущего множителя.

        :param screen: Экран, на котором будет выведен текст.
        :type screen: pg.Surface
        :param color: Цвет текста.
        :type color: pg.Color | tuple[int, int, int]

        """
        font = pg.font.Font(None, self.len_screen // 25)
        cur_multiplier_text = font.render(f'{self.cur_multip:.3f}', 1, color)
        text_x = 10
        text_y = 10
        screen.blit(cur_multiplier_text, (text_x, text_y))
