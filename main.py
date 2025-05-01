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
        while self.running == True:
            self.redraw()

    def close(self):
        self.running = False

def main():
    win = Window(800, 600)
    win.wait_for_close()

main()