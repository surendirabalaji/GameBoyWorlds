from gameboy_worlds.emulation.runes_of_virtue.trackers import (
    CoreRunesOfVirtueTracker,
)
from gameboy_worlds.interface.environment import (
    DummyEnvironment,
    TestEnvironmentMixin,
    TrainEnvironmentMixin,
)


class RunesOfVirtueEnvironment(DummyEnvironment):
    """
    A basic Runes of Virtue Environment.
    """

    REQUIRED_STATE_TRACKER = CoreRunesOfVirtueTracker


class RunesOfVirtueTestEnvironment(TestEnvironmentMixin, RunesOfVirtueEnvironment):
    pass


class RunesOfVirtueTrainEnvironment(TrainEnvironmentMixin, RunesOfVirtueEnvironment):
    pass
