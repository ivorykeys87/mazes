from graphics import *

def main():
    win = Window(800, 600)
    point1 = Point(5, 10)
    point2 = Point(20,50)
    line = Line(point1, point2)
    win.draw_line(line,"black")
    win.wait_for_close()

main()