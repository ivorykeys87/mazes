from graphics import Line, Point

class Cell():
    def __init__(self, l=True, r=True, t=True, b=True, p1=None, p2=None, window=None):
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
        if self.has_left_wall:
            lline = Line(Point(self.x1,self.y1), Point(self.x1, self.y2))
            self.win.draw_line(lline)
        if self.has_right_wall:
            rline = Line(Point(self.x2,self.y1), Point(self.x2, self.y2))
            self.win.draw_line(rline)
        if self.has_top_wall:
            tline = Line(Point(self.x1,self.y1), Point(self.x2, self.y1))
            self.win.draw_line(tline)
        if self.has_bottom_wall:
            bline = Line(Point(self.x1,self.y2), Point(self.x2, self.y2))
            self.win.draw_line(bline)
