"""
D. Полусапёр.
"""
import pygame as pg
from tasks.Chess import Board


class MinerBoard(Board):
    """
    Класс для представления квадратной доски.

    Длины измеряются в пикселях.

    :ivar length: Длина стороны доски. Также является длиной стороны экрана
    :type length: int
    :ivar cell_len: Длина стороны квадрата.
    :type cell_len: int
    :ivar cell_begin_coords: Список левых верхних точек квадратов.
    :type cell_begin_coords: list[list[tuple[int, int]]]
    :ivar map_mines: Карта мин. True — мина есть.
    :type map_mines: list[list[bool]]

    :param length: Длина стороны доски.
    :type length: int
    :param count_cells: Количество квадратов.
    :type count_cells: int
    :param map_mines: Карта мин. True — мина есть.
    :type map_mines: list[list[bool]]

    """
    def __init__(self, length: int, count_cells: int, map_mines: list[list[bool]]):
        """
        Инициализация класса.

        Единицы измерения — пиксели.
        :param length: Длина стороны доски.
        :type length: int
        :param count_cells: Количество квадратов.
        :type count_cells: int
        :param map_mines: Карта мин. True — мина есть.
        :type map_mines: list[list[bool]]

        """
        super().__init__(length, count_cells)

    def draw(self, screen: pg.Surface,
             colors: tuple[pg.Color | tuple[int, int, int], pg.Color | tuple[int, int, int]]
             = ((255, 255, 255), pg.Color('red'))) -> None:
        """
        Отрисовывание доски на заданном экране.

        :param screen: Экран, на котором будет выведена доска
        :type screen: pg.Surface
        :param colors: Цвета, использующиеся для отрисовки квадратов доски.
        :type colors: tuple[pg.Color | tuple[int, int, int], pg.Color | tuple[int, int, int]]

        """
        for index_side, side in enumerate(self.cell_begin_coords):
            for index_cell, coord in enumerate(side):
                x, y = coord
                color = colors[(index_side + index_cell) % 2]
                pg.draw.rect(screen, color, (x, y, self.cell_len, self.cell_len), 1)
                # Последний аргумент отвечает за заполнение.
        # При обрисовке мин — отступ на width и уменьшение ширины-высоты на 2 * width
