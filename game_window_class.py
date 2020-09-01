import pygame
from cell_class import *
vec = pygame.math.Vector2

# creating game window


class Game_window:
    def __init__(self, screen, x, y):
        self.pos = vec(x, y)
        self.screen = screen
        self.width, self.height = 500, 500
        self.image = pygame.Surface((self.width, self.height))
        self.rect = self.image.get_rect()
        # creating grid (game cells)
        self.rows = 25
        self.cols = 25
        self.grid = [[Cell(self.image, x, y) for x in range(self.cols)]
                     for y in range(self.rows)]  # from cell class

    def update(self):
        self.rect.topleft = self.pos
        for row in self.grid:
            for cell in row:
                cell.update()  # updates cells when game window is updated

    def draw(self):
        self.image.fill((174, 182, 191))
        for row in self.grid:
            for cell in row:
                cell.draw()
        self.screen.blit(self.image, (self.pos.x, self.pos.y))
