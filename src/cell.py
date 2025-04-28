from window import Line, Point


class Cell:
    def __init__(self, win):
        """The data members used to create the cell."""
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.__win = win

    def draw(self, x1, x2, y1, y2):
        # The cell needs to have coordinates in order to draw each wall.
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        """We draw a line based on if the cell has walls using the Line and Point classes from our window.py."""
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(x2, y2), Point(x2, y1))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self.__win.draw_line(line)
