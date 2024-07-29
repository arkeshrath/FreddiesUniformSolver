import logging
import time

from app.utilities.helper import Helper
from app.core.gridsolver import gridsolver

# Setup static logger instance
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class GridController:
    def __init__(self):
        self.helper = Helper()
        self.grid_solver = gridsolver()

    def solve_grid(self, file_path):
        with open(file_path, 'r') as f:
            file_content = f.read()

        start_time = time.time()
        coords, folds = self.helper.parse_file_content(file_content)

        if not coords:
            logger.warning("Invalid file format: no coordinates")
            return 'Unable to create grid due to invalid coordinates', [], 400

        status, grid = self.grid_solver.apply_folds(self.grid_solver.create_grid(coords), folds)
        total_time = time.time() - start_time

        if status != 'SUCCESS':
            logger.info(status)
            return status, self.grid_solver.grid_to_string(grid), 400

        logger.info("File uploaded and solved grid for filename: %s in %s seconds", file_path, total_time)
        return status, self.grid_solver.grid_to_string(grid), 200

