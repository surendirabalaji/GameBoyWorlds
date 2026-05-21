from gameboy_worlds.emulation.runes_of_virtue.base_metrics import (
    CoreRunesOfVirtueMetrics,
)
from gameboy_worlds.emulation.runes_of_virtue.test_metrics import (
    RunesOfVirtue1CaveOfDeceitTerminateMetric,
    RunesOfVirtue1ChucklesDialogTerminateMetric,
    RunesOfVirtue1DeathScreenTerminateMetric,
    RunesOfVirtue1GnuGnu1DialogTerminateMetric,
    RunesOfVirtue1GnuGnu2DialogTerminateMetric,
    RunesOfVirtue1KingDialogTerminateMetric,
    RunesOfVirtue1OpenMenuTerminateMetric,
    RunesOfVirtue1SherryDialogTerminateMetric,
    RunesOfVirtue1TelescopeViewTerminateMetric,
    RunesOfVirtue2NystulDialogTerminateMetric,
    RunesOfVirtue2OpenMenuTerminateMetric,
    RunesOfVirtue2ReadBookTerminateMetric,
)
from gameboy_worlds.emulation.tracker import (
    DummySubGoalMetric,
    StateTracker,
    TestTrackerMixin,
)


class CoreRunesOfVirtueTracker(StateTracker):
    """
    StateTracker for core Runes of Virtue metrics.
    """

    def start(self):
        super().start()
        self.metric_classes.extend([CoreRunesOfVirtueMetrics])


class RunesOfVirtueTestTracker(TestTrackerMixin, CoreRunesOfVirtueTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Runes of Virtue games.
    """

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue1OpenMenuTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1OpenMenuTestTracker(RunesOfVirtueTestTracker):
    """
    A TestTracker for Runes of Virtue 1 that ends an episode when the player opens the inventory menu.
    """

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue1OpenMenuTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue2OpenMenuTestTracker(RunesOfVirtueTestTracker):
    """
    A TestTracker for Runes of Virtue 2 that ends an episode when the player opens the inventory menu.
    """

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue2OpenMenuTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue2ReadBookTestTracker(RunesOfVirtueTestTracker):
    """Ends an episode when the player opens a book."""

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue2ReadBookTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue2NystulDialogTestTracker(RunesOfVirtueTestTracker):
    """Ends an episode when the player is in dialog with Nystul."""

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue2NystulDialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1KingDialogTestTracker(RunesOfVirtueTestTracker):
    """Ends an episode when the player is in dialog with the king."""

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue1KingDialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1ChucklesDialogTestTracker(RunesOfVirtueTestTracker):
    """Ends an episode when the player is in dialog with Chuckles."""

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue1ChucklesDialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1GnuGnu1DialogTestTracker(RunesOfVirtueTestTracker):
    """Ends an episode when the player is in dialog with Gnu Gnu at his 1st store."""

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue1GnuGnu1DialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1GnuGnu2DialogTestTracker(RunesOfVirtueTestTracker):
    """Ends an episode when the player is in dialog with Gnu Gnu at his 2nd store."""

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue1GnuGnu2DialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1SherryDialogTestTracker(RunesOfVirtueTestTracker):
    """Ends an episode when the player is in dialog with Sherry."""

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue1SherryDialogTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1CaveOfDeceitTestTracker(RunesOfVirtueTestTracker):
    """Ends an episode when the player has entered the Cave of Deceit."""

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue1CaveOfDeceitTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1TelescopeViewTestTracker(RunesOfVirtueTestTracker):
    """Ends an episode when the player is looking through the telescope."""

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue1TelescopeViewTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric


class RunesOfVirtue1DeathScreenTestTracker(RunesOfVirtueTestTracker):
    """Ends an episode when the death / game over screen is shown."""

    TERMINATION_TRUNCATION_METRIC = RunesOfVirtue1DeathScreenTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric
