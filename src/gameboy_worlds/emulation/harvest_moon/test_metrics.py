from typing import Optional
from abc import ABC

from gameboy_worlds.emulation.harvest_moon.parsers import HarvestMoonStateParser, BaseHarvestMoonStateParser
from gameboy_worlds.emulation.tracker import (
    RegionMatchTerminationOnlyMetric,
    TerminationMetric,
    RegionMatchTerminationMetric,
    TerminationTruncationMetric,
    RegionMatchSubGoal,
    AnyRegionMatchSubGoal,
)


class MultiRegionMatchTerminationMetric(TerminationTruncationMetric, ABC):
    """
    Terminates when OR_PAIRS, ALL_PAIRS, and NOT_PAIRS conditions are all satisfied.
    OR_PAIRS: list of (region, target) — at least one must match.
    ALL_PAIRS: list of (region, target) — every one must match.
    NOT_PAIRS: list of (region, target) — none must match.
    Termination condition: (any OR_PAIR matches) AND (all ALL_PAIRS match) AND (no NOT_PAIR matches).
    Any list may be empty, in which case its condition is trivially satisfied.
    """

    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _OR_PAIRS: list = []
    _ALL_PAIRS: list = []
    _NOT_PAIRS: list = []

    def determine_terminated(self, current_frame, recent_frames):
        all_frames = [current_frame]
        if recent_frames is not None:
            all_frames = recent_frames
        for frame in all_frames:
            or_ok = (not self._OR_PAIRS) or any(
                self.state_parser.named_region_matches_multi_target(frame, region, target)
                for region, target in self._OR_PAIRS
            )
            all_ok = all(
                self.state_parser.named_region_matches_multi_target(frame, region, target)
                for region, target in self._ALL_PAIRS
            )
            not_ok = not any(
                self.state_parser.named_region_matches_multi_target(frame, region, target)
                for region, target in self._NOT_PAIRS
            )
            if or_ok and all_ok and not_ok:
                return True
        return False

class PreviousFrameTerminateMetric(TerminationTruncationMetric, ABC):
    """
    Terminates based on what was on screen BEFORE the final action.

    _TERMINATION_NAMED_REGION / _TERMINATION_TARGET_NAME: checked against the
    last frame of the previous step (i.e. the frame visible before the action).

    _CURRENT_NAMED_REGION / _CURRENT_TARGET_NAME: optional additional check
    against the current step's frames (e.g. confirming the action had effect).
    Both conditions must be satisfied when the current fields are set.

    _prev_frame is updated AFTER super().step() so that determine_terminated
    always sees the frame from the step before the current one.
    """
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION: str = None
    _TERMINATION_TARGET_NAME: str = None
    _CURRENT_NAMED_REGION: str = None
    _CURRENT_TARGET_NAME: str = None

    def step(self, current_frame, recent_frames):
        super().step(current_frame, recent_frames)
        self._prev_frame = recent_frames[-1] if recent_frames is not None else current_frame

    def determine_terminated(self, current_frame, recent_frames):
        if not hasattr(self, "_prev_frame"):
            return False
        prev_ok = self.state_parser.named_region_matches_multi_target(
            self._prev_frame,
            self._TERMINATION_NAMED_REGION,
            self._TERMINATION_TARGET_NAME,
        )
        if not prev_ok:
            return False
        if self._CURRENT_NAMED_REGION is None:
            return True
        all_frames = recent_frames if recent_frames is not None else [current_frame]
        return any(
            self.state_parser.named_region_matches_multi_target(
                frame, self._CURRENT_NAMED_REGION, self._CURRENT_TARGET_NAME
            )
            for frame in all_frames
        )

class ChickenCoopTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom"
    _TERMINATION_TARGET_NAME = "chicken_coop_entrance"

class OutsideChickenCoopSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_chicken_coop"
    _NAMED_REGIONS = [
        "screen_middle",
        "screen_middle",
        "screen_middle",
    ]
    _TARGET_NAMES = [
        "outside_chicken_coop_left",
        "outside_chicken_coop_right",
        "outside_chicken_coop_up",
    ]

class OutsideChickenCoop2Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_chicken_coop"
    _NAMED_REGIONS = [
        "outside_barns",
        "outside_barns",
        "outside_barns",
    ]
    _TARGET_NAMES = [
        "outside_chicken_coop_left",
        "outside_chicken_coop_right",
        "outside_chicken_coop_up",
    ]
    
class OutsideChickenCoop3Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_chicken_coop"
    _NAMED_REGIONS = [
        "outside_chicken_coop",
        "outside_chicken_coop",
        "outside_chicken_coop",
    ]
    _TARGET_NAMES = [
        "outside_chicken_coop_left",
        "outside_chicken_coop_right",
        "outside_chicken_coop_up",
    ]
    
class CowBarnTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom"
    _TERMINATION_TARGET_NAME = "cow_barn_entrance"

class OutsideCowBarnSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_cow_barn"
    _NAMED_REGIONS = [
        "screen_middle",
        "screen_middle",
        "screen_middle",
    ]
    _TARGET_NAMES = [
        "outside_cow_barn_left",
        "outside_cow_barn_right",
        "outside_cow_barn_up",
    ]

class OutsideCowBarn2Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_cow_barn"
    _NAMED_REGIONS = [
        "outside_barns",
        "outside_barns",
        "outside_barns",
    ]
    _TARGET_NAMES = [
        "outside_cow_barn_left",
        "outside_cow_barn_right",
        "outside_cow_barn_up",
    ]

class StorageTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom"
    _TERMINATION_TARGET_NAME = "storage_shed_entrance"

class OutsideStorageSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_storage_shed"
    _NAMED_REGIONS = [
        "screen_middle",
        "screen_middle",
        "screen_middle",
    ]
    _TARGET_NAMES = [
        "outside_storage_left",
        "outside_storage_right",
        "outside_storage_up",
    ]
    
class PickupWaterCanTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_top"
    _TERMINATION_TARGET_NAME = "pick_up_watercan"

class NextToWaterCanSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_water_can"
    _NAMED_REGIONS = [
        "item_watercan_above",
        "item_watercan_right",
        "item_watercan_below",
    ]
    _TARGET_NAMES = [
        "pickup_watercan_down",
        "pickup_watercan_left",
        "pickup_watercan_up",
    ]
    
class PickupCowBellTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_top_mid"
    _TERMINATION_TARGET_NAME = "pick_up_cowbell"

class NextToCowBellSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_cowbell"
    _NAMED_REGIONS = [
        "item_cowbell_above",
        "item_cowbell_below",
    ]
    _TARGET_NAMES = [
        "next_to_cowbell_down",
        "next_to_cowbell_up",
    ]

class PickupSickleTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_top_mid"
    _TERMINATION_TARGET_NAME = "pick_up_sickle"

class NextToSickleSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_sickle"
    _NAMED_REGIONS = [
        "item_sickle_above",
        "item_sickle_left",
        "item_sickle_below",
    ]
    _TARGET_NAMES = [
        "pickup_sickle_down",
        "pickup_sickle_right",
        "pickup_sickle_up",
    ]

class PickupHoeTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_top_short"
    _TERMINATION_TARGET_NAME = "pick_up_hoe"

class NextToHoeSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_hoe"
    _NAMED_REGIONS = [
        "item_hoe_above",
        "item_hoe_below",
    ]
    _TARGET_NAMES = [
        "pickup_hoe_down",
        "pickup_hoe_up",
    ]

class PickupHammerTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_top_mid"
    _TERMINATION_TARGET_NAME = "pick_up_hammer"

class NextToHammerSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_hammer"
    _NAMED_REGIONS = [
        "item_hammer_above",
        "item_hammer_below",
    ]
    _TARGET_NAMES = [
        "pickup_hammer_down",
        "pickup_hammer_up",
    ]

class PickupGrassSeedTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_top"
    _TERMINATION_TARGET_NAME = "pick_up_grass_seed"

class NextToGrassSeedSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_grass_seed"
    _NAMED_REGIONS = [
        "item_grass_seed_above",
        "item_grass_seed_right",
        "item_grass_seed_below",
    ]
    _TARGET_NAMES = [
        "pickup_grass_seed_down",
        "pickup_grass_seed_left",
        "pickup_grass_seed_up",
    ]

class GoToSleepTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "item_bed"
    _TERMINATION_TARGET_NAME = "sleep_in_bed"
    
class SleepOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "sleep_option"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "choose_yes_for_sleep",
    ]
    
class FeedSpiritTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "fed_spirit"

class HelpSpiritEarthquakeTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "helped_spirit_earthquake"

class NextToSpiritSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_spirit"
    _NAMED_REGIONS = [
        "item_spirit_left",
        "item_spirit_below",
        "item_spirit_above",
    ]
    _TARGET_NAMES = [
        "feed_spirit_right",
        "feed_spirit_up",
        "feed_spirit_down",
    ]

class NextToEarthquakeSpiritSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_spirit_earthquake"
    _NAMED_REGIONS = [
        "item_spirit_left",
        "item_spirit_below",
        "item_spirit_above",
    ]
    _TARGET_NAMES = [
        "help_spirit_earthquake_right",
        "help_spirit_earthquake_up",
        "help_spirit_earthquake_down",
    ]

class WaterTurnipTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _OR_PAIRS = [
        ("turnip_center", "finish_watering_1"),
        ("turnip_center", "finish_watering_2"),
    ]

class NextToTurnipSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_turnip"
    _NAMED_REGIONS = ["turnip_top", "turnip_top"]
    _TARGET_NAMES = ["ready_to_water_1", "ready_to_water_2"]
    
class BuyMaterialTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_material"

class OutsideCarpenter1Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_carpenter"
    _NAMED_REGIONS = [
        "center_sign",
    ]
    _TARGET_NAMES = [
        "outside_carpenter",
    ]

class ShopForMaterialSubgoal(AnyRegionMatchSubGoal):
    NAME = "shop_for_material"
    _NAMED_REGIONS = [
        "screen_top_half",
    ]
    _TARGET_NAMES = [
        "in_carpenter",
    ]

class SelectMaterialSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_material"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_material",
    ]

class BuyChickenTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_chicken"

class OutsideAnimalShop1Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_animal_shop"
    _NAMED_REGIONS = [
        "center_sign",
    ]
    _TARGET_NAMES = [
        "outside_animal_shop",
    ]

class ShopForAnimalSubgoal(AnyRegionMatchSubGoal):
    NAME = "shop_for_animal"
    _NAMED_REGIONS = [
        "screen_top_half",
    ]
    _TARGET_NAMES = [
        "in_animal_shop",
    ]

class SelectChickenSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_chicken"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_chicken",
    ]

class SelectCowSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_cow"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_cow",
    ]

class BuyCowTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "bought_named_cow"

class SellChickenTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "sold_chicken"

class SelectSellingChickenSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_selling_chicken"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_selling_chicken",
    ]

# HM2 sell cow task
class SellCowTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "sold_cow"

class SelectSellingCowSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_selling_cow"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_selling_cow",
    ]

# HM2 get hothouse estimate task
class ShopForConstructionEstimatesSubgoal(AnyRegionMatchSubGoal):
    NAME = "shop_for_construction_estimates"
    _NAMED_REGIONS = ["screen_top_half"]
    _TARGET_NAMES = ["shop_for_construction_estimates"]

class SelectHothouseSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_hothouse"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["select_hothouse"]

class GetHothouseEstimateTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "hothouse_estimate"

class BuyCowBrushTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_cow_brush"

class BuySaddlebagTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_saddlebag"

class BuyMilkerTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_milker"

class OutsideToolShop1Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_tool_shop"
    _NAMED_REGIONS = [
        "center_sign",
    ]
    _TARGET_NAMES = [
        "outside_tool_shop",
    ]

class ShopForToolsSubgoal(AnyRegionMatchSubGoal):
    NAME = "shop_for_tools"
    _NAMED_REGIONS = [
        "screen_top_half",
    ]
    _TARGET_NAMES = [
        "in_tool_shop",
    ]

class SelectCowBrushSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_cow_brush"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_cow_brush",
    ]

class SelectSaddlebagSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_saddlebag"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_saddlebag",
    ]

class SelectMilkerSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_milker"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_milker",
    ]

class BuyRiceBallTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_rice_ball"
    
class OutsideRestaurantSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_restaurant"
    _NAMED_REGIONS = [
        "center_sign",
    ]
    _TARGET_NAMES = [
        "outside_restaurant",
    ]
    
class ShopForFoodSubgoal(AnyRegionMatchSubGoal):
    NAME = "shop_for_food"
    _NAMED_REGIONS = [
        "screen_top_half",
    ]
    _TARGET_NAMES = [
        "in_restaurant",
    ]
    
class SelectRiceBallSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_rice_ball"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_rice_ball",
    ]
    
class BuyRiceBallOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "buy_rice_ball_option"
    _NAMED_REGIONS = [
        "screen_bottom_half",
    ]
    _TARGET_NAMES = [
        "option_to_buy_rice_ball",
    ]

class BuyCroissantTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_croissant"

class SelectCroissantSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_croissant"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_croissant",
    ]

class BuyCroissantOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "buy_croissant_option"
    _NAMED_REGIONS = [
        "screen_bottom_half",
    ]
    _TARGET_NAMES = [
        "option_to_buy_croissant",
    ]

class BuyCakeTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_cake"

class SelectCakeSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_cake"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_cake",
    ]

class BuyCakeOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "buy_cake_option"
    _NAMED_REGIONS = [
        "screen_bottom_half",
    ]
    _TARGET_NAMES = [
        "option_to_buy_cake",
    ]

class OutsideJuiceBarSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_juice_bar"
    _NAMED_REGIONS = [
        "center_sign",
    ]
    _TARGET_NAMES = [
        "outside_juice_bar",
    ]

class ShopForJuiceSubgoal(AnyRegionMatchSubGoal):
    NAME = "shop_for_juice"
    _NAMED_REGIONS = [
        "screen_top_half",
    ]
    _TARGET_NAMES = [
        "in_juice_bar",
    ]

class BuyGrapeJuiceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_grape_juice"

class SelectGrapeJuiceSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_grape_juice"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_grape_juice",
    ]

class BuyGrapeJuiceOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "buy_grape_juice_option"
    _NAMED_REGIONS = [
        "screen_bottom_half",
    ]
    _TARGET_NAMES = [
        "option_to_buy_grape_juice",
    ]

class GoToChurchPrayTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "praying"

class OutsideChurchSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_church"
    _NAMED_REGIONS = [
        "center_sign",
    ]
    _TARGET_NAMES = [
        "outside_church",
    ]

class InsideChurchSubgoal(AnyRegionMatchSubGoal):
    NAME = "inside_church"
    _NAMED_REGIONS = [
        "screen_top_half",
    ]
    _TARGET_NAMES = [
        "in_church",
    ]

class PrayOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "choose_to_pray"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "option_to_pray",
    ]

class OpenStorageListTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "left_border_frame"
    _TERMINATION_TARGET_NAME = "open_storage_list"
    
class NextToStorageListSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_storage_list"
    _NAMED_REGIONS = [
        "item_storage_list",
    ]
    _TARGET_NAMES = [
        "next_to_storage_list",
    ]

class ReadFerrySignTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_ferry_sign"

class NextToFerrySignSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_ferry_sign"
    _NAMED_REGIONS = [
        "item_ferry_sign_above",
        "item_ferry_sign_left",
    ]
    _TARGET_NAMES = [
        "next_to_ferry_sign_down",
        "next_to_ferry_sign_right",
    ]

class FindSecretSavingsTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "found_secret_savings"

class NextToFireplaceSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_fireplace"
    _NAMED_REGIONS = [
        "item_fireplace_below",
    ]
    _TARGET_NAMES = [
        "next_to_fireplace_up",
    ]

class FindLuckyMoneyTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "found_lucky_money"

class NextToClockSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_clock"
    _NAMED_REGIONS = [
        "item_clock_below",
    ]
    _TARGET_NAMES = [
        "next_to_clock_up",
    ]

class FindRainyMoneyTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "found_rainy_money"

class NextToSafeSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_safe"
    _NAMED_REGIONS = [
        "item_safe_below",
        "item_safe_below",
    ]
    _TARGET_NAMES = [
        "next_to_safe_up",
        "next_to_safe_left",
    ]

class FindLostBirdTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "found_bird_for_friend"

class NextToLostBirdSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_lost_bird"
    _NAMED_REGIONS = [
        "item_lost_bird_below",
        "item_lost_bird_left",
        "item_lost_bird_right",
    ]
    _TARGET_NAMES = [
        "find_lost_bird_up",
        "find_lost_bird_right",
        "find_lost_bird_left",
    ]

class SpeakToBlueHairGirlTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "speaking_to_blue_hair_girl"
    
class NextToBlueHairGirlSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_blue_hair_girl"
    _NAMED_REGIONS = [
        "item_blue_hair_girl_below",
        "item_blue_hair_girl_left",
        "item_blue_hair_girl_right",
    ]
    _TARGET_NAMES = [
        "next_to_blue_hair_girl_up",
        "next_to_blue_hair_girl_right",
        "next_to_blue_hair_girl_left",
    ]
    
class SpeakToGoldenHairGirlTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "speaking_to_golden_hair_girl"

class NextToGoldenHairGirlSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_golden_hair_girl"
    _NAMED_REGIONS = [
        "item_golden_hair_girl_below",
        "item_golden_hair_girl_right",
        "item_golden_hair_girl_above",
    ]
    _TARGET_NAMES = [
        "next_to_golden_hair_girl_up",
        "next_to_golden_hair_girl_left",
        "next_to_golden_hair_girl_down",
    ]

class SpeakToPinkHairGirlTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "speaking_to_pink_hair_girl"

class NextToPinkHairGirlSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_pink_hair_girl"
    _NAMED_REGIONS = [
        "item_pink_hair_girl_above",
        "item_pink_hair_girl_left",
        "item_pink_hair_girl_right",
    ]
    _TARGET_NAMES = [
        "next_to_pink_hair_girl_down",
        "next_to_pink_hair_girl_right",
        "next_to_pink_hair_girl_left",
    ]

# HM1 winter gathering speak to girl tasks
class SpeakToBlueHairGirlWGTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "speaking_to_blue_hair_girl_wg"

class NextToBlueHairGirlWGSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_blue_hair_girl_wg"
    _NAMED_REGIONS = [
        "item_blue_hair_girl_wg_below",
        "item_blue_hair_girl_wg_left",
        "item_blue_hair_girl_wg_right",
    ]
    _TARGET_NAMES = [
        "next_to_blue_hair_girl_wg_up",
        "next_to_blue_hair_girl_wg_right",
        "next_to_blue_hair_girl_wg_left",
    ]

class SpeakToPinkHairGirlWGTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "speaking_to_pink_hair_girl_wg"

class NextToPinkHairGirlWGSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_pink_hair_girl_wg"
    _NAMED_REGIONS = [
        "item_pink_hair_girl_wg_above",
        "item_pink_hair_girl_wg_left",
        "item_pink_hair_girl_wg_right",
    ]
    _TARGET_NAMES = [
        "next_to_pink_hair_girl_wg_down",
        "next_to_pink_hair_girl_wg_right",
        "next_to_pink_hair_girl_wg_left",
    ]

class SpeakToRedHairGirlWGTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "speaking_to_red_hair_girl_wg"

class NextToRedHairGirlWGSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_red_hair_girl_wg"
    _NAMED_REGIONS = [
        "item_red_hair_girl_wg_above",
        "item_red_hair_girl_wg_left",
        "item_red_hair_girl_wg_right",
    ]
    _TARGET_NAMES = [
        "next_to_red_hair_girl_wg_down",
        "next_to_red_hair_girl_wg_right",
        "next_to_red_hair_girl_wg_left",
    ]

class FillChickenFodderBlock1TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "item_chicken_stall_block1"
    _TERMINATION_TARGET_NAME = "filled_chicken_stall_block1"
    
class NextToChickenFodderBlock1Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_chicken_stall_block1_with_fodder"
    _NAMED_REGIONS = [
        "item_next_to_chicken_stall_block1",
    ]
    _TARGET_NAMES = [
        "next_to_chicken_stall_block1",
    ]
    
class NextToChickenSiloSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_chicken_silo"
    _NAMED_REGIONS = [
        "item_chicken_silo_left",
        "item_chicken_silo_below1",
        "item_chicken_silo_below2",
    ]
    _TARGET_NAMES = [
        "next_to_chicken_silo_right",
        "next_to_chicken_silo_up1",
        "next_to_chicken_silo_up2",
    ]

class PickupChickenFodderSubgoal(AnyRegionMatchSubGoal):
    NAME = "picked_up_chicken_fodder_from_silo"
    _NAMED_REGIONS = [
        "item_chicken_silo_left",
        "item_chicken_silo_below1",
        "item_chicken_silo_below2",
    ]
    _TARGET_NAMES = [
        "got_fodder_from_chicken_silo_right",
        "got_fodder_from_chicken_silo_up1",
        "got_fodder_from_chicken_silo_up2",
    ]

# HM1 fill cow fodder task
class NextToCowFeedingStallSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_cow_feeding_stall_with_fodder"
    _NAMED_REGIONS = [
        "item_cow_feeding_stall_right",
    ]
    _TARGET_NAMES = [
        "next_to_cow_feeding_stall_left",
    ]

class FillUpperRightCowStallTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_cow_feeding_stall"
    _TERMINATION_TARGET_NAME = "cow_feeding_stall_filled"

# HM2 fill chicken fodder subgoals
class NextToChickenSilo2Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_chicken_silo"
    _NAMED_REGIONS = [
        "item_chicken_silo_left1",
        "item_chicken_silo_left2",
        "item_chicken_silo_below",
    ]
    _TARGET_NAMES = [
        "next_to_chicken_silo_right1",
        "next_to_chicken_silo_right2",
        "next_to_chicken_silo_up",
    ]

class PickupChickenFodder2Subgoal(AnyRegionMatchSubGoal):
    NAME = "picked_up_chicken_fodder_from_silo"
    _NAMED_REGIONS = [
        "item_chicken_silo_left1",
        "item_chicken_silo_left2",
        "item_chicken_silo_below",
    ]
    _TARGET_NAMES = [
        "got_fodder_from_chicken_silo_right1",
        "got_fodder_from_chicken_silo_right2",
        "got_fodder_from_chicken_silo_up",
    ]


class HospitalEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "screen_top_half"
    _TERMINATION_TARGET_NAME = "in_hospital"

class OutsideHospitalSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_hospital"
    _NAMED_REGIONS = [
        "hospital_location",
        "hospital_location",
        "hospital_location",
    ]
    _TARGET_NAMES = [
        "outside_hospital_up",
        "outside_hospital_left",
        "outside_hospital_right",
    ]

class ToolShopEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "screen_top_half"
    _TERMINATION_TARGET_NAME = "in_tool_shop"

class OutsideToolShop2Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_tool_shop"
    _NAMED_REGIONS = [
        "tool_shop_location",
        "tool_shop_location",
        "tool_shop_location",
    ]
    _TARGET_NAMES = [
        "outside_tool_shop_up",
        "outside_tool_shop_left",
        "outside_tool_shop_right",
    ]

class CarpenterEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "screen_top_half"
    _TERMINATION_TARGET_NAME = "in_carpenter"

class OutsideCarpenter2Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_carpenter"
    _NAMED_REGIONS = [
        "carpenter_location",
        "carpenter_location",
        "carpenter_location",
    ]
    _TARGET_NAMES = [
        "outside_carpenter_up",
        "outside_carpenter_left",
        "outside_carpenter_right",
    ]

class AnimalShopEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "screen_top_half"
    _TERMINATION_TARGET_NAME = "in_animal_shop"

class OutsideAnimalShop2Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_animal_shop"
    _NAMED_REGIONS = [
        "animal_shop_location",
        "animal_shop_location",
        "animal_shop_location",
    ]
    _TARGET_NAMES = [
        "outside_animal_shop_up",
        "outside_animal_shop_left",
        "outside_animal_shop_right",
    ]

class LibraryEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "screen_top_half"
    _TERMINATION_TARGET_NAME = "in_library"

class OutsideLibrarySubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_library"
    _NAMED_REGIONS = [
        "library_location",
        "library_location",
        "library_location",
    ]
    _TARGET_NAMES = [
        "outside_library_up",
        "outside_library_left",
        "outside_library_right",
    ]

class FlowerShopEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_top_half"
    _TERMINATION_TARGET_NAME = "in_flower_shop"

class OutsideFlowerShop2Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_flower_shop"
    _NAMED_REGIONS = [
        "flower_shop_location",
        "flower_shop_location",
        "flower_shop_location",
    ]
    _TARGET_NAMES = [
        "outside_flower_shop_up",
        "outside_flower_shop_left",
        "outside_flower_shop_right",
    ]


class SelectBridgeSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_bridge"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["select_bridge"]

class GetBridgeEstimateTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bridge_estimate"


class RestaurantEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_top_half"
    _TERMINATION_TARGET_NAME = "in_restaurant"

class OutsideRestaurant2Subgoal(AnyRegionMatchSubGoal):
    NAME = "outside_restaurant"
    _NAMED_REGIONS = [
        "restaurant_location",
        "restaurant_location",
        "restaurant_location",
    ]
    _TARGET_NAMES = [
        "outside_restaurant_up",
        "outside_restaurant_left",
        "outside_restaurant_right",
    ]

class BuyLunchSetTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_lunch_set"

class SelectLunchSetSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_lunch_set"
    _NAMED_REGIONS = [
        "screen_bottom_half",
    ]
    _TARGET_NAMES = [
        "select_lunch_set",
    ]

class BuyLunchSetOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "buy_lunch_set_option"
    _NAMED_REGIONS = [
        "screen_bottom_half",
    ]
    _TARGET_NAMES = [
        "option_to_buy_lunch_set",
    ]

class BuyBeverageSetTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_beverage_set"

class SelectBeverageSetSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_beverage_set"
    _NAMED_REGIONS = [
        "screen_bottom_half",
    ]
    _TARGET_NAMES = [
        "select_beverage_set",
    ]

class BuyBeverageSetOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "buy_beverage_set_option"
    _NAMED_REGIONS = [
        "screen_bottom_half",
    ]
    _TARGET_NAMES = [
        "option_to_buy_beverage_set",
    ]

class BuyTodaysSpecialTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "bought_todays_special"

class SelectTodaysSpecialSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_todays_special"
    _NAMED_REGIONS = [
        "screen_bottom_half",
    ]
    _TARGET_NAMES = [
        "select_todays_special",
    ]

class BuyTodaysSpecialOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "buy_todays_special_option"
    _NAMED_REGIONS = [
        "screen_bottom_half",
    ]
    _TARGET_NAMES = [
        "option_to_buy_todays_special",
    ]

# TO DO
class ReadNoticeBoardTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_notice_board"

class NextToNoticeBoardSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_notice_board"
    _NAMED_REGIONS = [
        "item_notice_board_above",
        "item_notice_board_left",
        "item_notice_board_right",
    ]
    _TARGET_NAMES = [
        "next_to_notice_board_down",
        "next_to_notice_board_right",
        "next_to_notice_board_left",
    ]

class ReadVillageSignTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_village_sign"

class NextToVillageSignSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_village_sign"
    _NAMED_REGIONS = [
        "item_village_sign_above",
        "item_village_sign_left",
        "item_village_sign_right",
    ]
    _TARGET_NAMES = [
        "next_to_village_sign_down",
        "next_to_village_sign_right",
        "next_to_village_sign_left",
    ]

class ReadFarmSignTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_farm_sign"

class NextToFarmSignSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_farm_sign"
    _NAMED_REGIONS = [
        "item_farm_sign_above",
        "item_farm_sign_left",
        "item_farm_sign_right",
    ]
    _TARGET_NAMES = [
        "next_to_farm_sign_down",
        "next_to_farm_sign_right",
        "next_to_farm_sign_left",
    ]

class ReadSecretGardenSignTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_secret_garden_sign"

class NextToSecretGardenSignSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_secret_garden_sign"
    _NAMED_REGIONS = [
        "item_secret_garden_sign_above",
        "item_secret_garden_sign_right",
        "item_secret_garden_sign_left",
    ]
    _TARGET_NAMES = [
        "next_to_secret_garden_sign_down",
        "next_to_secret_garden_sign_left",
        "next_to_secret_garden_sign_right",
    ]

class ReadCropFieldSignTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_crop_field_sign"

class NextToCropFieldSignSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_crop_field_sign"
    _NAMED_REGIONS = [
        "item_crop_field_sign_above",
    ]
    _TARGET_NAMES = [
        "next_to_crop_field_sign_down",
    ]

class NextToDiarySubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_diary"
    _NAMED_REGIONS = [
        "item_diary",
    ]
    _TARGET_NAMES = [
        "next_to_diary",
    ]

class DiaryOptionSubgoal(AnyRegionMatchSubGoal):
    NAME = "diary_sleep_option"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "option_to_diary_sleep",
    ]
    

class OpenMenuTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "screen"
    _TERMINATION_TARGET_NAME = "menu_open"

# HM2 equip tool tasks
class EmptyHandsSelectedSubgoal(AnyRegionMatchSubGoal):
    NAME = "empty_hands_selected"
    _NAMED_REGIONS = ["equipment_region_4"]
    _TARGET_NAMES = ["empty_hands_selected"]

class ReadyToPickSickleSubgoal(AnyRegionMatchSubGoal):
    NAME = "ready_to_pick_sickle"
    _NAMED_REGIONS = ["top_left_label"]
    _TARGET_NAMES = ["ready_to_pick_sickle"]

class EquipSickleTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "equipment_region_4"
    _TERMINATION_TARGET_NAME = "sickle_equipped"

class ReadyToPickHammerSubgoal(AnyRegionMatchSubGoal):
    NAME = "ready_to_pick_hammer"
    _NAMED_REGIONS = ["top_left_label"]
    _TARGET_NAMES = ["ready_to_pick_hammer"]

class EquipHammerTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "equipment_region_4"
    _TERMINATION_TARGET_NAME = "hammer_equipped"

class ReadyToPickFishingRodSubgoal(AnyRegionMatchSubGoal):
    NAME = "ready_to_pick_fishing_rod"
    _NAMED_REGIONS = ["top_left_label"]
    _TARGET_NAMES = ["ready_to_pick_fishing_rod"]

class EquipFishingRodTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "equipment_region_4"
    _TERMINATION_TARGET_NAME = "fishing_rod_equipped"

class AxeSelected2Subgoal(AnyRegionMatchSubGoal):
    NAME = "axe_selected_2"
    _NAMED_REGIONS = ["equipment_region_2"]
    _TARGET_NAMES = ["ax_selected_2"]

class ReadyToPickNetSubgoal(AnyRegionMatchSubGoal):
    NAME = "ready_to_pick_net"
    _NAMED_REGIONS = ["top_left_label"]
    _TARGET_NAMES = ["ready_to_pick_net"]

class EquipNetReplacingAxTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "equipment_region_2"
    _TERMINATION_TARGET_NAME = "net_equipped"

class ReadyToPickRosemarySeedsSubgoal(AnyRegionMatchSubGoal):
    NAME = "ready_to_pick_rosemary_seeds"
    _NAMED_REGIONS = ["top_left_label"]
    _TARGET_NAMES = ["ready_to_pick_rosemary_seeds"]

class EquipRosemarySeedsReplacingAxTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "equipment_region_2"
    _TERMINATION_TARGET_NAME = "rosemary_seeds_equipped"

class SprinklerSelected1Subgoal(AnyRegionMatchSubGoal):
    NAME = "sprinkler_selected_1"
    _NAMED_REGIONS = ["equipment_region_1"]
    _TARGET_NAMES = ["sprinkler_selected_1"]

class EquipSickleReplacingSprinklerTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "equipment_region_1"
    _TERMINATION_TARGET_NAME = "sickle_equipped_1"

class HoeSelected3Subgoal(AnyRegionMatchSubGoal):
    NAME = "hoe_selected_3"
    _NAMED_REGIONS = ["equipment_region_3"]
    _TARGET_NAMES = ["hoe_selected_3"]

class EquipNetReplacingHoeTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "equipment_region_3"
    _TERMINATION_TARGET_NAME = "net_equipped_3"

# HM1 pick up egg task
class NextToEggSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_egg"
    _NAMED_REGIONS = ["item_egg_left", "item_egg_above", "item_egg_right"]
    _TARGET_NAMES = ["next_to_egg_right", "next_to_egg_down", "next_to_egg_left"]

# HM1 hatch egg task
class HatchEggTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_hatching_box"
    _TERMINATION_TARGET_NAME = "dropped_egg_into_hatching_box"

# HM1 break rock task
class NextToRockFromLeftSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_rock_from_left"
    _NAMED_REGIONS = ["item_rock_left"]
    _TARGET_NAMES = ["next_to_rock_right"]

class BreakRockTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_rock_left"
    _TERMINATION_TARGET_NAME = "rock_cleared"

class NextToRightmostRockAboveSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_rightmost_rock_above"
    _NAMED_REGIONS = ["item_rightmost_rock_above"]
    _TARGET_NAMES = ["next_to_rightmost_rock_down"]

class BreakRightmostRockTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_rightmost_rock_above"
    _TERMINATION_TARGET_NAME = "rightmost_rock_cleared"

# HM1 weed removal tasks
class NextToTopLeftWeedFromRightSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_top_left_weed"
    _NAMED_REGIONS = ["item_top_left_weed"]
    _TARGET_NAMES = ["next_to_top_left_weed_up"]

class RemoveTopLeftWeedTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_top_left_weed"
    _TERMINATION_TARGET_NAME = "top_left_weed_removed"

class CutTopLeftWeedTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_top_left_weed"
    _TERMINATION_TARGET_NAME = "top_left_weed_cut"

class NextToLowestWeedFromAboveSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_lowest_weed_from_above"
    _NAMED_REGIONS = ["item_weed_above"]
    _TARGET_NAMES = ["next_to_lowest_weed_down"]

class RemoveLowestWeedTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_weed_above"
    _TERMINATION_TARGET_NAME = "lowest_weed_removed"

class CutLowestWeedTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_weed_above"
    _TERMINATION_TARGET_NAME = "lowest_weed_cut"

# HM1 harvest center grassline task
class NextToGrasslandFromLeftSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_grassland_right"
    _NAMED_REGIONS = ["item_grassland_right"]
    _TARGET_NAMES = ["next_to_grassland_left"]

class HarvestCenterGrasslineTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_center_grassline", "center_grass_harvested_1"),
        ("item_center_grassline", "center_grass_harvested_2"),
    ]

# HM1 restore fence task
class PickedUpBrokenFenceSubgoal(AnyRegionMatchSubGoal):
    NAME = "picked_up_broken_fence"
    _NAMED_REGIONS = [
        "item_broken_fence_field",
        "item_broken_fence_field",
        "item_broken_fence_field",
        "item_broken_fence_field",
    ]
    _TARGET_NAMES = [
        "picked_up_broken_fence_up",
        "picked_up_broken_fence_down",
        "picked_up_broken_fence_left",
        "picked_up_broken_fence_right",
    ]

class RestoreFenceTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_fence_field", "restored_fence"),
    ]

# HM1 harvest turnip task
class NextToCenterTurnipSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_turnip"
    _NAMED_REGIONS = ["item_turnip_field", "item_turnip_field"]
    _TARGET_NAMES = ["next_to_center_turnip_down_1", "next_to_center_turnip_down_2"]

class HarvestCenterTurnipTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_turnip_field", "center_turnip_harvested_1"),
        ("item_turnip_field", "center_turnip_harvested_2"),
    ]

class NextToCenterTurnipLeftSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_turnip_left"
    _NAMED_REGIONS = ["item_turnip_field_water", "item_turnip_field_water"]
    _TARGET_NAMES = ["next_to_center_turnip_left_1", "next_to_center_turnip_left_2"]

class WaterCenterTurnipTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_turnip_field_water", "center_turnip_watered_1"),
        ("item_turnip_field_water", "center_turnip_watered_2"),
    ]

# HM2 harvest eggplant task
class NextToCenterEggplantSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_eggplant"
    _NAMED_REGIONS = ["item_eggplant_field", "item_eggplant_field"]
    _TARGET_NAMES = ["next_to_center_eggplant_up_1", "next_to_center_eggplant_up_2"]

class HarvestCenterEggplantTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_eggplant_field", "center_eggplant_harvested_1"),
        ("item_eggplant_field", "center_eggplant_harvested_2"),
    ]

class NextToCenterPotatoSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_potato"
    _NAMED_REGIONS = ["item_potato_field", "item_potato_field"]
    _TARGET_NAMES = ["next_to_center_potato_up_1", "next_to_center_potato_up_2"]

class WaterCenterPotatoTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_potato_field", "center_potato_watered_1"),
        ("item_potato_field", "center_potato_watered_2"),
    ]

class NextToCenterPotatoBelowSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_potato_below"
    _NAMED_REGIONS = ["item_potato_field", "item_potato_field"]
    _TARGET_NAMES = ["next_to_center_potato_below_up_1", "next_to_center_potato_below_up_2"]

class HarvestCenterPotatoTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_potato_field", "center_potato_harvested_1"),
        ("item_potato_field", "center_potato_harvested_2"),
    ]

class NextToCenterAsparagusSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_asparagus"
    _NAMED_REGIONS = ["item_asparagus_field", "item_asparagus_field"]
    _TARGET_NAMES = ["next_to_center_asparagus_right_1", "next_to_center_asparagus_right_2"]

class WaterCenterAsparagusTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_asparagus_field", "center_asparagus_watered_1"),
        ("item_asparagus_field", "center_asparagus_watered_2"),
    ]

# HM2 water corn field task
class AtCornCenterSubgoal(AnyRegionMatchSubGoal):
    NAME = "at_corn_center"
    _NAMED_REGIONS = ["item_corn_field", "item_corn_field"]
    _TARGET_NAMES = ["at_corn_center_1", "at_corn_center_2"]

class WaterCornFieldTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_corn_field", "corn_field_watered_1"),
        ("item_corn_field", "corn_field_watered_2"),
    ]

# HM2 water cabbage field task
class AtCabbageCenterSubgoal(AnyRegionMatchSubGoal):
    NAME = "at_cabbage_center"
    _NAMED_REGIONS = ["item_cabbage_field", "item_cabbage_field"]
    _TARGET_NAMES = ["at_cabbage_center_1", "at_cabbage_center_2"]

class WaterCabbageFieldTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_cabbage_field", "cabbage_field_watered_1"),
        ("item_cabbage_field", "cabbage_field_watered_2"),
    ]

# HM2 cut center corn task
class NextToCenterCornSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_corn"
    _NAMED_REGIONS = ["item_center_corn_above", "item_center_corn_above"]
    _TARGET_NAMES = ["next_to_center_corn_down_1", "next_to_center_corn_down_2"]

class CutCenterCornTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_center_corn_above", "center_corn_cut_1"),
        ("item_center_corn_above", "center_corn_cut_2"),
    ]

class NextToCenterCarrotSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_carrot"
    _NAMED_REGIONS = ["item_carrot_field", "item_carrot_field"]
    _TARGET_NAMES = ["next_to_center_carrot_up_1", "next_to_center_carrot_up_2"]

class HarvestCenterCarrotTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_carrot_field", "center_carrot_harvested_1"),
        ("item_carrot_field", "center_carrot_harvested_2"),
    ]

# HM2 ship eggplant task
class NextToShippingBoxSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_shipping_box"
    _NAMED_REGIONS = ["item_next_to_shipping_box"]
    _TARGET_NAMES = ["next_to_shipping_box_up"]

class ShipEggplantTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_shipping_box_field"
    _TERMINATION_TARGET_NAME = "drop_eggplant_into_shipping_box"

# HM2 cherry cup race task
class AtTheStartLineSubgoal(AnyRegionMatchSubGoal):
    NAME = "at_the_start_line"
    _NAMED_REGIONS = ["item_start_line"]
    _TARGET_NAMES = ["at_the_start_line"]

class Cross500mLineTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_distance_markers"
    _TERMINATION_TARGET_NAME = "crossed_500m_line"

class Cross1000mLineTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_distance_markers"
    _TERMINATION_TARGET_NAME = "crossed_1000m_line"

# HM2 billboard article tasks
class ComputersArticleSelectedSubgoal(AnyRegionMatchSubGoal):
    NAME = "computers_article_selected"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["computers_article_selected"]

class ReadComputersArticleTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_computers_article"

class BouldersArticleSelectedSubgoal(AnyRegionMatchSubGoal):
    NAME = "boulders_article_selected"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["boulders_article_selected"]

class ReadBouldersArticleTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_boulders_article"

class CropsArticleSelectedSubgoal(AnyRegionMatchSubGoal):
    NAME = "selling_crops_article_selected"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["crops_article_selected"]

class ReadCropsArticleTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_crops_article"

# HM2 weed tasks
class NextToLeftmostWeedSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_leftmost_weed"
    _NAMED_REGIONS = [
        "item_leftmost_weed_right",
        "item_leftmost_weed_above",
    ]
    _TARGET_NAMES = [
        "next_to_leftmost_weed_left",
        "next_to_leftmost_weed_down",
    ]

class RemoveLeftmostWeedTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_leftmost_weed_right", "leftmost_weed_removed_left"),
        ("item_leftmost_weed_above", "leftmost_weed_removed_down"),
    ]

# HM2 pick berry task
class NextToBerrySubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_berry"
    _NAMED_REGIONS = [
        "item_berry_left",
    ]
    _TARGET_NAMES = [
        "next_to_berry_right",
    ]

class PickBerryTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_berry_left", "berry_picked_right"),
    ]

class NextToBerryAboveSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_berry_above"
    _NAMED_REGIONS = [
        "item_berry_above",
        "item_berry_above",
    ]
    _TARGET_NAMES = [
        "next_to_berry_down_1",
        "next_to_berry_down_2",
    ]

class PickBerryAboveTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_berry_above", "berry_picked_above_1"),
        ("item_berry_above", "berry_picked_above_2"),
    ]

# HM2 speak to girl tasks
class NextToBlueHairGirl2Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_blue_hair_girl"
    _NAMED_REGIONS = [
        "npc_blue_hair_girl_left",
        "npc_blue_hair_girl_below",
        "npc_blue_hair_girl_right",
    ]
    _TARGET_NAMES = [
        "next_to_blue_hair_girl_right",
        "next_to_blue_hair_girl_up",
        "next_to_blue_hair_girl_left",
    ]

class SpeakToBlueHairGirl2TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "speaking_to_blue_hair_girl"

class NextToPurpleHairGirlSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_purple_hair_girl"
    _NAMED_REGIONS = [
        "npc_purple_hair_girl_left",
        "npc_purple_hair_girl_below",
    ]
    _TARGET_NAMES = [
        "next_to_purple_hair_girl_right",
        "next_to_purple_hair_girl_up",
    ]

class SpeakToPurpleHairGirlTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "speaking_to_purple_hair_girl"

class NextToBlondeGirlSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_blonde_girl"
    _NAMED_REGIONS = [
        "npc_blonde_girl_right",
        "npc_blonde_girl_above",
    ]
    _TARGET_NAMES = [
        "next_to_blonde_girl_left",
        "next_to_blonde_girl_down",
    ]

class SpeakToBlondeGirlTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "speaking_to_blonde_girl"

# HM2 hatch egg task
class HarvestMoon2NextToHatchingBoxSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_hatching_box"
    _NAMED_REGIONS = ["item_next_to_hatching_box"]
    _TARGET_NAMES = ["next_to_hatching_box"]

class HarvestMoon2HatchEggTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_hatching_box"
    _TERMINATION_TARGET_NAME = "dropped_egg_into_hatching_box"

## HM3
class NextToSecretGardenSign3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_secret_garden_sign"
    _NAMED_REGIONS = [
        "item_secret_garden_sign_above",
        "item_secret_garden_sign_right",
    ]
    _TARGET_NAMES = [
        "next_to_secret_garden_sign_down",
        "next_to_secret_garden_sign_left",
    ]

class BuyPotatoSeeds3TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "select_potato_seeds"

class NextToPotatoSeeds3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_potato_seeds"
    _NAMED_REGIONS = ["item_potato_seeds_above", "item_potato_seeds_below"]
    _TARGET_NAMES = ["next_to_potato_seeds_down", "next_to_potato_seeds_up"]

class ChooseTea3TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "select_tea"

class NextToTea3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_tea"
    _NAMED_REGIONS = ["item_tea_above", "item_tea_below"]
    _TARGET_NAMES = ["next_to_tea_down", "next_to_tea_up"]

class ChooseAsparagusSeedsTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "select_asparagus_seeds"

class NextToAsparagusSeeds3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_asparagus_seeds"
    _NAMED_REGIONS = ["item_asparagus_seeds_above", "item_asparagus_seeds_below"]
    _TARGET_NAMES = ["next_to_asparagus_seeds_down", "next_to_asparagus_seeds_up"]

