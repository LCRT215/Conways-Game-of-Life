import pygame
import sys
from game_window_class import *
WIDTH, HEIGHT = 800, 800
BACKGROUND = (33, 47, 60)

#initial game setup
def get_events():
    global running
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


def update():
    game_window.update()


def draw():
    window.fill(BACKGROUND)
    game_window.draw()


pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_window = Game_window(window, 150, 180)

running = True
while running:
    get_events()
    update()
    draw()
    pygame.display.update()
    clock.tick()

pygame.quit()
sys.exit()
