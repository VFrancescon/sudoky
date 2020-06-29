import pygame
import os

number1 = pygame.image.load(os.path.join('res', '1.png'))
number2 = pygame.image.load(os.path.join('res', '2.png'))
number3 = pygame.image.load(os.path.join('res', '3.png'))
number4 = pygame.image.load(os.path.join('res', '4.png'))
number5 = pygame.image.load(os.path.join('res', '5.png'))
number6 = pygame.image.load(os.path.join('res', '6.png'))
number7 = pygame.image.load(os.path.join('res', '7.png'))
number8 = pygame.image.load(os.path.join('res', '8.png'))
number9 = pygame.image.load(os.path.join('res', '9.png'))

class Grid:
    def __init__(self):
        self.grid_lines = [((0,60), (540,60)), #1st h line
                           ((0,120), (540,120)), #2nd h line
                           ((0,180), (540,180)), #3rd h line
                           ((0,240), (540,240)),  #4th h line
                           ((0,300), (540,300)),  #5th h line
                           ((0,360), (540,360)),  #6th h line
                           ((0,420), (540,420)),  #7th h line
                           ((0,480), (540,480)),  #8th h line
                           ((0,540), (540,540)),  #9th h line
                           #((0,600), (600,600)),  #10th h line
        
                           ((60,0), (60,540)),   #1st v line
                           ((120,0), (120,540)),  #2nd v line
                           ((180,0), (180,540)), #3rd v line
                           ((240,0), (240,540)), #4th v line
                           ((300,0), (300,540)),  #5th v line
                           ((360,0), (360,540)), #6th v line
                           ((420,0), (420,540)), #7th v line
                           ((480,0), (480,540)),  #8th v line
                           ((540,0), (540,540))] #9th v line
                           #((600,0), (600,600)) #10th v line
        self.grid = [[0 for x in range(9)] for y in range(9)]
        self.switch_player = True

        # self.grid.lines = []
        # for i in range(11):
        #     self.grid.lines.append(tuple((0, 60+60*i), (600, 60+60*i)))    
        #     self.grid.lines.append(tuple((60+60*i, 0), (60+60*i, 600)))

    def draw(self, surface):
        for line in self.grid_lines:
            if line [0][1] % 180 == 0 and line[0][0] == 0:
                pygame.draw.line(surface, (0,0,0), line[0], line[1], 3)

            elif line[0][0] % 180 == 0 and line[0][1] == 0:
                pygame.draw.line(surface, (0,0,0), line[0], line[1], 3)

            else:
                pygame.draw.line(surface, (0,0,0), line[0], line[1], 1)
        
        for y in range(9):
            for x in range(9):
                if self.get_cell_value(x, y) == "X":
                    surface.blit(number1, (x*60, y*60))
                elif self.get_cell_value(x, y) == "O":
                    surface.blit(number2, (x*60, y*60))

    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x] = value

    def get_mouse(self, x, y, player):
        if self.get_cell_value(x, y,) == 0:
            self.switch_player = True
            if player == 'X':
                self.set_cell_value(x, y, 'X')
            elif player == "O":
                self.set_cell_value(x, y, 'O')
        else: 
            self.switch_player = False

    def print_grid(self):
        for row in self.grid:
            print(row)
