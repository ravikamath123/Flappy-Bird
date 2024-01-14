import pygame as pg
import sys

GAME_WIDTH = 1000
GAME_HEIGHT = 700
BACKGROUND_COLOR = (0, 255, 0)

pg.init()

clock = pg.time.Clock()
window = pg.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pg.display.set_caption("Flappy Bird")

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    pg.display.flip()

