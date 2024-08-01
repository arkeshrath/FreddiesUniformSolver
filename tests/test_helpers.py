import unittest
from app.utilities.helper import Helper

class TestHelper(unittest.TestCase):

    def setUp(self):
        self.helper = Helper()
        self.sample_content = (
            "cell at x=0,y=0\n"
            "cell at x=11,y=10\n"
            "cell at x=3,y=0\n"
            "fold up along y=5\n"
            "fold left along x=7\n"
        )
        self.invalid_content = (
            "cell at x=0,y=0\n"
            "cell at x=11,y=10\n"
            "cell at x=invalid,y=0\n"  # Invalid coordinate
            "fold up along y=5\n"
            "fold left along x=7\n"
        )

    def test_md5_hash(self):
        file_content = "This is a test content"
        expected_md5 = "75e6f8645a9f5059e0970f95a3a0c0be"
        self.assertEqual(self.helper.md5_hash(file_content), expected_md5)

    def test_parse_file_content_valid(self):
        coords, folds = self.helper.parse_file_content(self.sample_content)
        expected_coords = [(0, 0), (11, 10), (3, 0)]
        expected_folds = [
            {"axis": "y", "line": 5, "direction": "up"},
            {"axis": "x", "line": 7, "direction": "left"}
        ]
        self.assertEqual(coords, expected_coords)
        self.assertEqual(folds, expected_folds)

    def test_parse_file_content_invalid(self):
        with self.assertRaises(ValueError):
            self.helper.parse_file_content(self.invalid_content)

    def test_allowed_file(self):
        assert self.helper.allowed_file('abc.txt') == True
        assert self.helper.allowed_file('abc.png') == False

if __name__ == '__main__':
    unittest.main()
