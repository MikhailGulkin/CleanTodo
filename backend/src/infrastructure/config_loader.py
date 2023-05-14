import os

# import tomllib
from pathlib import Path
from typing import TypeVar

import tomli
from adaptix import Retort

T = TypeVar("T")
DEFAULT_CONFIG_PATH = "./config/config.toml"


def read_toml(path: str) -> dict:
    with open(Path(__file__).absolute().parent.parent.parent.joinpath(path), "rb") as f:
        return tomli.load(f)


def load_config(config_type: type[T], config_scope: str | None = None, path: str | None = None) -> T:
    if path is None:
        path = os.getenv("CONFIG_PATH", DEFAULT_CONFIG_PATH)

    data = read_toml(path)

    if config_scope is not None:
        data = data[config_scope]

    dcf = Retort()
    config = dcf.load(data, config_type)
    return config
