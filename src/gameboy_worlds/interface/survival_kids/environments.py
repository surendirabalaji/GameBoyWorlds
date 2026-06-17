from gameboy_worlds.emulation.emulator import Emulator
from gameboy_worlds.emulation.survival_kids.trackers import (
    SurvivalKidsOCRTracker,
    SurvivalKidsTracker,
)
from gameboy_worlds.interface.environment import (
    DummyEnvironment,
    Environment,
    TestEnvironmentMixin,
    TrainEnvironmentMixin,
)


class SurvivalKidsEnvironment(DummyEnvironment):
    """A basic Survival Kids environment."""

    REQUIRED_EMULATOR = Emulator
    REQUIRED_STATE_TRACKER = SurvivalKidsTracker


class SurvivalKidsOCREnvironment(SurvivalKidsEnvironment):
    """A Survival Kids environment that includes OCR region captures."""

    REQUIRED_EMULATOR = Emulator
    REQUIRED_STATE_TRACKER = SurvivalKidsOCRTracker

    @staticmethod
    def override_emulator_kwargs(emulator_kwargs: dict) -> dict:
        Environment.override_state_tracker_class(
            emulator_kwargs, SurvivalKidsOCREnvironment.REQUIRED_STATE_TRACKER
        )
        return emulator_kwargs


class SurvivalKidsTestEnvironment(TestEnvironmentMixin, SurvivalKidsOCREnvironment):
    pass


class SurvivalKidsTrainEnvironment(TrainEnvironmentMixin, SurvivalKidsOCREnvironment):
    pass
