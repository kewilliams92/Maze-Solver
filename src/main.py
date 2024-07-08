from cell import Cell
from graphics import Window


def main():
    window = Window(800, 600)

    # create a cell
    cell = Cell(window)
    cell.has_left_wall = False
    cell.draw(100, 100, 200, 200)

    cell = Cell(window)
    cell.has_top_wall = False
    cell.draw(200, 100, 300, 200)

    cell = Cell(window)
    cell.has_right_wall = False
    cell.draw(300, 100, 400, 200)

    cell = Cell(window)
    cell.has_bottom_wall = False
    cell.draw(400, 100, 500, 200)

    window.wait_for_close()


main()
