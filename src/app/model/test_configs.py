"""
Unit tests for the configs module.
"""

import yaml
import tempfile
import unittest
from unittest.mock import patch

import configs


class TestConfigs(unittest.TestCase):
    """Test cases for the Configs module."""

    @patch("configs.CONFIG_PATH", tempfile.NamedTemporaryFile().name)  # pylint: disable=consider-using-with
    def test_read_config(self):
        # Create a temporary config file with test data
        test_config = {"background": "pink", "main_color": "light",
                       "font_size": "14"}

        with open(configs.CONFIG_PATH, "w", encoding="utf-8") as file:
            file.write(yaml.dump(test_config))

        # Test reading the config
        config = configs.read_config()
        self.assertEqual(config, test_config)

    @patch("configs.CONFIG_PATH", tempfile.NamedTemporaryFile().name)  # pylint: disable=consider-using-with
    def test_update_config(self):
        # Create a temporary config file with test data
        test_config = {"background": "pink", "main_color": "light",
                       "font_size": "14"}
        with open(configs.CONFIG_PATH, "w", encoding="utf-8") as file:
            file.write(yaml.dump(test_config))

        # Test updating the config
        key = "background"
        new_value = "green"
        configs.update_config(key, new_value)

        updated_config = configs.read_config()
        self.assertEqual(updated_config[key], new_value)


if __name__ == "__main__":
    unittest.main()
