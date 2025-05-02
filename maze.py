from cell import Cell
from graphics import Point, Window
import time

class Maze():
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = []
        self._create_cells()

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

    def animate(self):
        self.win.redraw()
        time.sleep(0.15)
        