"""
Пространство для тестов.
"""
import pygame as pg

from tasks.Chess import Board
from tasks.Half_miner import MinerBoard

if __name__ == '__main__':
    match input():
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
            # Во время движения отрисовывает нормально. После движения плохо запоминает.
            # Можно запоминать прямоугольники и каждый раз их отрисовывать.
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
                            # w, h = event.pos[0], event.pos[1]
                            if drawing:
                                # Не рисует с отрицательными координатами
                                screen2.fill(bgc)
                                screen2.blit(screen, (0, 0))
                                coords = (min(x1, x1 + w), min(y1, y1 + h))
                                pg.draw.rect(screen2, sub_color, (coords, (abs(w), abs(h))), 1)

                                # pg.draw.rect(screen2, sub_color, (top_coords, bottom_coords), 1)
                        case pg.MOUSEBUTTONUP:
                            # ПРОБЛЕМА!!!!
                            # Переработать систему с top / bottom. Необходимо искать минимальную пару точек.
                            # Хотя стоп...
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
            screen = pg.display.set_mode((width, height))
            pg.init()
            board = MinerBoard(len_side, count_squares, list())

            running = True
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                board.draw(screen)
                pg.display.flip()

        case _:
            print("Неправильный ввод")

    pg.quit()
