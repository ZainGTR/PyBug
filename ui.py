import pygame as pg

class Ui:
    def __init__(self, text, color, bg_color, size, font, main_screen) -> None:
        self.text = text
        self.color = color
        self.bg_color = bg_color
        self.mSurface = pg.Surface(size)
        self.render = font.render(text, True, color)

        self.mSurface.fill(bg_color)
        self.mSurface.blit(self.render, (0, 0))
        main_screen.blit(self.mSurface, (200, 50))