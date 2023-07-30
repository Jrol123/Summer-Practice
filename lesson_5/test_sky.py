import os.path
from random import randint, randrange
import pygame as pg

width = 800
height = 600


class Star(pg.sprite.Sprite):

    def __init__(self, *group):
        super().__init__(*group)

        self.len = randint(1, 100)

        self.image = pg.Surface((self.len, self.len))
        pg.draw.circle(self.image, (200, 200, 200), (self.len // 2, self.len // 2), self.len // 2)

        self.rect = self.image.get_rect()
        self.x = self.rect.x = randrange(width)
        self.y = self.rect.y = randrange(height)

    def update(self):
        self.x += 0.1 * (self.len // 2)
        self.y += 0.05
        self.rect.x = self.x % width
        self.rect.y = self.y % height


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


screen = pg.display.set_mode((width, height))
pg.init()
pg.display.set_caption("Task - A")

all_sprites = pg.sprite.Group()
for _ in range(100):
    Star(all_sprites)

fps = 100
clock = pg.time.Clock()

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill('black')
    all_sprites.draw(screen)
    all_sprites.update()

    pg.display.flip()
    clock.tick(fps)
