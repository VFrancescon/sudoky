import pygame
import os
pygame.init()
pygame.font.init()

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH = 540
HEIGHT = 540

class Grid:
    def __init__(self):
        self.grid_lines = [((0,60), (540,60)),    #1st h line
                           ((0,120), (540,120)),  #2nd h line
                           ((0,180), (540,180)),  #3rd h line
                           ((0,240), (540,240)),  #4th h line
                           ((0,300), (540,300)),  #5th h line
                           ((0,360), (540,360)),  #6th h line
                           ((0,420), (540,420)),  #7th h line
                           ((0,480), (540,480)),  #8th h line
                           ((0,540), (540,540)),  #9th h line

                           ((60,0), (60,540)),    #1st v line
                           ((120,0), (120,540)),  #2nd v line
                           ((180,0), (180,540)),  #3rd v line
                           ((240,0), (240,540)),  #4th v line
                           ((300,0), (300,540)),  #5th v line
                           ((360,0), (360,540)),  #6th v line
                           ((420,0), (420,540)),  #7th v line
                           ((480,0), (480,540)),  #8th v line
                           ((540,0), (540,540))]  #9th v line
        self.erase = False
        self.grid = [[0 for x in range(9)] for y in range(9)]
        self.col = []
        self.width = WIDTH // 9
        self.height = HEIGHT // 9
        self.box = []
        self.comments = []
        self.x_counter = 0
        self.y_counter = 0
        self.x_cor = 0
        self.y_cor = 0

    def draw(self, surface):
        for line in self.grid_lines:
            if line [0][1] % 180 == 0 and line[0][0] == 0:
                pygame.draw.line(surface, BLACK, line[0], line[1], 3)

            elif line[0][0] % 180 == 0 and line[0][1] == 0:
                pygame.draw.line(surface, BLACK, line[0], line[1], 3)

            else:
                pygame.draw.line(surface, BLACK, line[0], line[1], 1)

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value
    
    def get_row(self, y):
        print(self.grid[y])
        return self.grid[y]

    def get_col(self, x):
        self.col = []
        for y in range(9):
            self.col.append(self.grid[y][x])
        print(self.col)
        return self.col
        
    def get_box(self, x, y):
        self.box = []
        box_x = x // 3
        box_y = y // 3
        for x in range(3):
            for y in range(3):
                self.box.append(self.get_cell_value(y + box_x*3,x + box_y*3))
        print(self.box)
        return self.box

    def box_draw(self, surface):
        for i in range(len(self.box)):
            pygame.draw.rect(surface, BLACK, self.box[i], 1)

    def red_box(self, x, y, surface):
        if self.erase == False:
            self.tempx = x
            self.tempy = y
            if self.get_cell_value(x,y) == 0: 
                reddy = pygame.Rect(x*60 + 1, y*60 + 1, 58, 58)
                pygame.draw.rect(surface, RED, reddy, 2)
                self.erase = True
        else:
            if self.get_cell_value(x,y) == 0:
                erase_box = pygame.Rect(self.tempx*60 + 1, self.tempy*60 + 1, 58, 58)
                pygame.draw.rect(surface, WHITE, erase_box, 2)

                reddy = pygame.Rect(x*60 + 1, y*60 + 1, 58, 58)
                pygame.draw.rect(surface, RED, reddy, 2)
                self.tempx = x
                self.tempy = y
                self.erase = True

    def clear_box(self, x, y, surface):
        if self.get_cell_value(x,y) == 0:
            white_box = pygame.Rect(x*60 + 1, y*60 + 1, 59, 59)
            pygame.draw.rect(surface, WHITE, white_box, 0)
        else: print("Cannot clear a filled box")

    def print_grid(self):
        print("---------------------------")
        for row in self.grid:
            print(row)

    def print_value(self, surface, x, y):
        font = pygame.font.SysFont('helvetica', 70, bold=0, italic=0, constructor=None)
        number = str(self.get_cell_value(x,y))
        text = font.render(number, 1, BLACK)
        textpos = [x*60 +11,y*60]
        surface.blit(text, textpos)

    def print_comment(self, surface, x, y, key): #need to find a way to store counters for each box used
        font = pygame.font.SysFont('helvetica', 15, bold=0, italic=0, constructor=None)
        number = str(key)
        if self.x_cor != x or self.y_cor != y:
            self.comments = []
            self.x_counter = 0
            self.y_counter = 0

        if key in self.comments:
            print("Already inputted")
        else:
            text = font.render(number, 1, BLACK)
            textpos = [x*60 + 5 + self.x_counter,y*60+2 + self.y_counter]
            surface.blit(text, textpos)
        self.comments.append(key)

        self.x_counter += 15
        if self.x_counter == 60: 
            self.x_counter = 0
            self.y_counter += 15

        self.x_cor = x
        self.y_cor = y