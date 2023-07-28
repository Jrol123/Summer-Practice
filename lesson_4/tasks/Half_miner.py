"""
D. Полусапёр.
"""
import random

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
    :ivar map_numbers: Карта цифр. -1 — нет цифры
    :type map_numbers: list[list[int]]

    :param length: Длина стороны доски.
    :type length: int
    :param count_cells: Количество квадратов.
    :type count_cells: int
    :param map_mines: Карта мин. True — мина есть.
    :type map_mines: list[list[bool]]

    """

    # Ошибка на 1100 40
    def __init__(self, length: int, count_cells: int, map_mines: list[list[bool]] = list()):
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
        self.map_mines = map_mines
        if len(map_mines) == 0:
            for i in range(count_cells):
                self.map_mines.append([])
                for _ in range(count_cells):
                    self.map_mines[i].append(random.choice([True, False]))

        self.map_numbers = []
        for i in range(count_cells):
            self.map_numbers.append([])
            for _ in range(count_cells):
                self.map_numbers[i].append(-1)

    def draw(self, screen: pg.Surface,
             colors: tuple[pg.Color | tuple[int, int, int], pg.Color | tuple[int, int, int]]
             = ((255, 255, 255), pg.Color('red')), width: int = 1) -> None:
        """
        Отрисовывание доски на заданном экране.

        :param screen: Экран, на котором будет выведена доска
        :type screen: pg.Surface
        :param colors: Цвета, использующиеся для отрисовки квадратов доски.
        :type colors: tuple[pg.Color | tuple[int, int, int], pg.Color | tuple[int, int, int]]
        :param width: Ширина границы клетки
        :type width: int

        """
        screen.fill('black')
        for index_side, side in enumerate(self.cell_begin_coords):
            for index_cell, coord in enumerate(side):
                x, y = coord
                """Границы квадратов"""
                pg.draw.rect(screen, colors[0], (x, y, self.cell_len, self.cell_len), width)

                if self.map_mines[index_side][index_cell]:
                    """Если есть мина"""
                    pg.draw.rect(screen, colors[1],
                                 (x + width, y + width,
                                  self.cell_len - 2 * width, self.cell_len - 2 * width))
                    # При обрисовке мин — отступ на width и уменьшение ширины-высоты на 2 * width

                elif self.map_numbers[index_side][index_cell] >= 0:
                    """Если пользователь поставил цифру"""
                    font = pg.font.Font(None, self.cell_len // 2)
                    text = font.render(f'{self.map_numbers[index_side][index_cell]}', 1, (0, 191, 255))
                    screen.blit(text, ((x + self.cell_len // 2) - text.get_width() // 2,
                                       (y + self.cell_len // 2) - text.get_height() // 2))

        # в теории можно просто заливать изменившиеся ячейки чёрным

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos: tuple[int, int]) -> tuple[int, int]:
        pos_x, pos_y = mouse_pos
        return pos_x // self.cell_len, pos_y // self.cell_len

    def on_click(self, cell):
        column, row = cell

        if self.map_mines[row][column]:
            return
        elif self.map_numbers[row][column] != -1 and not self.map_mines[row][column]:
            self.map_numbers[row][column] = -1
            return

        cur_count = 0
        if row == 0:
            row_check = range(0, row + 1 + 1)
        else:
            row_check = range(row - 1, row + 1 + 1)
        if column == 0:
            column_check = range(0, column + 1 + 1)
        else:
            column_check = range(column - 1, column + 1 + 1)
        for r in row_check:
            for c in column_check:
                cur_count += int(self.map_mines[r][c])
        self.map_numbers[row][column] = cur_count
