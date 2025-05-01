from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, w, h):
        self.root = Tk()
        self.root.title("My Maze Solver")
        self.canvas = Canvas(self.root, width = w, height = h, bg = "white")
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.canvas.update_idletasks()
        self.canvas.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, color="black"):
        line.draw(self.canvas, color)

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, point1, point2):
        self.x1 = point1.x
        self.y1 = point1.y
        self.x2 = point2.x
        self.y2 = point2.y

    def draw(self, canvas, color="black"):
        canvas.create_line(
            self.x1, self.y1, self.x2, self.y2, fill=color, width=2
        )
