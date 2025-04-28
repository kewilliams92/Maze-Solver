from cell import Cell
from window import Window


# wide rectangle example coordinates: (50, 5) (500, 100)
def main():
    win = Window(800, 600)
    # create a cell
    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(50, 50, 5, 100)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(500, 500, 5, 100)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(50, 500, 5, 5)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(50, 500, 100, 100)

    win.wait_for_close()


main()
