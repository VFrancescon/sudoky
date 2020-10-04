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

grid.pre_print_grid(surface)

while running:
    grid.draw(surface)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            lclick = pos[0] // 60
            rclick = pos[1] // 60
            if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
                if pygame.mouse.get_pressed()[0] == True: l_click = True
                if pygame.mouse.get_pressed()[2] == True: r_click = True
                if grid.get_cell_value(lclick, rclick) == 0:
                    grid.red_box(lclick, rclick, surface)
            if pygame.mouse.get_pressed()[1]:
                grid.clear_box(lclick, rclick, surface)


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1 or event.key == pygame.K_1:
                inputk = 1
            elif event.key == pygame.K_KP2 or event.key == pygame.K_2:
                inputk = 2
            elif event.key == pygame.K_KP3 or event.key == pygame.K_3:
                inputk = 3
            elif event.key == pygame.K_KP4 or event.key == pygame.K_4:
                inputk = 4
            elif event.key == pygame.K_KP5 or event.key == pygame.K_5:
                inputk = 5
            elif event.key == pygame.K_KP6 or event.key == pygame.K_6:
                inputk = 6
            elif event.key == pygame.K_KP7 or event.key == pygame.K_7:
                inputk = 7
            elif event.key == pygame.K_KP8 or event.key == pygame.K_8:
                inputk = 8
            elif event.key == pygame.K_KP9 or event.key == pygame.K_9:
                inputk = 9
            elif event.key == pygame.K_r:
                inputk = 'r'
            elif event.key == pygame.K_c:
                inputk = 'c'
            elif event.key == pygame.K_a:
                inputk = 'a'
            elif event.key == pygame.K_b:
                inputk = 'b'
            elif event.key == pygame.K_n:
                inputk = 'n'
            elif event.key == pygame.K_g:
                inputk = 'g'
            elif event.key == pygame.K_s:
                inputk = 's'
            elif event.key == pygame.K_l:
                inputk = 'l'

            if isinstance(inputk, str):
                if inputk == 'r':
                    grid.solver(surface)
                elif inputk == 'c':
                    print(grid.get_comments(lclick,rclick))
                elif inputk == 'b':
                    grid.n_triplet_b(lclick, rclick, surface)
                elif inputk == 'n':
                    grid.ppair_h(lclick, rclick, surface)
                elif inputk == 'g':
                    grid.n_triplet_h(lclick, rclick, surface)
                elif inputk == 'a':
                    grid.ppair_v(lclick, rclick, surface)
                elif inputk == 's':
                    grid.generate_candidates(surface)
                elif inputk == 'l':
                    grid.dc_checker(lclick, rclick, surface)                     

            if isinstance(inputk, int):
                if l_click == True:
                    if grid.get_cell_value(lclick, rclick) == 0:
                        grid.print_value(surface, lclick, rclick, inputk)
                    l_click = False
                    r_click = False

                elif r_click == True:
                    grid.print_comment(surface, lclick, rclick, inputk)
                    l_click = False
                    r_click = False
        



