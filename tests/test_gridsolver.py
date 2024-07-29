import unittest
from app.core.gridsolver import gridsolver

class TestGridSolver(unittest.TestCase):

    def setUp(self):
        self.solver = gridsolver()

    def test_create_grid(self):
        coords = [(0, 0), (1, 1), (2, 2)]
        grid = self.solver.create_grid(coords)
        expected_grid = [
            ['0', '.', '.'],
            ['.', '0', '.'],
            ['.', '.', '0']
        ]
        self.assertEqual(grid, expected_grid, "Grid creation failed")

    def test_can_fold_line_y(self):
        grid = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '0', '.']
        ]
        self.assertTrue(self.solver.can_fold_line(grid, 'y', 0), "Should be able to fold along y=0")
        self.assertFalse(self.solver.can_fold_line(grid, 'y', 2), "Should not be able to fold along y=2")

    def test_can_fold_line_x(self):
        grid = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '0', '.']
        ]
        self.assertTrue(self.solver.can_fold_line(grid, 'x', 0), "Should be able to fold along x=0")
        self.assertFalse(self.solver.can_fold_line(grid, 'x', 1), "Should not be able to fold along x=1")

    def test_fold_grid_up(self):
        grid = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '0']
        ]
        _, folded_grid = self.solver.fold_grid(grid, 'y', 1, 'up')
        expected_grid = [
            ['.', '.', '0']
        ]
        self.assertEqual(folded_grid, expected_grid, "Folding grid up failed")

    def test_fold_grid_down(self):
        grid = [
            ['0', '.', '.'],
            ['.', '.', '.'],
            ['0', '.', '0']
        ]
        _, folded_grid = self.solver.fold_grid(grid, 'y', 1, 'down')
        expected_grid = [
            ['0', '.', '0']
        ]
        self.assertEqual(folded_grid, expected_grid, "Folding grid down failed")

    def test_fold_grid_left(self):
        grid = [
            ['.', '.', '0'],
            ['.', '.', '0'],
            ['.', '.', '0']
        ]
        _, folded_grid = self.solver.fold_grid(grid, 'x', 1, 'left')
        expected_grid = [
            ['0'],
            ['0'],
            ['0']
        ]
        self.assertEqual(folded_grid, expected_grid, "Folding grid left failed")

    def test_fold_grid_right(self):
        grid = [
            ['0', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        _, folded_grid = self.solver.fold_grid(grid, 'x', 1, 'right')
        expected_grid = [
            ['0'],
            ['.'],
            ['.']
        ]
        self.assertEqual(folded_grid, expected_grid, "Folding grid right failed")

    def test_apply_folds(self):
        coords = [(0, 0), (1, 1), (3, 3), (4, 4)]
        folds = [
            {'axis': 'y', 'line': 2, 'direction': 'up'},
            {'axis': 'x', 'line': 2, 'direction': 'left'}
        ]
        grid = self.solver.create_grid(coords)
        _, folded_grid = self.solver.apply_folds(grid, folds)
        expected_grid = [
            ['0', '.'],
            ['.', '0']
        ]
        self.assertEqual(folded_grid, expected_grid, "Applying folds failed")

    def test_apply_invalid_folds(self):
        coords = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
        folds = [
            {'axis': 'y', 'line': 2, 'direction': 'up'},
            {'axis': 'x', 'line': 2, 'direction': 'left'}
        ]
        grid = self.solver.create_grid(coords)
        status, folded_grid = self.solver.apply_folds(grid, folds)
        expected_status = f"Error : A black cell is present in the fold line along x=2 in left direction"
        self.assertEqual(status, expected_status)

if __name__ == '__main__':
    unittest.main()
