from cell import Cell
from window import Window


def main():
    win = Window(800, 600)
    # create a cell
    cell = Cell(win)
    cell.has_left_wall = False
    cell.draw(100, 100, 200, 200)

    cell = Cell(win)
    cell.has_right_wall = False
    cell.draw(200, 100, 300, 200)

    cell = Cell(win)
    cell.has_top_wall = False
    cell.draw(300, 100, 400, 200)

    cell = Cell(win)
    cell.has_bottom_wall = False
    cell.draw(400, 200, 500, 100)

    win.wait_for_close()


main()
