from graphics import *
from cell import *

def main():
    win = Window(800, 600)
    point1 = Point(100, 100)
    point2 = Point(200,200)
    point3 = Point(200, 100)
    point4 = Point(300,200)
    cell= Cell(p1=point1, p2=point2, window=win)
    cell2 = Cell(p1=point3, p2=point4, window=win)
    cell.draw()
    cell2.draw()
    cell.draw_move(cell2)
    win.wait_for_close()

main()