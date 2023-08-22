"""Module for working with configuration data."""

import os
import yaml
from pathlib import Path

CONFIG_PATH: str = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "config/config.yml"
)


def read_config() -> dict:
    """
    Read and return the configuration from the configuration file.

    Returns:
        dict: Configuration data.
    """
    config: dict = _load_config()
    return config


def update_config(key: str, value: str) -> None:
    """
    Update the configuration with a new key-value pair.

    Args:
        key (str): Key to update.
        value (str): New value to set.
    """
    config: dict = read_config()
    config[key] = value
    _dump_config(config)


def _load_config() -> dict:
    """
    Load and return the configuration data from the configuration file.

    Returns:
        dict: Configuration data.
    """
    Path(CONFIG_PATH).touch(exist_ok=True)
    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        config: dict = yaml.safe_load(file) or {}
    return config


def _dump_config(config: dict) -> None:
    """
    # Dump the configuration data to the configuration file.

    Args:
        config (dict): Configuration data to write.
    """
    with open(CONFIG_PATH, "w", encoding="utf-8") as file:
        yaml.safe_dump(config, file)
