import pygame
from grid import Grid
import os

WIDTH = 540
LENGTH = 540
os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'

surface = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Sudoky")

grid = Grid()

running = True
player = "X"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                # print(pos[0] // 60, pos[1] // 60)
                grid.get_mouse(pos[0] // 60, pos[1] // 60, player)
                if player == "X":
                    player = "O"
                else: player = 'X'

                grid.print_grid()

    surface.fill((255,255,255))

    grid.draw(surface)
    pygame.display.flip()