class NextToTurnipSeeds3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_turnip_seeds"
    _NAMED_REGIONS = ["item_turnip_seeds_above", "item_turnip_seeds_below"]
    _TARGET_NAMES = ["next_to_turnip_seeds_down", "next_to_turnip_seeds_up"]

class BuyTurnipSeeds3TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "select_turnip_seeds"

class ReadMorningMarketSignTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_morning_market_sign"

class NextToMorningMarketSignSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_morning_market_sign"
    _NAMED_REGIONS = [
        "item_morning_market_sign_left",
    ]
    _TARGET_NAMES = [
        "next_to_morning_market_sign_right",
    ]

class ReadStorageSignTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "reading_storage_sign"

class NextToStorageSign3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_storage_sign"
    _NAMED_REGIONS = [
        "item_storage_sign_below",
        "item_storage_sign_left",
        "item_storage_sign_right",
    ]
    _TARGET_NAMES = [
        "next_to_storage_sign_up",
        "next_to_storage_sign_right",
        "next_to_storage_sign_left",
    ]

class SpeakToKirkVillageTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_upper_border"
    _TERMINATION_TARGET_NAME = "speaking_to_kirk_village"

class NextToKirkVillageSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_kirk_village"
    _NAMED_REGIONS = [
        "npc_kirk_above",
    ]
    _TARGET_NAMES = [
        "next_to_kirk_down",
    ]

class TakeFerryTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "village_ferry_entrance"

class NextToKirkMainlandSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_kirk_mainland"
    _NAMED_REGIONS = [
        "npc_kirk_mainland_right",
        "npc_kirk_mainland_below",
    ]
    _TARGET_NAMES = [
        "next_to_kirk_mainland_left",
        "next_to_kirk_mainland_up",
    ]

class SpeakToJoeTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_upper_border"
    _TERMINATION_TARGET_NAME = "speaking_to_joe"

class NextToJoeSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_joe"
    _NAMED_REGIONS = [
        "npc_joe_left",
    ]
    _TARGET_NAMES = [
        "next_to_joe_right",
    ]

class SpeakToLukiaTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_upper_border"
    _TERMINATION_TARGET_NAME = "speaking_to_lukia"

class NextToLukiaSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_Lukia"
    _NAMED_REGIONS = [
        "npc_lukia_right",
    ]
    _TARGET_NAMES = [
        "next_to_lukia_left",
    ]

class SpeakToLucusTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_upper_border"
    _TERMINATION_TARGET_NAME = "speaking_to_lucus"

class NextToLucusSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_lucus"
    _NAMED_REGIONS = [
        "npc_lucus_above",
        "npc_lucus_left",
        "npc_lucus_right",
    ]
    _TARGET_NAMES = [
        "next_to_lucus_down",
        "next_to_lucus_right",
        "next_to_lucus_left",
    ]

class SpeakToLylaTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_upper_border"
    _TERMINATION_TARGET_NAME = "speaking_to_lyla"

class NextToLylaSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_lyla"
    _NAMED_REGIONS = [
        "npc_lyla_right",
    ]
    _TARGET_NAMES = [
        "next_to_lyla_left",
    ]

class BuyHorseSaddleTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _OR_PAIRS = [
        ("item_horse_saddle_empty_1", "bought_horse_saddle_1"),
        ("item_horse_saddle_empty_2", "bought_horse_saddle_2"),
    ]

class NextToHorseSaddleSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_horse_saddle"
    _NAMED_REGIONS = ["item_horse_saddle_above", "item_horse_saddle_below"]
    _TARGET_NAMES = ["next_to_horse_saddle_down", "next_to_horse_saddle_up"]

class BuyFlowerVaseTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _OR_PAIRS = [
        ("item_flower_vase_empty_1", "bought_flower_vase_1"),
        ("item_flower_vase_empty_2", "bought_flower_vase_2"),
    ]
    _ALL_PAIRS = [
        ("dialogue_box_bottom", "bought_from_flower_shop"),
    ]

class NextToVaseSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_vase"
    _NAMED_REGIONS = ["item_flower_vase_above", "item_flower_vase_below"]
    _TARGET_NAMES = ["next_to_vase_down", "next_to_vase_up"]

class BuyMealSetTerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _OR_PAIRS = [
        ("item_meal_set_empty_1", "bought_meal_set_1"),
        ("item_meal_set_empty_2", "bought_meal_set_2"),
    ]

class SelectMealSetSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_meal_set"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_meal_set",
    ]

class BuyCoffeeTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "select_coffee"

class NextToCoffeeSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_coffee"
    _NAMED_REGIONS = [
        "item_coffee_above",
        "item_coffee_below",
    ]
    _TARGET_NAMES = [
        "next_to_coffee_down",
        "next_to_coffee_up",
    ]

class SelectCoffeeSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_coffee"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "select_coffee",
    ]

class NextToWeed3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_weed"
    _NAMED_REGIONS = ["item_weed_left"]
    _TARGET_NAMES = ["next_to_weed_right"]

class RemoveWeed3TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_weed_left"
    _TERMINATION_TARGET_NAME = "weed_removed"

class NextToCherrySubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_cherry"
    _NAMED_REGIONS = ["item_cherry_left"]
    _TARGET_NAMES = ["next_to_cherry_right"]

class PickUpCherry3TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_cherry_left"
    _TERMINATION_TARGET_NAME = "cherry_picked"

class SpeakToKateTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "speaking_to_kate"

class NextToKateSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_kate"
    _NAMED_REGIONS = [
        "npc_kate_left",
        "npc_kate_right",
        "npc_kate_below",
    ]
    _TARGET_NAMES = [
        "next_to_kate_right",
        "next_to_kate_left",
        "next_to_kate_up",
    ]

class NextToCenterSPotatoSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_spotato"
    _NAMED_REGIONS = ["item_center_spotato_above"]
    _TARGET_NAMES = ["next_to_spotato_down"]

class WaterCenterSPotato3TerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_center_spotato_above", "center_spotato_watered"),
    ]

class NextToCenterWatermelonSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_watermelon"
    _NAMED_REGIONS = ["item_center_watermelon_above"]
    _TARGET_NAMES = ["next_to_center_watermelon_down"]

class WaterCenterWatermelon3TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_center_watermelon_above"
    _TERMINATION_TARGET_NAME = "center_watermelon_watered"

class NextToTargetPotatoBelowSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_target_potato_below"
    _NAMED_REGIONS = ["item_target_potato_below"]
    _TARGET_NAMES = ["next_to_target_potato_up"]

class HarvestTargetPotato3TerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_target_potato_below", "target_potato_harvested"),
    ]

# HM3 harvest center eggplant top 3x3 field task
class NextToCenterEggplantTopSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_eggplant"
    _NAMED_REGIONS = ["item_center_eggplant_above", "item_center_eggplant_left"]
    _TARGET_NAMES = ["next_to_eggplant_down", "next_to_eggplant_right"]

class HarvestCenterEggplantTop3TerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _OR_PAIRS = [
        ("item_center_eggplant_above", "center_eggplant_harvested_down"),
        ("item_center_eggplant_left", "center_eggplant_harvested_right"),
    ]

class NextToBookshelfSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_bookshelf"
    _NAMED_REGIONS = ["item_bookshelf_below"]
    _TARGET_NAMES = ["next_to_bookshelf_up"]

class ReadAnimalCh2TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "dialogue_box_bottom"
    _TERMINATION_TARGET_NAME = "finish_animal_ch2"

# HM3 harvest center turnip task
class NextToCenterTurnip3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_center_turnip_below"
    _NAMED_REGIONS = ["item_center_turnip_below"]
    _TARGET_NAMES = ["next_to_center_turnip_up"]

class HarvestCenterTurnip3TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_center_turnip_below"
    _TERMINATION_TARGET_NAME = "center_turnip_harvested"

class NextToSellChicken3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_sell_chicken"
    _NAMED_REGIONS = ["item_sell_chicken_below", "item_sell_chicken_above"]
    _TARGET_NAMES = ["next_to_sell_chicken_up", "next_to_sell_chicken_down"]

class SellChicken3TerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _OR_PAIRS = [
        ("sell_animal_section_1", "selling_animal_1"),
        ("sell_animal_section_2", "selling_animal_2"),
    ]
    _ALL_PAIRS = [
        ("dialogue_box_bottom", "animal_sold"),
    ]

class NextToBerry3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_berry_above"
    _NAMED_REGIONS = ["item_berry_above"]
    _TARGET_NAMES = ["next_to_berry_down"]

class PickBerry3TerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_berry_above"
    _TERMINATION_TARGET_NAME = "berry_picked_above"

class CheckPlayerMoneySubgoal(AnyRegionMatchSubGoal):
    NAME = "choose_may"
    _NAMED_REGIONS = ["menu_box"]
    _TARGET_NAMES = ["choose_may"]

class CheckPlayerMoneyTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "player_top_left"
    _TERMINATION_TARGET_NAME = "display_player_status"

class FillCowFodderBlock3TerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _OR_PAIRS = [
        ("item_right_cow_stall_block", "filled_right_cow_stall_block"),
        ("item_cow_stall_block_2", "filled_cow_stall_block_right"),
    ]

class NextToCowFodderBlock3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_rightmost_cow_fodder_block"
    _NAMED_REGIONS = ["item_right_cow_stall_block_below", "item_right_cow_stall_block_left"]
    _TARGET_NAMES = ["next_to_right_cow_stall_block_up", "next_to_right_cow_stall_block_right"]

class FarmEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "farm_entrance"

class NearFarmSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_farm"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "farm_label",
    ]

class VillageEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "top_entrance"
    _TERMINATION_TARGET_NAME = "village_entrance"

class NearVillageSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_village"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["village_label"]

class GrasslandEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "grassland_entrance"

class NearGrasslandSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_grassland"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["grassland_label"]

class ForestEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "forest_entrance"

class NearForestSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_forest"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["forest_label"]

class CliffEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "cliff_entrance"

class NearCliffSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_cliff"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["cliff_label"]

class MountainEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "mountain_entrance"

class NearMountainSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_mountain"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["mountain_label"]

class ShoppingMallEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "shopping_mall_entrance"

class NearShoppingMallSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_shopping_mall"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "shopping_mall_label",
    ]

class ShoppingMallSecondFloorTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "shopping_mall_second_floor"

class NextToStairsSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_stairs"
    _NAMED_REGIONS = ["item_stairs", "item_stairs", "item_stairs"]
    _TARGET_NAMES = ["next_to_stairs_1", "next_to_stairs_2", "next_to_stairs_3"]

class FarmersUnionEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "farmers_union_entrance"

class NearFarmersUnionSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_farmers_union"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "farmers_union_label",
    ]

class AquariumEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "aquarium_entrance"

class NearAquariumSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_aquarium"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "aquarium_label",
    ]

class TheatreEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "theatre_entrance"

class NearTheatreSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_theatre"
    _NAMED_REGIONS = [
        "dialogue_box_bottom",
    ]
    _TARGET_NAMES = [
        "theatre_label",
    ]

class HotSpringEntranceTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser

    _TERMINATION_NAMED_REGION = "entrance"
    _TERMINATION_TARGET_NAME = "hot_spring_entrance"

class NearHotSpringSubgoal(AnyRegionMatchSubGoal):
    NAME = "outside_hot_spring"
    _NAMED_REGIONS = [
        "outside_hot_spring",
        "outside_hot_spring",
        "outside_hot_spring",
    ]
    _TARGET_NAMES = [
        "outside_hot_spring_left",
        "outside_hot_spring_right",
        "outside_hot_spring_up",
    ]

# HM3 hatch egg task
class HarvestMoon3NextToHatchingBoxSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_hatching_box"
    _NAMED_REGIONS = ["item_next_to_hatching_box"]
    _TARGET_NAMES = ["next_to_hatching_box"]

class HarvestMoon3HatchEggTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_hatching_box"
    _TERMINATION_TARGET_NAME = "dropped_egg_into_hatching_box"

# HM3 fill chicken fodder subgoals
class NextToChickenSilo3Subgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_chicken_silo"
    _NAMED_REGIONS = [
        "item_chicken_silo_left1",
        "item_chicken_silo_left2",
        "item_chicken_silo_above",
    ]
    _TARGET_NAMES = [
        "next_to_chicken_silo_right1",
        "next_to_chicken_silo_right2",
        "next_to_chicken_silo_down",
    ]

class PickupChickenFodder3Subgoal(AnyRegionMatchSubGoal):
    NAME = "picked_up_chicken_fodder_from_silo"
    _NAMED_REGIONS = [
        "item_chicken_silo_left1",
        "item_chicken_silo_left2",
        "item_chicken_silo_above",
    ]
    _TARGET_NAMES = [
        "got_fodder_from_chicken_silo_right1",
        "got_fodder_from_chicken_silo_right2",
        "got_fodder_from_chicken_silo_down",
    ]

class NextToTopmostChickenStallBlockSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_topmost_chicken_stall_block_with_fodder"
    _NAMED_REGIONS = ["item_next_to_topmost_chicken_stall_block"]
    _TARGET_NAMES = ["next_to_topmost_chicken_stall_block"]

class FillTopmostChickenStallBlockTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "item_topmost_chicken_stall_block"
    _TERMINATION_TARGET_NAME = "filled_topmost_chicken_stall_block"

class NextToFodderSetSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_fodder_set"
    _NAMED_REGIONS = ["item_fodder_set_below"]
    _TARGET_NAMES = ["next_to_fodder_set_up"]

class SelectedFodderSetSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_fodder_set"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["selected_fodder_set"]

class BuyFodderSet3TerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _ALL_PAIRS = [("dialogue_box_bottom", "bought_from_farmers_union"), ("item_fodder_set", "picked_fodder_set")]

class NextToHorseMedicineSubgoal(AnyRegionMatchSubGoal):
    NAME = "next_to_horse_medicine"
    _NAMED_REGIONS = ["item_horse_medicine_below"]
    _TARGET_NAMES = ["next_to_horse_medicine_up"]

class SelectedHorseMedicineSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_horse_medicine"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["selected_horse_medicine"]

class BuyHorseMedicine3TerminateMetric(MultiRegionMatchTerminationMetric, TerminationMetric):
    _ALL_PAIRS = [("dialogue_box_bottom", "bought_from_farmers_union"), ("item_horse_medicine", "picked_horse_medicine")]

# HM1 home expansion estimate task
class SelectHomeExpansionSubgoal(AnyRegionMatchSubGoal):
    NAME = "selected_home_expansion"
    _NAMED_REGIONS = ["dialogue_box_bottom"]
    _TARGET_NAMES = ["select_home_expansion"]

class GetHomeExpansionEstimateTerminateMetric(RegionMatchTerminationMetric, TerminationMetric):
    REQUIRED_PARSER = BaseHarvestMoonStateParser
    _TERMINATION_NAMED_REGION = "screen_bottom_half"
    _TERMINATION_TARGET_NAME = "home_expansion_estimate"

