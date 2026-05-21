from gameboy_worlds.emulation.emulator import Emulator
from gameboy_worlds.emulation.runes_of_virtue.parsers import RunesOfVirtueStateParser
from gameboy_worlds.emulation.runes_of_virtue.trackers import CoreRunesOfVirtueTracker


class RunesOfVirtueEmulator(Emulator):
    """
    Emulator subclass for Runes of Virtue. Mirrors Pokemon's PokemonEmulator
    in shape so that game-specific quirks (auto-skip title screen, dialogue
    auto-advance, etc.) can be added here as they are discovered. For now
    behaves identically to the base Emulator.
    """

    REQUIRED_STATE_PARSER = RunesOfVirtueStateParser
    REQUIRED_STATE_TRACKER = CoreRunesOfVirtueTracker
