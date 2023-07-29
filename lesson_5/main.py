"""
Место тестирования.
"""
import os.path

import pygame as pg


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pg.image.load(fullname).convert()
    except pg.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    len_side = 640
    count_squares = 32
    len_square = len_side // count_squares
    screen = pg.display.set_mode((len_side, len_side))
    pg.init()

    image = load_image("maxresdefault.jpg", -1)
    image = pg.transform.scale(image, (len_side, len_side))

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.blit(image, (0, 0))

        pg.display.flip()

    # match input("Введите\nНомер задания:\n"):
    #     case 'A':
    #         pass
    #     case _:
    #         print("Неправильный ввод.")
