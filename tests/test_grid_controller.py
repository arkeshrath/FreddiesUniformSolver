import unittest
from unittest.mock import patch, MagicMock
from app.controller.grid_controller import GridController

class TestGridController(unittest.TestCase):

    def setUp(self):
        self.controller = GridController()

    @patch('app.controller.grid_controller.Helper')
    @patch('app.controller.grid_controller.gridsolver')
    def test_solve_grid_success(self, MockGridSolver, MockHelper):
        # Mock Helper
        mock_helper = MockHelper.return_value
        mock_helper.parse_file_content.return_value = ([(0, 0), (1, 2)], [{'axis': 'y', 'line': 1, 'direction': 'up'}])

        # Mock GridSolver
        mock_grid_solver = MockGridSolver.return_value
        mock_grid_solver.create_grid.return_value = [['0', '.'], ['.', '.'], ['.', '0']]
        mock_grid_solver.apply_folds.return_value = ('SUCCESS', [['0', '0']])
        mock_grid_solver.grid_to_string.return_value = '0.\n'

        with patch('builtins.open',
                   unittest.mock.mock_open(read_data='cell at x=0,y=0\ncell at x=1,y=2\nfold up along y=1')):
            status, grid_str, status_code = self.controller.solve_grid('test_file.txt')

        self.assertEqual(status, 'SUCCESS')
        self.assertEqual(grid_str, '00\n')
        self.assertEqual(status_code, 200)

    @patch('app.controller.grid_controller.Helper')
    @patch('app.controller.grid_controller.gridsolver')
    def test_solve_grid_invalid_coords(self, MockGridSolver, MockHelper):
        # Mock Helper
        mock_helper = MockHelper.return_value
        mock_helper.parse_file_content.return_value = ([], [])

        with patch('builtins.open', unittest.mock.mock_open(read_data='fold up along y=1')):
            status, grid_str, status_code = self.controller.solve_grid('test_file.txt')

        self.assertEqual(status, 'Unable to create grid due to invalid coordinates')
        self.assertEqual(grid_str, [])
        self.assertEqual(status_code, 400)

    @patch('app.controller.grid_controller.Helper')
    @patch('app.controller.grid_controller.gridsolver')
    def test_solve_grid_failure(self, MockGridSolver, MockHelper):
        # Mock Helper
        mock_helper = MockHelper.return_value
        mock_helper.parse_file_content.return_value = ([(0, 0)], [{'axis': 'y', 'line': 1, 'direction': 'up'}])

        # Mock GridSolver
        mock_grid_solver = MockGridSolver.return_value
        mock_grid_solver.create_grid.return_value = [['0']]
        mock_grid_solver.apply_folds.return_value = ('Fold index is out of range!', [['0', '.']])
        mock_grid_solver.grid_to_string.return_value = '0\n'

        with patch('builtins.open', unittest.mock.mock_open(read_data='cell at x=0,y=0\nfold up along y=1')):
            status, grid_str, status_code = self.controller.solve_grid('test_file.txt')

        self.assertEqual(status, 'Fold index is out of range!')
        self.assertEqual(grid_str, '0\n')
        self.assertEqual(status_code, 400)

if __name__ == '__main__':
    unittest.main()
