import pygame as pg
from sys import exit
from bug import bug
from ui import Ui

pg.init()

scr_width = 800
scr_height = 600

mainscreen = pg.display.set_mode((scr_width, scr_height))
clock = pg.time.Clock()

font = pg.font.Font(None, 50)
test = Ui("Hello", "white", "purple", (100, 30), font, mainscreen)

newbug = bug(25, 40, mainscreen)


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

    

    pg.display.update()
    clock.tick(60)