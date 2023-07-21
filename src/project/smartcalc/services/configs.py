"""Модуль для работы с файлом конфигурации."""

from pathlib import Path
import yaml

CONFIG_PATH: str = "config/config.yml"


def read_config() -> dict:
    config: dict = _load_config()
    return config


def update_config(key: str, value: str) -> None:
    config: dict = read_config()
    config[key] = value
    _dump_config(config)


def _load_config() -> dict:
    Path(CONFIG_PATH).touch(exist_ok=True)
    with open(CONFIG_PATH, 'r') as file:
        config: dict = yaml.safe_load(file) or {}
    return config


def _dump_config(config: dict) -> None:
    with open(CONFIG_PATH, 'w') as file:
        yaml.safe_dump(config, file)

# file naming ??

# def write_config(config: dict) -> None:
#     _dump_config(config)
