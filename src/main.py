from graphics import Line, Point, Window


def main():
    window = Window(800, 600)
    p1 = Point(50, 50)
    p2 = Point(200, 200)
    p3 = Point(50, 350)
    p4 = Point(500, 300)

    # create a line
    line = Line(p1, p2)
    line2 = Line(p3, p4)

    # Draw line on window
    window.draw_line(line, "red")
    window.draw_line(line2, "blue")
    # close window
    window.wait_for_close()


main()
