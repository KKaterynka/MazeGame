"""Implemention of the Maze ADT using a 2-D array."""
from arrays import Array2D
from lliststack import Stack


class Maze:
    """Define constants to represent contents of the maze cells."""
    MAZE_WALL = "*"
    PATH_TOKEN = "x"
    TRIED_TOKEN = "o"

    def __init__(self, num_rows, num_cols):
        """Creates a maze object with all cells marked as open."""
        self._maze_cells = Array2D(num_rows, num_cols)
        self._start_cell = None
        self._exit_cell = None
        self.path = None

    def num_rows(self):
        """Returns the number of rows in the maze."""
        return self._maze_cells.num_rows()

    def num_cols(self):
        """Returns the number of columns in the maze."""
        return self._maze_cells.num_cols()

    def set_wall(self, row, col):
        """Fills the indicated cell with a "wall" marker."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._maze_cells[row, col] = self.MAZE_WALL

    def set_start(self, row, col):
        """Sets the starting cell position."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._start_cell = _CellPosition(row, col)

    def set_exit(self, row, col):
        """Sets the exit cell position."""
        assert 0 <= row < self.num_rows() and \
               0 <= col < self.num_cols(), "Cell index out of range."
        self._exit_cell = _CellPosition(row, col)

    def find_path(self):
        """
        Attempts to solve the maze by finding a path from the starting cell
        to the exit. Returns True if a path is found and False otherwise.
        """
        self.path = Stack()
        self.path.push(self._start_cell)
        self._mark_path(self._start_cell.row, self._start_cell.col)
        while True:
            if self.path.is_empty():
                return False
            current_cell = self.path.peek()
            row = current_cell.row
            col = current_cell.col
            if not self._exit_found(row, col):
                for try_row in [row, row+1, row-1]:
                    if not current_cell.row == self.path.peek().row and not \
                            current_cell.col == self.path.peek().col:
                        break
                    for col_try in [col, col+1, col-1]:
                        if self._valid_move(try_row + row, col_try + col):
                            self._mark_path(try_row + row, col_try + col)
                            self.path.push(_CellPosition(try_row + row, col_try + col))
                            break
                if current_cell.row == self.path.peek().row and \
                        current_cell.col == self.path.peek().col:
                    del_cell = self.path.pop()
                    self._mark_tried(del_cell.row, del_cell.col)
                    try:
                        current_cell = self.path.peek()
                    except AssertionError:
                        return False
            else:
                return True

    def reset(self):
        """Resets the maze by removing all "path" and "tried" tokens."""
        self.path = None
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] == self.PATH_TOKEN or \
                        self._maze_cells[row, col] == self.TRIED_TOKEN:
                    self._maze_cells[row, col] = None

    def __str__(self):
        """Returns a text-based representation of the maze."""
        string = ""
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._maze_cells[row, col] != None:
                    string += str(self._maze_cells[row, col]) + " "
                else:
                    string += "_ "
            string += '' if row == self.num_rows() - 1 else '\n'
            # string += '\n'

        return string

    def _valid_move(self, row, col):
        """Returns True if the given cell position is a valid move."""
        return 0 <= row < self.num_rows() \
               and 0 <= col < self.num_cols() \
               and self._maze_cells[row, col] is None

    def _exit_found(self, row, col):
        """Helper method to determine if the exit was found."""
        return row == self._exit_cell.row and col == self._exit_cell.col

    def _mark_tried(self, row, col):
        """Drops a "tried" token at the given cell."""
        self._maze_cells[row, col] = self.TRIED_TOKEN

    def _mark_path(self, row, col):
        """Drops a "path" token at the given cell."""
        self._maze_cells[row, col] = self.PATH_TOKEN


class _CellPosition(object):
    """Private storage class for holding a cell position."""

    def __init__(self, row, col):
        self.row = row
        self.col = col
