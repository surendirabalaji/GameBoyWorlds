from typing import Optional

import numpy as np

from gameboy_worlds.emulation.runes_of_virtue.parsers import (
    RunesOfVirtueStateParser,
)
from gameboy_worlds.emulation.tracker import (
    RegionMatchTerminationMetric,
    TerminationMetric,
)


class RunesOfVirtue1OpenMenuTerminateMetric(TerminationMetric):
    """Terminates the episode when the player opens the inventory menu in Runes of Virtue 1."""

    REQUIRED_PARSER = RunesOfVirtueStateParser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtueStateParser
            if self.state_parser.is_in_menu(frame):
                return True
        return False


class RunesOfVirtue2OpenMenuTerminateMetric(TerminationMetric):
    """Terminates the episode when the player opens the inventory menu in Runes of Virtue 2."""

    REQUIRED_PARSER = RunesOfVirtueStateParser

    def determine_terminated(
        self, current_frame: np.ndarray, recent_frames: Optional[np.ndarray]
    ) -> bool:
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            self.state_parser: RunesOfVirtueStateParser
            if self.state_parser.is_in_menu(frame):
                return True
        return False


class RunesOfVirtue1KingDialogTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    """Terminates when the king's dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    _TERMINATION_NAMED_REGION = "king_dialog_indicator"
    _TERMINATION_TARGET_NAME = "king_dialog"


class RunesOfVirtue2ReadBookTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    """Terminates when an opened book is on screen."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    _TERMINATION_NAMED_REGION = "book_open_indicator"
    _TERMINATION_TARGET_NAME = "book_open"


class RunesOfVirtue2NystulDialogTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    """Terminates when Nystul's dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    _TERMINATION_NAMED_REGION = "nystul_dialog_indicator"
    _TERMINATION_TARGET_NAME = "nystul_dialog"


class RunesOfVirtue1ChucklesDialogTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    """Terminates when Chuckles's dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    _TERMINATION_NAMED_REGION = "dialog_indicator"
    _TERMINATION_TARGET_NAME = "chuckles_dialog"


class RunesOfVirtue1GnuGnu1DialogTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    """Terminates when Gnu Gnu's 1st store dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    _TERMINATION_NAMED_REGION = "dialog_indicator"
    _TERMINATION_TARGET_NAME = "gnu_gnu_1_dialog"


class RunesOfVirtue1GnuGnu2DialogTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    """Terminates when Gnu Gnu's 2nd store dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    _TERMINATION_NAMED_REGION = "dialog_indicator"
    _TERMINATION_TARGET_NAME = "gnu_gnu_2_dialog"


class RunesOfVirtue1SherryDialogTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    """Terminates when Sherry's dialog is on screen."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    _TERMINATION_NAMED_REGION = "dialog_indicator"
    _TERMINATION_TARGET_NAME = "sherry_dialog"


class RunesOfVirtue1CaveOfDeceitTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    """Terminates when the player is inside the Cave of Deceit."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    _TERMINATION_NAMED_REGION = "cave_of_deceit_indicator"
    _TERMINATION_TARGET_NAME = "cave_of_deceit"


class RunesOfVirtue1TelescopeViewTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    """Terminates when the telescope view is on screen."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    _TERMINATION_NAMED_REGION = "telescope_view_indicator"
    _TERMINATION_TARGET_NAME = "telescope_view"


class RunesOfVirtue1DeathScreenTerminateMetric(
    RegionMatchTerminationMetric, TerminationMetric
):
    """Terminates when the death / game over screen is on screen."""

    REQUIRED_PARSER = RunesOfVirtueStateParser
    _TERMINATION_NAMED_REGION = "death_screen_indicator"
    _TERMINATION_TARGET_NAME = "death_screen"
