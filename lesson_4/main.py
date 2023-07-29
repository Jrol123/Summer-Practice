"""
Пространство для тестов.
"""
from random import randint

import pygame as pg

from tasks.Chess import Board
from tasks.Half_miner import MinerBoard
from tasks.Multip_table import Table

if __name__ == '__main__':
    match input("\nВведите\nНомер задания:\n"):
        case 'A':
            len_side, count_squares = map(int, input().split())
            screen = pg.display.set_mode((len_side, len_side))
            pg.init()
            board = Board(len_side, count_squares)

            running = True
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                board.draw(screen)
                pg.display.flip()

        case 'C':
            # Реализовано через запоминание фигур
            # Не совсем понимаю, как можно это провернуть со множеством screen, ведь они будут перекрывать друг-друга!
            bgc = (0, 0, 0)
            sub_color = (255, 255, 255)

            size_screen = tuple(map(int, input().split()))
            screen = pg.display.set_mode(size_screen)
            screen2 = pg.display.set_mode(size_screen)
            list_surface = []
            """Координаты левой верхней точки + ширина + высота"""
            pg.init()

            x1, y1, w, h = 0, 0, 0, 0
            drawing = False

            running = True
            while running:
                for event in pg.event.get():
                    match event.type:
                        case pg.QUIT:
                            running = False
                        case pg.MOUSEBUTTONDOWN:
                            drawing = True
                            screen2.fill(bgc)
                            x1, y1 = event.pos
                        case pg.MOUSEMOTION:
                            """
                            Отрисовка на доп. экране.
                            
                            Позже прикрепляется к основному экрану.
                            """
                            w, h = event.pos[0] - x1, event.pos[1] - y1
                            if drawing:
                                screen2.fill(bgc)
                                screen2.blit(screen, (0, 0))
                                coords = (min(x1, x1 + w), min(y1, y1 + h))
                                pg.draw.rect(screen2, sub_color, (coords, (abs(w), abs(h))), 1)
                        case pg.MOUSEBUTTONUP:
                            drawing = False

                            coords = (min(x1, x1 + w), min(y1, y1 + h))
                            list_surface.append((coords, (abs(w), abs(h))))
                            screen.fill(bgc)
                            for entity in list_surface:
                                pg.draw.rect(screen, sub_color, entity, 1)
                        case pg.KEYDOWN:
                            if not (event.key == pg.K_z and pg.key.get_mods() & pg.KMOD_CTRL):
                                continue
                            list_surface.pop(-1)
                            screen.fill(bgc)
                            for entity in list_surface:
                                pg.draw.rect(screen, sub_color, entity, 1)
                if drawing:
                    screen.blit(screen2, (0, 0))
                    for entity in list_surface:
                        pg.draw.rect(screen, sub_color, entity, 1)
                pg.display.flip()

        case 'D':
            len_side, count_squares = map(int, input().split())
            screen = pg.display.set_mode((len_side, len_side))
            pg.init()
            map_mines = [[False, False, True, True],
                         [False, True, False, True],
                         [False, False, False, False],
                         [True, False, False, False]]
            board = MinerBoard(len_side, count_squares)

            running = True
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    if event.type == pg.MOUSEBUTTONDOWN:
                        board.get_click(event.pos)
                board.draw(screen)
                pg.display.flip()

        case 'E':
            bgc = (0, 0, 0)

            # 600 360 1
            # 600 180 1
            # 600 40 1
            # 0.01

            len_side, count_nums = (
                map(int, input("\nВведите\nДлину стороны экрана _ Количество цифр:\n").split()))
            start_multip, step = map(float, input("\nВведите\nНачальный множитель _ Шаг множителя:\n").split())
            fps, lim_fps = map(
                int, input(
                    "\nВведите\nНачальная скорость выполнения программы _ Максимальная скорость выполнения программы:\n").split())
            screen = pg.display.set_mode((len_side, len_side))
            pg.init()

            table = Table(len_side, count_nums, start_multip, step)

            delta_s = 0.1
            delta_h = 0.1

            sub_color = pg.Color(100, 100, 100)
            s = float(randint(0, 100 - 1))
            h = float(randint(0, 256 - 1))
            sub_color.hsva = (h,  s, 100, 100)

            running = True
            drawing = True

            clock = pg.time.Clock()

            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                    if event.type == pg.KEYDOWN:
                        keys = pg.key.get_pressed()

                        if keys[pg.K_SPACE]:
                            drawing = not drawing
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if pg.mouse.get_pressed()[0]:
                            fps = fps % lim_fps + 1
                        else:
                            fps = fps % lim_fps + 10

                if not drawing:
                    continue

                screen.fill(bgc)
                table.draw(screen, sub_color)
                sub_color = (h, s, 100, 100)

                font = pg.font.Font(None, len_side // 25)
                cur_fps_text = font.render(f'{fps}', 1, (255, 255, 255))
                text_x = len_side - cur_fps_text.get_width() - 10
                text_y = 10
                screen.blit(cur_fps_text, (text_x, text_y))

                table.draw_stat(screen, (255, 255, 255))
                table.cur_multip += table.step_mul
                pg.display.flip()

                s += delta_s * randint(1, 2)
                h += delta_h * randint(1, 2)
                if not (0 + delta_s * 2 <= s <= 100 - delta_s * 2):
                    delta_s = -delta_s
                if not (0 + delta_h * 2 <= h <= 256 - delta_h * 2):
                    delta_h = -delta_h

                clock.tick(fps)
        case _:
            print("Неправильный ввод")

    pg.quit()
