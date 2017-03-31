import re
import os
from math import floor

TOGGLE = True
UPPER_LIMIT = 5 if TOGGLE else 9


def string_to_2d_array(strings):
    return [[int(character) for character in line] for line in strings]


def get_block(integer):
    return int(floor(integer / 3))


class SudokuBlock:
    def __init__(self, sudoku_grid, x, y, value):
        self.sudoku_grid = sudoku_grid
        self.x = x
        self.y = y

        self.value = value

        if self.value > 0:
            self.possibilities = set()
        else:
            self.possibilities = set(range(1, 9 + 1))

    def discard_possibility(self, possibility):
        if possibility in self.possibilities:
            self.possibilities.remove(possibility)
            self.solve()

    def solve(self):
        if len(self.possibilities) == 1:
            assert self.value == 0, ""
            self.value = self.possibilities.pop()

            self.sudoku_grid.queue.append(self)

    def solved(self):
        return self.value > 0

    def string(self, debug=False):
        if debug and len(self.possibilities):
            if len(self.possibilities) == 9 and TOGGLE:
                return '*'

            elif len(self.possibilities) > UPPER_LIMIT:
                return '!' + str(','.join(str(i)
                    for i in set(range(1, 9 + 1)) - self.possibilities))

            return str('/'.join(str(i) for i in self.possibilities))

        return str(self.value or '-')

    def __str__(self):
        return self.string()

    def info(self):
        return '{}({},{})'.format(self.value, self.x, self.y)

class SudokuSolver:
    def __init__(self, grid=None):
        self.grid = [[
            SudokuBlock(self, x, y, initial_value)
            for x, initial_value in enumerate(line)]
            for y, line in enumerate(grid)
        ]

        self.queue = []
        self.update()

    def update(self):
        self.queue = [cell for blocks in self.grid
            for cell in blocks if cell.solved()]

    def solve(self):
        while self.queue:
            cell = self.queue.pop(0)

            print('\nGetting Rid of {}[{}, {}] Queue={}'.format(
                cell.value, cell.x, cell.y, [a.info() for a in self.queue]))
            print(self.string(True))

            # Row iteration : see if slicing improves performance
            for block in self.grid[cell.y]:
                block.discard_possibility(cell.value)

            # Column iteration
            for blocks in self.grid:
                blocks[cell.x].discard_possibility(cell.value)

            # Cell iteration
            x_bound = get_block(cell.x)
            y_bound = get_block(cell.y)

            for blocks in self.grid[y_bound * 3:y_bound * 3 + 3]:
                for cell_ in blocks[x_bound * 3:x_bound * 3 + 3]:
                    cell_.discard_possibility(cell.value)

    def string(self, debug=False):
        GRID = 5
        if debug:
            GRID = 12 if TOGGLE else 18

        strings = ['+' + '+'.join(['-' * (GRID * 3 + 2)] * 3) + '+']
        for index, blocks in enumerate(self.grid):
            strings += [
                '|'+ '|'.join(block.string(debug).center(GRID) for block in blocks)
                + '|']

            if index % 3 == 2:
                strings += ['+' + '+'.join(['-' * (GRID * 3 + 2)] * 3) + '+']

        return '\n'.join(strings)

    def __str__(self):
        return self.string()

    def solved(self):
        return all(len(cell.possibilities) == 0
            for line in self.grid for cell in line)


SUFFIX = os.path.expanduser('~') + '/git/Euler/'


def q96():
    new_line_regex = re.compile('Grid ([0-9]*)')
    with open(SUFFIX + 'data/p096_sudoku.txt', 'r') as file:
        string_buffer = []
        last_match = None

        for line in file.readlines():
            new_line_match = new_line_regex.match(line)
            if new_line_match:
                if len(string_buffer):
                    array = string_to_2d_array(string_buffer)
                    solver = SudokuSolver(array)
                    solver.solve()

                    index, = last_match.groups()
                    print('\nGrid {}: {}'.format(index, solver.solved()))
                    print(str(solver) + '\n')
                    if not solver.solved():
                        return -1

                string_buffer = []
                last_match = new_line_match
            else:
                string_buffer.append(line.strip('\n'))

    return -1


if __name__ == '__main__':
    q96()
