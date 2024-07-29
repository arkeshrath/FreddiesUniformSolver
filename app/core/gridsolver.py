import logging

# Setup static logger instance
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class gridsolver:
    def __init__(self):
        logger.info('Grid creator initialized')
    def create_grid(self, coords):
        """ Create grid with dimensions calculated from input. """
        max_x = max(x for x, y in coords) + 1
        max_y = max(y for x, y in coords) + 1
        grid = [['.' for _ in range(max_x)] for _ in range(max_y)]
        for x, y in coords:
            grid[int(y)][int(x)] = '0'
        logger.info('Created grid with dimensions: %s x %s', max_x, max_y)
        return grid

    def print_grid(self, grid):
        for row in grid:
            print(''.join(row))
        print()
    def grid_to_string(self, grid):
        grid_str = ''
        for row in grid:
            grid_str += ''.join(row) + '\n'
        return grid_str
    def can_fold_line(self, grid, axis, line):
        """ Check if fold line is free of all black cells. """
        if axis == 'y':
            return all(grid[line][x] == '.' for x in range(len(grid[0])))
        elif axis == 'x':
            return all(grid[y][line] == '.' for y in range(len(grid)))
        return False
    def fold_grid(self, grid, axis, line, direction):
        """ Perform folding transformations on input data. """
        logger.info("Folding grid along %s=%d in %s direction", axis, line, direction)
        folded_grid = []

        try:
            if axis == 'y':
                if not self.can_fold_line(grid, axis, line):
                    raise ValueError(f"Cannot fold along y={line} because it contains black cells.")

                top = grid[:line]
                bottom = grid[line + 1:]

                # Pad the smaller side if necessary
                if len(top) < len(bottom):
                    top = [['.'] * len(top[0]) for _ in range(len(bottom) - len(top))] + top
                elif len(bottom) < len(top):
                    bottom = [['.'] * len(bottom[0]) for _ in range(len(top) - len(bottom))] + bottom

                if direction == 'up':
                    bottom.reverse()

                folded_grid = [
                    [
                        '0' if top[i][j] == '0' or bottom[i][j] == '0' else '.'
                        for j in range(len(top[0]))
                    ]
                    for i in range(len(top))
                ]

            elif axis == 'x':
                if not self.can_fold_line(grid, axis, line):
                    raise ValueError(f"Cannot fold along x={line} because it contains black cells.")

                left = [row[:line] for row in grid]
                right = [row[line + 1:] for row in grid]

                # Pad the smaller side if necessary
                max_width = max(len(left[0]), len(right[0]))
                if len(left[0]) < max_width:
                    left = [row + ['.'] * (max_width - len(row)) for row in left]
                if len(right[0]) < max_width:
                    right = [row + ['.'] * (max_width - len(row)) for row in right]

                if direction == 'left':
                    right = [row[::-1] for row in right]

                folded_grid = [
                    [
                        '0' if left[i][j] == '0' or right[i][j] == '0' else '.'
                        for j in range(len(left[0]))
                    ]
                    for i in range(len(left))
                ]

            return "SUCCESS", folded_grid
        except ValueError as ve:
            logger.error("A black cell is present in the fold line along %s=%d in %s direction", axis, line, direction)
            return f"Error : A black cell is present in the fold line along {axis}={line} in {direction} direction", grid
        except IndexError as ie:
            logger.error("A black cell is present in the fold line along %s=%d in %s direction", axis, line, direction)
            return f"Fold index is out of range!", grid

    def apply_folds(self, grid, folds):
        logger.info("Applying fold instructions: %s", folds)
        for fold in folds:
            axis = fold.get('axis')
            line = fold.get('line')
            direction = fold.get('direction')
            status, grid = self.fold_grid(grid, axis, line, direction)
        return status, grid