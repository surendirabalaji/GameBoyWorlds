from typing import Dict, Type

from gameboy_worlds.interface.controller import Controller
from gameboy_worlds.interface.environment import DummyEnvironment, Environment
from gameboy_worlds.interface.survival_kids.environments import (
    SurvivalKidsEnvironment,
    SurvivalKidsTestEnvironment,
)


AVAILABLE_ENVIRONMENTS: Dict[str, Dict[str, Type[Environment]]] = {
    "survival_kids_1": {
        "dummy": DummyEnvironment,
        "default": SurvivalKidsEnvironment,
        "test": SurvivalKidsTestEnvironment,
    },
    "survival_kids_2": {
        "dummy": DummyEnvironment,
        "default": SurvivalKidsEnvironment,
        "test": SurvivalKidsTestEnvironment,
    },
}

AVAILABLE_CONTROLLERS: Dict[str, Dict[str, Type[Controller]]] = {}
