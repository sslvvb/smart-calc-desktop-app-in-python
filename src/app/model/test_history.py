"""
Unit tests for the history module.
"""

import unittest
import tempfile
import os
from unittest.mock import patch

import history


class TestHistory(unittest.TestCase):
    """Test cases for the History module."""

    def test_read_file(self):
        # Test reading history from the history file
        test_data = ["22=22.0; x=1.0\n", "11=11.0; x=1.0\n", "38=38.0; x=1.0\n"]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_history_file = os.path.join(temp_dir, "history.txt")
            with open(temp_history_file, "w", encoding="utf-8") as file:
                file.writelines(test_data)

            with patch("history._HISTORY_PATH", temp_history_file):
                history_data = history.read_file()

            self.assertEqual(history_data, test_data)

    def test_clean(self):
        # Test clearing the history file
        test_data = ["22=22.0; x=1.0\n", "11=11.0; x=1.0\n", "38=38.0; x=1.0\n"]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_history_file = os.path.join(temp_dir, "history.txt")
            with open(temp_history_file, "w", encoding="utf-8") as file:
                file.writelines(test_data)

            with patch("history._HISTORY_PATH", temp_history_file):
                history.clean()

                with open(temp_history_file, "r", encoding="utf-8") as file:
                    cleaned_history = file.read()

                self.assertEqual(cleaned_history, "")

    def test_write(self):
        # Test writing a new expression to the history file
        test_data = ["22=22.0; x=1.0\n", "11=11.0; x=1.0\n"]

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_history_file = os.path.join(temp_dir, "history.txt")
            with open(temp_history_file, "w", encoding="utf-8") as file:
                file.writelines(test_data)

            new_expression = "38=38.0; x=1.0"
            expected_result = [new_expression + "\n"] + test_data

            with patch("history._HISTORY_PATH", temp_history_file):
                history.write(new_expression)

                with open(temp_history_file, "r", encoding="utf-8") as file:
                    updated_history = file.readlines()

                self.assertEqual(updated_history, expected_result)


if __name__ == "__main__":
    unittest.main()
