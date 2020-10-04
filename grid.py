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
        
        self.grid = [[5,0,9,0,0,0,0,0,0], #dc grid, dev purposes
                     [0,7,0,0,0,6,0,0,1],
                     [6,0,0,0,9,0,0,0,4],
                     [0,0,0,0,0,9,0,5,0],
                     [0,4,0,0,0,3,0,8,0],
                     [0,5,8,0,7,0,0,2,0],
                     [0,6,0,2,0,0,0,4,0],
                     [0,8,0,0,0,7,0,0,3],
                     [0,0,0,0,0,0,0,0,0]]

        self.complete = [1,2,3,4,5,6,7,8,9]
        self.empty = [0,0,0,0,0,0,0,0,0]
        self.permanent = [[0 for x in range(9)] for y in range(9)]
        self.availables = 0
        self.col = []
        self.box = []
        self.comments = [[[0 for x in range(9)] for y in range(9)] for z in range(9)]
        self.x_offset = 0
        self.y_offset = 0
        self.x_cor = 0
        self.y_cor = 0
        self.counter = [[[0 for x in range(9)] for y in range(9)] for z in range(9)]

    def draw(self, surface):
        for line in self.grid_lines:
            if line [0][1] % 180 == 0 and line[0][0] == 0:
                pygame.draw.line(surface, BLACK, line[0], line[1], 3)

            elif line[0][0] % 180 == 0 and line[0][1] == 0:
                pygame.draw.line(surface, BLACK, line[0], line[1], 3)

            else:
                pygame.draw.line(surface, BLACK, line[0], line[1], 1)

    def get_cell_value(self, x, y):
        # for k in self.comments[x][y]:
        #     self.print_comment(surface, x, y, self.comments[x][y][k])lue(self, x, y):
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
        return self.comments[x][y]

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
        white_box = pygame.Rect(x*60 + 1, y*60 + 1, 59, 59)
        if self.get_cell_value(x,y) == 0:
            pygame.draw.rect(surface, WHITE, white_box, 0)
            self.set_cell_value(x,y,0)

    def print_grid(self):
        print("---------------------------")
        for row in self.grid:
            print(row)

    def print_value(self, surface, x, y, key):
        bx = x // 3
        by = y // 3
        font = pygame.font.SysFont('helvetica', 70, bold=0, italic=0, constructor=None)
        number = str(key)
        text = font.render(number, 1, BLUE)
        textpos = [x*60 +11,y*60]
        self.clear_box(x, y, surface)
        surface.blit(text, textpos)
        self.set_cell_value(x, y, key)

        for i in range(9):
            for j in range(9):
                if self.get_cell_value(j,y) == 0:
                    if j == x:
                        continue
                    else:  
                        if key in self.comments[j][y]:
                            self.comments[j][y].remove(key)
                            self.quick_cprint(j,y,surface)
            if self.get_cell_value(x,i) == 0:
                if i == y:
                    continue
                else:
                    if key in self.comments[x][i]:
                        self.comments[x][i].remove(key)
                        self.quick_cprint(x,i,surface)
    

        for i in range(3):
            for j in range(3):
                if self.get_cell_value(j+bx*3, i +by*3) == 0:
                    if key in self.comments[j+bx*3][i +by*3]:
                        self.comments[j+bx*3][i +by*3].remove(key)
                        self.quick_cprint(j+bx*3, i +by*3, surface)

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
            self.comments[x][y] = list( set(self.comments[x][y]) - set(self.empty) ) 
            if key == 0:
                return
                
            if key == 1:
                self.x_offset = 0
                self.y_offset = 0
                if key not in self.comments[x][y]:
                    self.comments[x][y].append(key)
            elif key == 2:
                self.x_offset = 20
                self.y_offset = 0
                if key not in self.comments[x][y]:
                    self.comments[x][y].append(key)
            elif key == 3:
                self.x_offset = 40
                self.y_offset = 0
                if key not in self.comments[x][y]:
                    self.comments[x][y].append(key)
            elif key == 4:
                self.x_offset = 0
                self.y_offset = 20
                if key not in self.comments[x][y]:
                    self.comments[x][y].append(key)
            elif key == 5:
                self.x_offset = 20
                self.y_offset = 20
                if key not in self.comments[x][y]:
                    self.comments[x][y].append(key)
            elif key == 6:
                self.x_offset = 40
                self.y_offset = 20
                if key not in self.comments[x][y]:
                    self.comments[x][y].append(key)
            elif key == 7:
                self.x_offset = 0
                self.y_offset = 40
                if key not in self.comments[x][y]:
                    self.comments[x][y].append(key)
            elif key == 8:
                self.x_offset = 20
                self.y_offset = 40
                if key not in self.comments[x][y]:
                    self.comments[x][y].append(key)
            elif key == 9:
                self.x_offset = 40
                self.y_offset = 40
                if key not in self.comments[x][y]:
                    self.comments[x][y].append(key)

            text = font.render(number, 1, GREY)
            textpos = [x*60 + 5 + self.x_offset,y*60+2 + self.y_offset]
            surface.blit(text, textpos)

    def single(self, x, y, surface):
        self.comments[x][y] = list( set(self.comments[x][y]) - set(self.empty) )
        if len(self.comments[x][y]) == 1:
            self.print_value(surface,x,y,self.comments[x][y][0])
    
    def comment_counter_b(self, x, y):
        bx = x // 3 
        by = y // 3
        self.counter_b = [[[0 for x in range(9)] for y in range(9)] for z in range(9)]
        for k in range(9):
            for i in range(3):
                for j in range(3):
                    if self.get_cell_value(j+bx*3, i+by*3) == 0:
                        if k+1 in self.comments[j+bx*3][i+by*3]:
                            self.counter_b[bx][by][k] += 1

    def comment_counter_h(self, y):
        self.counter_h = [[0 for x in range(9)] for y in range(9)]
        for k in range(9):
            for i in range(9):
                if self.get_cell_value(i, y) == 0:
                    if k+1 in self.comments[i][y]:
                        self.counter_h[y][k] += 1

    def comment_counter_v(self, x):
        self.counter_v = [[0 for x in range(9)] for y in range(9)]
        for k in range(9):
            for i in range(9):
                if self.get_cell_value(x, i) == 0:
                    if k+1 in self.comments[x][i]:
                        self.counter_v[x][k] += 1

    def single_naked(self,x,y, surface):
        bx = x // 3 
        by = y // 3
        self.comment_counter_b(x,y)
        for k in range(9):
            if self.counter[bx][by][k] == 1:
                for q in range(3):
                    for w in range(3):
                        if self.get_cell_value(w+bx*3, q+by*3) == 0:
                            if k+1 in self.comments[w+bx*3][q+by*3]:
                                x1 = w+bx*3
                                y1 = q+by*3
                self.print_value(surface, x1, y1, k+1)

    def solver(self, surface):
        for i in range(9):
            for j in range(9):
                if self.get_cell_value(j, i) == 0:
                    # self.single_naked(j,i,surface)
                    self.single(j,i,surface)
                    # self.dc_checker(j,i,surface)
                    self.single_hidden_b(j, i, surface)
                    self.single_hidden_h(i, surface)
                    self.single_hidden_v(j, surface)
                    self.dc_checker(j,i,surface)
                    self.ppair_h(j,i, surface)
                    self.ppair_v(j,i, surface)
                    self.n_triplet_b(j,i,surface)
                    self.n_triplet_h(j,i,surface)

    def generate_candidates(self, surface):
        self.clear_board(surface)
        for i in range(9):
            for j in range(9):
                availables = list(set(self.complete) - set(self.get_row(i)) - set(self.get_col(j)) - set(self.get_box(j,i)))
                if self.get_cell_value(j,i) == 0:
                    for k in range(len(availables)):
                        self.print_comment(surface, j, i, availables[k])

    def quick_cprint(self,x, y, surface):
        self.clear_box(x, y, surface)
        for i in self.comments[x][y]:
            self.print_comment(surface, x, y, i )

    def dc_checker(self, x, y, surface):
        bx = x // 3 
        by = y // 3
        for i in range(3):
            for j in range(3):
                if self.get_cell_value(j+bx*3, i+by*3) == 0:
                    if len(self.comments[x][y]) == 2:
                        if x != i+bx*3 or y != j+by*3:
                            if self.comments[x][y] == self.comments[i+bx*3][j+by*3]:
                                if x == i+bx*3:
                                    for k in range(9):
                                        if k == y or k == j+by*3:
                                            continue
                                        else:
                                            for q in self.comments[x][y]:
                                                if q in self.comments[x][k]:
                                                    self.comments[x][k].remove( q )
                                                    self.quick_cprint(x, k, surface)
                                if y == j+by*3:
                                    for k in range(9):
                                        if k == x or k == i+bx*3:
                                            continue
                                        else:
                                            for q in self.comments[x][y]:
                                                if q in self.comments[k][y]:
                                                    self.comments[k][y].remove( q )
                                                    self.quick_cprint(k, y, surface)

    def single_hidden_b(self, x, y, surface):
        bx = x // 3
        by = y // 3
        self.comment_counter_b(x,y)
        for k in range(9):
            if self.counter_b[bx][by][k] == 1:
                for q in range(3):
                    for w in range(3):
                        if self.get_cell_value(w+bx*3, q+by*3) == 0:
                            if k+1 in self.comments[w+bx*3][q+by*3]:
                                self.print_value(surface, w+bx*3, q+by*3, k+1)
            
        
    def single_hidden_h(self, y, surface):
        self.comment_counter_h(y)
        for k in range(9):
            for i in range(9):
                if self.get_cell_value(i,y) == 0:
                    if k+1 in self.comments[i][y]:
                        if self.counter_h[y][k] == 1:
                            self.print_value(surface, i, y, k+1)

    def single_hidden_v(self, x, surface):
        self.comment_counter_v(x)
        for k in range(9):
            for i in range(9):
                if self.get_cell_value(x,i) == 0:
                    if k+1 in self.comments[x][i]:
                        if self.counter_v[x][k] == 1:
                            self.print_value(surface, x, i, k+1)

    def ppair_v(self, x,y, surface):
        self.comment_counter_v(x)
        self.comment_counter_b(x,y)      
        
        bx = x // 3
        by = y // 3
        for k in range(9):
            y1 = []
            if self.counter_v[x][k] == 2:
                for i in range(9):
                    if self.get_cell_value(x,i) == 0:
                        if k+1 in self.comments[x][i]:
                            y1.append(i)
                for j in range(9):
                    if len(y1) == 2:
                        if self.get_cell_value(x,j) == 0:
                            if y1[0] == j or y1[1] == j:
                                continue
                            else: 
                                if k+1 in self.comments[x][j]:
                                    self.comments[x][j].remove(k+1)
                                    self.quick_cprint(x,j,surface)

                for q in range(3):
                    for w in range(3):
                        if self.get_cell_value(w+bx*3, q+by*3) == 0:
                            if (w+bx*3 == x and q+by*3 == y1[0]) or (w+bx*3 == x and q+by*3 == y1[1]): 
                                continue
                            else:
                                if y1[0] // 3 == y1[1] // 3:
                                    if k+1 in self.comments[w+bx*3][q+by*3]:
                                        print("Column statement, Removing", k+1, "from", w+bx*3, q+by*3)
                                        self.comments[w+bx*3][q+by*3].remove(k+1)
                                        self.quick_cprint(w+bx*3, q+by*3, surface)

            elif self.counter_b[bx][by][k] == 2:
                for i in range(3):
                    if self.get_cell_value(x,by*3+i) == 0:
                        if k+1 in self.comments[x][by*3+i]:
                            y1.append(by*3+i)
                for j in range(9):
                    if self.get_cell_value(x, j) == 0:
                        if len(y1) == 2:
                            if j == y1[0] or j == y1[1]:
                                continue
                            else:
                                if k+1 in self.comments[x][j]:
                                    print("Removing", k+1, "from", x,j)
                                    self.comments[x][j].remove(k+1)
                                    self.quick_cprint(x, j, surface)

    def ppair_h(self, x,y, surface):
        self.comment_counter_h(y)
        self.comment_counter_b(x,y)      
        
        bx = x // 3
        by = y // 3
        for k in range(9):
            x1 = []
            if self.counter_h[y][k] == 2:
                for i in range(9):
                    if self.get_cell_value(i,y) == 0:
                        if k+1 in self.comments[i][y]:
                            x1.append(i)
                for j in range(9):
                    if len(x1) == 2:
                        if self.get_cell_value(j,y) == 0:
                            if x1[0] == j or x1[1] == j:
                                continue
                            else: 
                                if k+1 in self.comments[j][y]:
                                    self.comments[j][y].remove(k+1)
                                    self.quick_cprint(j,y,surface)

                for q in range(3):
                    for w in range(3):
                        if self.get_cell_value(w+bx*3, q+by*3) == 0:
                            if (w+bx*3 == x1[0] and q+by*3 == y) or (w+bx*3 == x1[1] and q+by*3 == y): 
                                continue
                            else:
                                if x1[0] // 3 == x1[1] // 3:
                                    if k+1 in self.comments[w+bx*3][q+by*3]:
                                        print("Removing", k+1, "from", w+bx*3, q+by*3)
                                        self.comments[w+bx*3][q+by*3].remove(k+1)
                                        self.quick_cprint(w+bx*3, q+by*3, surface)

            elif self.counter_b[bx][by][k] == 2:
                print("two in a box", k+1)
                for i in range(3):
                    if self.get_cell_value(bx*3+i,y) == 0:
                        if k+1 in self.comments[bx*3+i][y]:
                            x1.append(bx*3+i)
                print(x1)
                for j in range(9):
                    if self.get_cell_value(j, y) == 0:
                        if len(x1) == 2:
                            if j == x1[0] or j == x1[1]:
                                continue
                            else:
                                if k+1 in self.comments[j][y]:
                                    print("Removing", k+1, "from", j,y)
                                    self.comments[j][y].remove(k+1)
                                    self.quick_cprint(j, y, surface)
                        
    def n_triplet_b(self, x, y, surface):
        bx = x // 3
        by = y // 3
        if len(self.comments[x][y]) == 3:
            x1 = []
            y1 = []
            for i in range(3):
                for j in range(3):
                    if self.get_cell_value(j+bx*3, i+by*3) == 0:
                        if len(self.comments[j+bx*3][i+by*3]) == 2:
                            x1.append(j+bx*3)
                            y1.append(i+by*3)
            
            if len(x1) == len(y1) == 2:
               if list( set(self.comments[x][y]) - set(self.comments[x1[0]][y1[0]]) - set(self.comments[x1[1]][y1[1]]) ) == []:
                    for i in range(3):
                        for j in range(3):
                            if self.get_cell_value(j+bx*3, i+by*3) == 0:
                                if j+bx*3 in x1 and i+by*3 in y1 or j+bx*3 == x and i+by*3 == y:
                                    continue
                                else:
                                    self.comments[j+bx*3][i+by*3] = list( set(self.comments[j+bx*3][i+by*3]) - set(self.comments[x][y]) )
                                    self.quick_cprint(j+bx*3, i+by*3, surface)

    def n_triplet_h(self,x, y, surface): #not working idk why
        if len(self.comments[x][y]) == 3:
            x1 = []
            for i in range(9):
                    if self.get_cell_value(i, y) == 0:
                        if len(self.comments[i][y]) == 2:
                            x1.append(i)

            if len(x1) == 2:
                if list( set(self.comments[x][y]) - set(self.comments[x1[0]][y]) - set(self.comments[x1[1]][y]) ) == []:
                    for i in range(9):
                            if self.get_cell_value(i, y) == 0:
                                if i in x1 or i == x:
                                    continue
                                else:
                                    print("Removing", self.comments[x][y], "from", i,y)
                                    self.comments[i][y] = list( set(self.comments[i][y]) - set(self.comments[x][y]) )
                                    self.quick_cprint(i,y, surface)

    def clear_board(self, surface):
        for i in range(9):
            for j in range(9):
                if self.get_cell_value(j, i) == 0:
                    self.clear_box(j,i, surface)
