# Setup static logger instance
import hashlib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Helper:

    def md5_hash(self, file_content):
        md5 = hashlib.md5()
        md5.update(file_content.encode('utf-8'))
        return md5.hexdigest()

    def parse_file_content(self, file_content):
        coords = []
        folds = []
        lines = file_content.strip().split('\n')

        for line in lines:
            line = line.strip()
            if line.startswith('cell at'):
                try:
                    # Extract coordinates from the line
                    parts = line.split()
                    x = int(parts[2].split(',')[0].split('=')[1])
                    y = int(parts[2].split(',')[1].split('=')[1])
                    coords.append((x, y))
                except (IndexError, ValueError) as e:
                    raise ValueError(f"Error parsing coordinate line '{line}'") from e

            elif line.startswith('fold'):
                try:
                    # Extract fold instructions from the line
                    parts = line.split()
                    axis = parts[3].split('=')[0]
                    fold_line = int(parts[3].split('=')[1])
                    direction = parts[1]
                    folds.append({"axis": axis, "line": fold_line, "direction": direction})
                except (IndexError, ValueError) as e:
                    raise ValueError(f"Error parsing fold line '{line}'") from e

        return coords, folds
