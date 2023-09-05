# tests/test_utils.py

import unittest
from shared import calculate_file_hash, validate_file_hash


class TestUtils(unittest.TestCase):

    def test_calculate_file_hash(self):
        # Test the calculate_file_hash function
        test_filename = "test_file.txt"
        with open(test_filename, "w") as file:
            file.write("Hello, SFTP!")

        expected_hash = "5eb63bbbe01eeed093cb22bb8f5acdc3"
        self.assertEqual(calculate_file_hash(test_filename), expected_hash)

    def test_validate_file_hash(self):
        # Test the validate_file_hash function
        test_filename = "test_file.txt"
        with open(test_filename, "w") as file:
            file.write("Hello, SFTP!")

        expected_hash = "5eb63bbbe01eeed093cb22bb8f5acdc3"
        self.assertTrue(validate_file_hash(test_filename, expected_hash))
        self.assertFalse(validate_file_hash(test_filename, "invalid_hash"))


if __name__ == "__main__":
    unittest.main()
