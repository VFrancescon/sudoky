import pygame
import os
pygame.init()
pygame.font.init()

RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (14,77,146)
GREY = (128,128,128)
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
        #self.grid = [[0 for x in range(9)] for y in range(9)] #empty initialisation, debug purposes
        
        self.grid = [[5,0,0,0,0,0,8,0,0],
                     [6,9,0,3,0,0,0,0,7],
                     [0,0,0,0,5,0,0,0,3],
                     [4,0,9,0,0,0,3,0,0],
                     [0,0,0,0,3,6,0,0,5],
                     [7,0,0,0,0,0,9,0,0],
                     [0,0,0,1,4,0,0,0,8],
                     [1,5,0,6,7,0,0,0,9],
                     [3,0,0,0,0,8,6,5,0]]

        self.complete = [1,2,3,4,5,6,7,8,9]
        self.permanent = [[0 for x in range(9)] for y in range(9)]
        self.availables = 0
        self.col = []
        #self.width = WIDTH // 9
        #self.height = HEIGHT // 9 both currently unused
        self.box = []
        self.comments = [[[0 for x in range(9)] for y in range(9)] for z in range(9)]
        self.comm_tracker = []
        self.x_offset = 0
        self.y_offset = 0
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
        return self.grid[y]

    def get_col(self, x):
        self.col = []
        for y in range(9):
            self.col.append(self.grid[y][x])
        return self.col
        
    def get_box(self, x, y):
        self.box = []
        box_x = x // 3
        box_y = y // 3
        for x in range(3):
            for y in range(3):
                self.box.append(self.get_cell_value(y + box_x*3,x + box_y*3))
        return self.box

    def get_comments(self, x, y):
        print(self.comments[x][y])
        return self.comments[x][y]

    # def set_comments(self, x, y):
    #     self.comments = list()

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
        curr_cell = self.permanent[y][x]
        white_box = pygame.Rect(x*60 + 1, y*60 + 1, 59, 59)
        if self.get_cell_value(x,y) != 0 and curr_cell == True:
            print("Cannot clear a pre-filled box")            
        else: 
            pygame.draw.rect(surface, WHITE, white_box, 0)
            self.set_cell_value(x,y,0)
            self.comm_tracker = []

    def print_grid(self):
        print("---------------------------")
        for row in self.grid:
            print(row)

    def print_value(self, surface, x, y, key):
        font = pygame.font.SysFont('helvetica', 70, bold=0, italic=0, constructor=None)
        number = str(key)
        text = font.render(number, 1, BLUE)
        textpos = [x*60 +11,y*60]
        self.clear_box(x, y, surface)
        surface.blit(text, textpos)
        self.set_cell_value(x, y, key)
    
    def pre_print_grid(self,surface):
        font = pygame.font.SysFont('helvetica', 70, bold=0, italic=0, constructor=None)
        for i in range(9):
            for j in range(9):
                if self.get_cell_value(i,j) != 0:
                    number = str(self.get_cell_value(i,j))
                    text = font.render(number, 1, BLACK)
                    textpos = [i*60 +11,j*60]
                    surface.blit(text, textpos)
                    self.permanent[j][i] = True
                else:
                    self.permanent[j][i] = False

    def print_comment(self, surface, x, y, key): #need to find a way to store counters for each box used
        font = pygame.font.SysFont('helvetica', 20, bold=0, italic=0, constructor=None)
        number = str(key)
        if self.get_cell_value(x,y) == 0:
            if self.x_cor != x or self.y_cor != y:
                self.comm_tracker = []

            if key in self.comm_tracker:
                print("Key already entered, try again")
            elif key == 0:
                print("Not printing a zero")
            else:
                self.comm_tracker.append(key)
                
                if key == 1:
                    self.x_offset = 0
                    self.y_offset = 0
                    self.comments[x][y][0] = key
                elif key == 2:
                    self.x_offset = 20
                    self.y_offset = 0
                    self.comments[x][y][1] = key
                elif key == 3:
                    self.x_offset = 40
                    self.y_offset = 0
                    self.comments[x][y][2] = key
                elif key == 4:
                    self.x_offset = 0
                    self.y_offset = 20
                    self.comments[x][y][3] = key
                elif key == 5:
                    self.x_offset = 20
                    self.y_offset = 20
                    self.comments[x][y][4] = key
                elif key == 6:
                    self.x_offset = 40
                    self.y_offset = 20
                    self.comments[x][y][5] = key
                elif key == 7:
                    self.x_offset = 0
                    self.y_offset = 40
                    self.comments[x][y][6] = key
                elif key == 8:
                    self.x_offset = 20
                    self.y_offset = 40
                    self.comments[x][y][7] = key
                elif key == 9:
                    self.x_offset = 40
                    self.y_offset = 40
                    self.comments[x][y][8] = key

                text = font.render(number, 1, GREY)
                textpos = [x*60 + 5 + self.x_offset,y*60+2 + self.y_offset]
                surface.blit(text, textpos)

            self.x_cor = x
            self.y_cor = y

    def get_availables(self, x, y):
        self.availables = list(set(self.complete) - set(self.get_row(y)) - set(self.get_col(x)) - set(self.get_box(x,y)))
        return self.availables

    def naked_single(self, x, y, surface):
        if len(self.get_availables(x,y)) == 1:
            value = self.get_availables(x,y)[0]
            self.print_value(surface, x, y, value)
    
    def naked_double(self, x, y, surface):
        if len(self.get_availables(x,y)) == 2:
            v = list(set(self.get_availables(x,y)) - set(self.get_col(x)))
            h = list(set(self.get_availables(x,y)) - set(self.get_row(y)))
            if len(v) == 1:
                self.print_value(surface, x, y, v[0])
            elif len(h) == 1:
                self.print_value(surface, x, y, v[0])

    def solver(self, surface):
        for i in range(9):
            for j in range(9):
                if self.get_cell_value(j, i) == 0:
                    self.naked_single(j, i, surface)

    def generate_candidates(self, surface):
        self.clear_board(surface)
        for i in range(9):
            for j in range(9):
                availables = list(set(self.complete) - set(self.get_row(i)) - set(self.get_col(j)) - set(self.get_box(j,i)))
                if self.get_cell_value(j,i) == 0:
                    for k in range(len(availables)):
                        self.print_comment(surface, j, i, availables[k])

    # def double_comments(self, x, y, surface):
    #     if (y % 3 == 0) and (x % 3 == 0): #00
    
    #         if self.get_comments(x,y) == self.get_comments(x+1,y):
    #             for k in range(9):
    #                 if self.get_cell_value(k,y) == 0:
    #                     if k == x or k == x+1:
    #                         print("No touchy at ", k, y)
    #                     else:
    #                         print("Subtracting ", self.comments[k][y], "and", self.comments[x][y])
    #                         self.comments[k][y] = list(set(self.comments[k][y]) - set(self.comments[x][y]))
    #                         print(self.comments[k][y])
    #                         for i in len(self.comments[x][y]):
    #                             self.clear_box(x,y,surface)
    #                             self.print_comment(surface, x, y, self.comments[x][y][i])

    def dc_checker(self, x, y):
        bx = x // 3 
        by = y // 3
        print(bx,by)
        for i in range(3):
            for j in range(3):
                if self.get_cell_value(x, y) == 0:
                    if x != j+bx*3 and y != j+by*3:                    
                        if self.comments[x][y] == self.comments[j+bx*3][i+by*3]:
                            
                            
                            if x == j+bx*3+1:
                                if (j+bx*3+1) // 3 == bx:
                                    print("Okay +1x statement", x,y, "and", j+bx*3+1, )
                            elif x == j+bx*3-1:
                                if (j+bx*3-1) // 3 == bx:
                                    print("Okay, dealing with these xs", x, "and", j+bx*3-1)
                            elif y == i+by*3+1:
                                if (i+by*3+1) // 3 == by:
                                    print("Okay, dealing with these ys", y, "and", i+by*3+1)
                            elif y == i+by*3-1:
                                if (i+by*3-1) // 3 == by:
                                    print("Okay, dealing with these ys", y, "and", i+by*3-1)
                 

    def clear_board(self, surface):
        for i in range(9):
            for j in range(9):
                if self.get_cell_value(j, i) == 0:
                    self.clear_box(j,i, surface)
