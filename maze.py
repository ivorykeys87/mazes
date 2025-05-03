from cell import Cell
from graphics import Point, Window
import time
import random

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed = None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self._create_cells()
        self.break_entrance_and_exit()
        self.break_walls_r(0,0)
        self.reset_cells_visited()

    def _create_cells(self):
        cx1 = self.x1
        cy1 = self.y1
        cx2 = self.x1 + self.cell_size_x
        cy2 = self.y1 + self.cell_size_y
        for c in range(self.num_cols):
            row = []
            for r in range(self.num_rows):
                cell = Cell(p1=Point(cx1,cy1), p2 = Point(cx2,cy2), window=self.win)
                row.append(cell)
                if self.win != None:
                    cell.draw()
                    self.animate()
                cy1 += self.cell_size_y
                cy2 += self.cell_size_y
            self.cells.append(row)
            cx1 += self.cell_size_x
            cy1 = self.y1
            cx2 += self.cell_size_x
            cy2 = self.y1 + self.cell_size_y
        self.break_entrance_and_exit()

    def animate(self):
        self.win.redraw()
        time.sleep(0.05)
  
    def break_entrance_and_exit(self):
        entrance = self.cells[0][0]
        exit = self.cells[self.num_cols-1][self.num_rows-1]
        entrance.has_top_wall = False
        entrance.draw()
        exit.has_bottom_wall = False
        exit.draw()
        

    def break_walls_r(self, i, j):
        self.cells[i][j].visited = True
        while True:
            not_visited = []
            #check for top neighbor
            if i > 0:
                if self.cells[i-1][j].visited == False:
                    not_visited.append((i-1, j))
            #check for bottom neighbor
            if i < self.num_cols-1:
                if self.cells[i+1][j].visited == False:
                    not_visited.append((i+1,j))
            #check for right neighbor
            if j < self.num_rows-1:
                if self.cells[i][j+1].visited == False:
                    not_visited.append((i, j+1))
            #check for left neighbor
            if j > 0:
                if self.cells[i][j-1].visited == False:
                    not_visited.append((i,j-1))
            #check for no directions to go
            if len(not_visited) == 0:
                self.cells[i][j].draw()
                return
            direction = random.choice(not_visited)
            if i > direction[0]:
                self.cells[i][j].has_left_wall = False
                self.cells[direction[0]][direction[1]].has_right_wall = False
            if i < direction[0]:
                self.cells[i][j].has_right_wall = False
                self.cells[direction[0]][direction[1]].has_left_wall = False
            if j > direction[1]:
                self.cells[i][j].has_top_wall = False
                self.cells[direction[0]][direction[1]].has_bottom_wall = False
            if j < direction[1]:
                self.cells[i][j].has_bottom_wall = False
                self.cells[direction[0]][direction[1]].has_top_wall = False
            self.break_walls_r(direction[0],direction[1])
        

    def reset_cells_visited(self):
        for col in self.cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self.solve_r(0,0)

    def solve_r(self, i, j):
        self.animate()
        self.cells[i][j].visited = True
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True
        if i > 0 and self.cells[i-1][j].visited == False and self.cells[i][j].has_left_wall == False:
            self.cells[i][j].draw_move(self.cells[i-1][j])
            result = self.solve_r(i-1, j)
            if result == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i-1][j], undo=True)
        if i < self.num_cols-1 and self.cells[i+1][j].visited == False and self.cells[i][j].has_right_wall == False:
            self.cells[i][j].draw_move(self.cells[i+1][j])
            result = self.solve_r(i+1, j)
            if result == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i+1][j], undo=True)
        if j > 0 and self.cells[i][j-1].visited == False and self.cells[i][j].has_top_wall == False:
            self.cells[i][j].draw_move(self.cells[i][j-1])
            result = self.solve_r(i, j-1)
            if result == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j-1], undo=True)
        if j < self.num_rows - 1 and self.cells[i][j+1].visited == False and self.cells[i][j].has_bottom_wall == False:
            self.cells[i][j].draw_move(self.cells[i][j+1])
            result = self.solve_r(i, j+1)
            if result == True:
                return True
            else:
                self.cells[i][j].draw_move(self.cells[i][j+1], undo=True)
        
        return False

