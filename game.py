import pygame
from grid import Grid
import os
pygame.init()
pygame.font.init()
WIDTH = 540
LENGTH = 540
os.environ['SDL_VIDEO_WINDOW_POS'] = '400,100'
# font = pygame.font.Font('Helvetica 400.ttf ', 10) 

surface = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Sudoky")

grid = Grid()

running = True
l_click = False
r_click = False
x_counter = 0
y_counter = 0

surface.fill((255,255,255))

while running:
    #grid.draw(surface)
    grid.draw(surface)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
                if pygame.mouse.get_pressed()[0] == True: l_click = True
                if pygame.mouse.get_pressed()[2] == True: r_click = True
                if grid.get_cell_value(pos[0] // 60, pos[1] // 60) == 0:
                    grid.red_box(pos[0] // 60, pos[1] // 60, surface)
            if pygame.mouse.get_pressed()[1]:
                grid.clear_box(pos[0] // 60, pos[1] // 60, surface)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                inputk = 1
            if event.key == pygame.K_KP2 or event.key == pygame.K_2:
                inputk = 2
            if event.key == pygame.K_KP3 or event.key == pygame.K_3:
                inputk = 3
            if event.key == pygame.K_KP4 or event.key == pygame.K_4:
                inputk = 4
            if event.key == pygame.K_KP5 or event.key == pygame.K_5:
                inputk = 5
            if event.key == pygame.K_KP6 or event.key == pygame.K_6:
                inputk = 6
            if event.key == pygame.K_KP7 or event.key == pygame.K_7:
                inputk = 7
            if event.key == pygame.K_KP8 or event.key == pygame.K_8:
                inputk = 8
            if event.key == pygame.K_KP9 or event.key == pygame.K_9:
                inputk = 9
            if event.key == pygame.K_r:
                inputk = 'r'
            if event.key == pygame.K_c:
                inputk = 'c'
            if event.key == pygame.K_b:
                inputk = 'b'

            if isinstance(inputk, str):
                if inputk == 'r':
                    grid.get_row(pos[1] // 60)
                if inputk == 'c':
                    grid.get_col(pos[0] // 60)
                if inputk == 'b':
                    grid.get_box(pos[0] // 60, pos[1] // 60)                    

            if isinstance(inputk, int):
                if l_click == True:
                    if grid.get_cell_value(pos[0] // 60, pos[1] // 60) == 0:
                        grid.set_cell_value(pos[0] // 60, pos[1] // 60, inputk)
                        grid.print_value(surface, pos[0] // 60, pos[1] // 60)
                    l_click = False
                    r_click = False

                if r_click == True:
                    grid.print_comment(surface, pos[0] // 60, pos[1] // 60, inputk)
                    l_click = False
                    r_click = False
        


            #grid.print_grid()

