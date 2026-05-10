"""
Survival Kids game state parsers.
"""

import os
from enum import Enum
from typing import Dict, List, Optional, Tuple

import numpy as np

from gameboy_worlds.emulation.parser import (
    NamedScreenRegion,
    StateParser,
    _get_proper_regions,
)
from gameboy_worlds.utils import log_error, verify_parameters


class AgentState(Enum):
    FREE_ROAM = 0
    IN_DIALOGUE = 1
    IN_MENU = 2


class SurvivalKidsParser(StateParser):
    """Game state parser for Survival Kids 1 (GBC)."""

    VARIANT = "survival_kids_1"

    MULTI_TARGET_REGIONS: List[Tuple[str, int, int, int, int]] = [
        ("screen", 0, 0, 160, 144),
        ("screen_bottom", 0, 108, 160, 36),
        ("game_viewport", 0, 0, 160, 108),
        ("dialogue_area", 8, 112, 144, 28),
        ("menu_area", 0, 0, 160, 144),
    ]

    MULTI_TARGETS: Dict[str, List[str]] = {}

    def __init__(
        self,
        pyboy,
        parameters: dict,
        additional_multi_target_regions: Optional[
            List[Tuple[str, int, int, int, int]]
        ] = None,
        override_multi_targets: Optional[Dict[str, List[str]]] = None,
    ):
        verify_parameters(parameters)
        additional_multi_target_regions = additional_multi_target_regions or []
        override_multi_targets = override_multi_targets or {}
        if f"{self.VARIANT}_rom_data_path" not in parameters:
            log_error(
                f"ROM data path not found for variant: {self.VARIANT}. "
                f"Add {self.VARIANT}_rom_data_path to the config files.",
                parameters,
            )
        self.rom_data_path = parameters[f"{self.VARIANT}_rom_data_path"]
        captures_dir = os.path.join(self.rom_data_path, "captures")

        multi_target_regions = _get_proper_regions(
            override_regions=additional_multi_target_regions,
            base_regions=self.MULTI_TARGET_REGIONS,
        )

        multi_targets: Dict[str, List[str]] = {}
        for key, val in self.MULTI_TARGETS.items():
            multi_targets[key] = list(val)
        for key, val in override_multi_targets.items():
            if key in multi_targets:
                multi_targets[key].extend(val)
            else:
                multi_targets[key] = list(val)

        named_screen_regions: List[NamedScreenRegion] = []
        for region_name, x, y, w, h in multi_target_regions:
            target_paths: Dict[str, str] = {}
            subdir = os.path.join(captures_dir, region_name)
            for target_name in multi_targets.get(region_name, []):
                target_paths[target_name] = os.path.join(subdir, target_name)
            region = NamedScreenRegion(
                region_name,
                x,
                y,
                w,
                h,
                parameters=parameters,
                multi_target_paths=target_paths,
            )
            named_screen_regions.append(region)

        super().__init__(pyboy, parameters, named_screen_regions)

    def is_in_dialogue(self, current_screen: np.ndarray) -> bool:
        return False

    def is_in_menu(self, current_screen: np.ndarray) -> bool:
        return False

    def get_agent_state(self, current_screen: np.ndarray) -> AgentState:
        if self.is_in_menu(current_screen):
            return AgentState.IN_MENU
        if self.is_in_dialogue(current_screen):
            return AgentState.IN_DIALOGUE
        return AgentState.FREE_ROAM

    def read_memory_byte(self, address: int) -> int:
        return self._pyboy.memory[address]

    def __repr__(self) -> str:
        return f"<SurvivalKidsParser(variant={self.VARIANT})>"


class SurvivalKids2Parser(SurvivalKidsParser):
    """Game state parser for Survival Kids 2 (GBC)."""

    VARIANT = "survival_kids_2"

    def __repr__(self) -> str:
        return f"<SurvivalKids2Parser(variant={self.VARIANT})>"

