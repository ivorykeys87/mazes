from graphics import *

def main():
    win = Window(800, 600)
    point1 = Point(100, 100)
    point2 = Point(200,200)
    cell= Cell(True, True, True, True, point1, point2, win)
    cell.draw()
    win.wait_for_close()

main()