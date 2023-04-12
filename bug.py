import pygame as pg
import random

class bug:
    def __init__(self, w, h, main_screen) -> None:
        self.mSurface = pg.Surface((w,h))
        self.speed = 10
        scr_w, scr_h = main_screen.get_size()
        self.pos = get_spawn_pos(scr_w, scr_h)
        self.state = 0
        self.path = 0
        self.ability = 0

        self.mSurface.fill("white")
        main_screen.blit(self.mSurface, self.pos)

def get_spawn_pos(w, h):
    pos_x = random.randrange(1, w)
    pos_y = random.randrange(1, h)
    return pos_x, pos_y