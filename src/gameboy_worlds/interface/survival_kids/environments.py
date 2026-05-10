from gameboy_worlds.emulation.survival_kids.trackers import SurvivalKidsTracker
from gameboy_worlds.interface.environment import DummyEnvironment


class SurvivalKidsEnvironment(DummyEnvironment):
    REQUIRED_STATE_TRACKER = SurvivalKidsTracker
