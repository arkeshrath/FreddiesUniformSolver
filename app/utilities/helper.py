# Setup static logger instance
import hashlib
import logging
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Helper:

    def validate_input(self, input_str):
    # Define the regex patterns
        cell_pattern = re.compile(r'^cell at x=\d+,y=\d+$')
        fold_pattern = re.compile(r'^fold (up|down|left|right) along [xy]=\d+$')
        empty_pattern = re.compile(r'^$')

        # Check the input string against each pattern
        if cell_pattern.match(input_str):
            return True
        elif fold_pattern.match(input_str):
            return True
        elif empty_pattern.match(input_str):
            return True
        else:
            return False

    def md5_hash(self, file_content):
        md5 = hashlib.md5()
        md5.update(file_content.encode('utf-8'))
        return md5.hexdigest()

    def parse_file_content(self, file_content):
        coords = []
        folds = []
        lines = file_content.strip().split('\n')
        line_count = 1

        for line in lines:
            if not self.validate_input(line):
                raise ValueError(f"Invalid Input given in clues file, please check line number {line_count}")
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
            line_count += 1

        return coords, folds
