from graphics import Line, Point

class Cell():
    def __init__(self, l=True, r=True, t=True, b=True, p1=None, p2=None, window=None, visited = False):
        self.has_left_wall = l
        self.has_right_wall = r
        self.has_top_wall = t
        self.has_bottom_wall = b
        self.x1 = p1.x
        self.y1 = p1.y
        self.x2 = p2.x
        self.y2 = p2.y
        self.win = window

    def draw(self):
        if self.win is None:
            return
        if self.has_left_wall:
            lline = Line(Point(self.x1,self.y1), Point(self.x1, self.y2))
            self.win.draw_line(lline)
        if not self.has_left_wall:
            lline = Line(Point(self.x1,self.y1), Point(self.x1, self.y2))
            self.win.draw_line(lline, color="white")
        if self.has_right_wall:
            rline = Line(Point(self.x2,self.y1), Point(self.x2, self.y2))
            self.win.draw_line(rline)
        if not self.has_right_wall:
            rline = Line(Point(self.x2,self.y1), Point(self.x2, self.y2))
            self.win.draw_line(rline, color="white")
        if self.has_top_wall:
            tline = Line(Point(self.x1,self.y1), Point(self.x2, self.y1))
            self.win.draw_line(tline)
        if not self.has_top_wall:
            tline = Line(Point(self.x1,self.y1), Point(self.x2, self.y1))
            self.win.draw_line(tline, color= "white")
        if self.has_bottom_wall:
            bline = Line(Point(self.x1,self.y2), Point(self.x2, self.y2))
            self.win.draw_line(bline)
        if not self.has_bottom_wall:
            bline = Line(Point(self.x1,self.y2), Point(self.x2, self.y2))
            self.win.draw_line(bline, color="white")

    def draw_move(self, to_cell, undo=False):
        color = "red" if not undo else "gray"
        line = Line(Point((self.x1+self.x2)/2,(self.y1+self.y2)/2),Point((to_cell.x1+to_cell.x2)/2,(to_cell.y1+to_cell.y2)/2))
        self.win.draw_line(line,color)
