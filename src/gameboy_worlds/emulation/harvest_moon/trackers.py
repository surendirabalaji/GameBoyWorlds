from gameboy_worlds.emulation.harvest_moon.base_metrics import (
    CoreHarvestMoonMetrics,
    HarvestMoonOCRMetric,
    HarvestMoonTestMetric,
)
from gameboy_worlds.emulation.harvest_moon.test_metrics import (
    CowBarnTerminateMetric,
    OutsideCowBarnSubgoal,
    OutsideCowBarn2Subgoal,
    ChickenCoopTerminateMetric,
    OutsideChickenCoopSubgoal,
    OutsideChickenCoop2Subgoal,
    StorageTerminateMetric,
    OutsideStorageSubgoal,
    PickupWaterCanTerminateMetric,
    NextToWaterCanSubgoal,
    PickupCowBellTerminateMetric,
    NextToCowBellSubgoal,
    PickupSickleTerminateMetric,
    NextToSickleSubgoal,
    PickupHoeTerminateMetric,
    NextToHoeSubgoal,
    PickupHammerTerminateMetric,
    NextToHammerSubgoal,
    PickupGrassSeedTerminateMetric,
    NextToGrassSeedSubgoal,
    GoToSleepTerminateMetric,
    SleepOptionSubgoal,
    FeedSpiritTerminateMetric,
    HelpSpiritEarthquakeTerminateMetric,
    NextToSpiritSubgoal,
    NextToEarthquakeSpiritSubgoal,
    WaterTurnipTerminateMetric,
    NextToTurnipSubgoal,
    BuyMaterialTerminateMetric,
    OutsideCarpenter1Subgoal,
    ShopForMaterialSubgoal,
    SelectMaterialSubgoal,
    SelectHomeExpansionSubgoal,
    GetHomeExpansionEstimateTerminateMetric,
    BuyChickenTerminateMetric,
    BuyCowTerminateMetric,
    SellChickenTerminateMetric,
    SellCowTerminateMetric,
    SelectSellingCowSubgoal,
    ShopForConstructionEstimatesSubgoal,
    SelectHothouseSubgoal,
    GetHothouseEstimateTerminateMetric,
    OutsideAnimalShop1Subgoal,
    ShopForAnimalSubgoal,
    SelectChickenSubgoal,
    SelectCowSubgoal,
    SelectSellingChickenSubgoal,
    BuyCowBrushTerminateMetric,
    BuySaddlebagTerminateMetric,
    BuyMilkerTerminateMetric,
    OutsideToolShop1Subgoal,
    ShopForToolsSubgoal,
    SelectCowBrushSubgoal,
    SelectSaddlebagSubgoal,
    SelectMilkerSubgoal,
    BuyRiceBallTerminateMetric,
    OutsideRestaurantSubgoal,
    ShopForFoodSubgoal,
    SelectRiceBallSubgoal,
    BuyRiceBallOptionSubgoal,
    BuyCroissantTerminateMetric,
    SelectCroissantSubgoal,
    BuyCroissantOptionSubgoal,
    BuyCakeTerminateMetric,
    SelectCakeSubgoal,
    BuyCakeOptionSubgoal,
    OutsideJuiceBarSubgoal,
    ShopForJuiceSubgoal,
    BuyGrapeJuiceTerminateMetric,
    SelectGrapeJuiceSubgoal,
    BuyGrapeJuiceOptionSubgoal,
    GoToChurchPrayTerminateMetric,
    OutsideChurchSubgoal,
    InsideChurchSubgoal,
    PrayOptionSubgoal,
    OpenStorageListTerminateMetric,
    NextToStorageListSubgoal,
    FindRainyMoneyTerminateMetric,
    NextToSafeSubgoal,
    FindLostBirdTerminateMetric,
    NextToLostBirdSubgoal,
    SpeakToBlueHairGirlTerminateMetric,
    SpeakToBlueHairGirlWGTerminateMetric,
    NextToBlueHairGirlWGSubgoal,
    SpeakToPinkHairGirlWGTerminateMetric,
    NextToPinkHairGirlWGSubgoal,
    SpeakToRedHairGirlWGTerminateMetric,
    NextToRedHairGirlWGSubgoal,
    NextToBlueHairGirlSubgoal,
    SpeakToGoldenHairGirlTerminateMetric,
    NextToGoldenHairGirlSubgoal,
    SpeakToPinkHairGirlTerminateMetric,
    NextToPinkHairGirlSubgoal,
    FillChickenFodderBlock1TerminateMetric,
    NextToChickenSiloSubgoal,
    PickupChickenFodderSubgoal,
    NextToChickenFodderBlock1Subgoal,
    NextToCowFeedingStallSubgoal,
    FillUpperRightCowStallTerminateMetric,
    NextToChickenSilo2Subgoal,
    PickupChickenFodder2Subgoal,
    ReadVillageSignTerminateMetric,
    NextToVillageSignSubgoal,
    ReadFarmSignTerminateMetric,
    NextToFarmSignSubgoal,
    ReadSecretGardenSignTerminateMetric,
    NextToSecretGardenSignSubgoal,
    
    # HM2
    HospitalEntranceTerminateMetric,
    OutsideHospitalSubgoal,
    ToolShopEntranceTerminateMetric,
    OutsideToolShop2Subgoal,
    CarpenterEntranceTerminateMetric,
    OutsideCarpenter2Subgoal,
    AnimalShopEntranceTerminateMetric,
    OutsideAnimalShop2Subgoal,
    LibraryEntranceTerminateMetric,
    OutsideLibrarySubgoal,
    FindLuckyMoneyTerminateMetric,
    NextToClockSubgoal,
    FlowerShopEntranceTerminateMetric,
    OutsideFlowerShop2Subgoal,
    SelectBridgeSubgoal,
    GetBridgeEstimateTerminateMetric,
    RestaurantEntranceTerminateMetric,
    OutsideRestaurant2Subgoal,
    BuyLunchSetTerminateMetric,
    SelectLunchSetSubgoal,
    BuyLunchSetOptionSubgoal,
    BuyBeverageSetTerminateMetric,
    SelectBeverageSetSubgoal,
    BuyBeverageSetOptionSubgoal,
    BuyTodaysSpecialTerminateMetric,
    SelectTodaysSpecialSubgoal,
    BuyTodaysSpecialOptionSubgoal,
    
    # HM2 TO DO
    OpenMenuTerminateMetric,
    ReadNoticeBoardTerminateMetric,
    NextToNoticeBoardSubgoal,
    ReadCropFieldSignTerminateMetric,
    NextToCropFieldSignSubgoal,
    NextToDiarySubgoal,
    DiaryOptionSubgoal,
    EmptyHandsSelectedSubgoal,
    ReadyToPickSickleSubgoal,
    EquipSickleTerminateMetric,
    ReadyToPickHammerSubgoal,
    EquipHammerTerminateMetric,
    ReadyToPickFishingRodSubgoal,
    EquipFishingRodTerminateMetric,
    AxeSelected2Subgoal,
    SprinklerSelected1Subgoal,
    EquipSickleReplacingSprinklerTerminateMetric,
    HoeSelected3Subgoal,
    EquipNetReplacingHoeTerminateMetric,
    NextToEggSubgoal,
    HatchEggTerminateMetric,
    NextToRockFromLeftSubgoal,
    BreakRockTerminateMetric,
    NextToRightmostRockAboveSubgoal,
    BreakRightmostRockTerminateMetric,
    NextToLowestWeedFromAboveSubgoal,
    RemoveLowestWeedTerminateMetric,
    CutLowestWeedTerminateMetric,
    NextToTopLeftWeedFromRightSubgoal,
    RemoveTopLeftWeedTerminateMetric,
    CutTopLeftWeedTerminateMetric,
    NextToGrasslandFromLeftSubgoal,
    HarvestCenterGrasslineTerminateMetric,
    PickedUpBrokenFenceSubgoal,
    RestoreFenceTerminateMetric,
    NextToCenterTurnipSubgoal,
    HarvestCenterTurnipTerminateMetric,
    NextToCenterTurnipLeftSubgoal,
    WaterCenterTurnipTerminateMetric,
    # NextToShippingBoxSubgoal,
    # ShipEggplantTerminateMetric,
    AtTheStartLineSubgoal,
    Cross500mLineTerminateMetric,
    Cross1000mLineTerminateMetric,
    NextToCenterEggplantSubgoal,
    HarvestCenterEggplantTerminateMetric,
    NextToCenterCarrotSubgoal,
    HarvestCenterCarrotTerminateMetric,
    NextToCenterPotatoSubgoal,
    WaterCenterPotatoTerminateMetric,
    NextToCenterPotatoBelowSubgoal,
    HarvestCenterPotatoTerminateMetric,
    NextToCenterAsparagusSubgoal,
    WaterCenterAsparagusTerminateMetric,
    AtCornCenterSubgoal,
    WaterCornFieldTerminateMetric,
    AtCabbageCenterSubgoal,
    WaterCabbageFieldTerminateMetric,
    NextToCenterCornSubgoal,
    CutCenterCornTerminateMetric,
    ComputersArticleSelectedSubgoal,
    ReadComputersArticleTerminateMetric,
    BouldersArticleSelectedSubgoal,
    ReadBouldersArticleTerminateMetric,
    CropsArticleSelectedSubgoal,
    ReadCropsArticleTerminateMetric,
    NextToLeftmostWeedSubgoal,
    RemoveLeftmostWeedTerminateMetric,
    NextToBerrySubgoal,
    PickBerryTerminateMetric,
    NextToBerryAboveSubgoal,
    PickBerryAboveTerminateMetric,
    NextToBlueHairGirl2Subgoal,
    SpeakToBlueHairGirl2TerminateMetric,
    NextToPurpleHairGirlSubgoal,
    SpeakToPurpleHairGirlTerminateMetric,
    NextToBlondeGirlSubgoal,
    SpeakToBlondeGirlTerminateMetric,
    HarvestMoon2NextToHatchingBoxSubgoal,
    HarvestMoon2HatchEggTerminateMetric,
    ReadyToPickNetSubgoal,
    EquipNetReplacingAxTerminateMetric,
    ReadyToPickRosemarySeedsSubgoal,
    EquipRosemarySeedsReplacingAxTerminateMetric,
    
    ## HM3
    NextToWeed3Subgoal,
    RemoveWeed3TerminateMetric,
    NextToCherrySubgoal,
    PickUpCherry3TerminateMetric,
    HarvestMoon3NextToHatchingBoxSubgoal,
    HarvestMoon3HatchEggTerminateMetric,
    NextToChickenSilo3Subgoal,
    PickupChickenFodder3Subgoal,
    NextToTopmostChickenStallBlockSubgoal,
    FillTopmostChickenStallBlockTerminateMetric,
    NextToFodderSetSubgoal,
    SelectedFodderSetSubgoal,
    BuyFodderSet3TerminateMetric,
    NextToHorseMedicineSubgoal,
    SelectedHorseMedicineSubgoal,
    BuyHorseMedicine3TerminateMetric,
    SpeakToKateTerminateMetric,
    NextToKateSubgoal,
    NextToCenterSPotatoSubgoal,
    ReadAnimalCh2TerminateMetric,
    NextToBookshelfSubgoal,
    HarvestCenterTurnip3TerminateMetric,
    NextToCenterTurnip3Subgoal,
    SellChicken3TerminateMetric,
    NextToSellChicken3Subgoal,
    PickBerry3TerminateMetric,
    NextToBerry3Subgoal,
    CheckPlayerMoneyTerminateMetric,
    CheckPlayerMoneySubgoal,
    HarvestCenterEggplantTop3TerminateMetric,
    NextToCenterEggplantTopSubgoal,
    WaterCenterSPotato3TerminateMetric,
    NextToCenterWatermelonSubgoal,
    WaterCenterWatermelon3TerminateMetric,
    NextToTargetPotatoBelowSubgoal,
    HarvestTargetPotato3TerminateMetric,
    OutsideChickenCoop3Subgoal,
    NextToSecretGardenSign3Subgoal,
    ReadFerrySignTerminateMetric,
    NextToFerrySignSubgoal,
    FindSecretSavingsTerminateMetric,
    NextToFireplaceSubgoal,
    BuyPotatoSeeds3TerminateMetric,
    NextToPotatoSeeds3Subgoal,
    ChooseTea3TerminateMetric,
    NextToTea3Subgoal,
    ChooseAsparagusSeedsTerminateMetric,
    NextToAsparagusSeeds3Subgoal,
    NextToTurnipSeeds3Subgoal,
    BuyTurnipSeeds3TerminateMetric,
    ReadMorningMarketSignTerminateMetric,
    NextToMorningMarketSignSubgoal,
    ReadStorageSignTerminateMetric,
    NextToStorageSign3Subgoal,
    SpeakToKirkVillageTerminateMetric,
    NextToKirkVillageSubgoal,
    TakeFerryTerminateMetric,
    NextToKirkMainlandSubgoal,
    SpeakToJoeTerminateMetric,
    NextToJoeSubgoal,
    SpeakToLukiaTerminateMetric,
    NextToLukiaSubgoal,
    SpeakToLucusTerminateMetric,
    NextToLucusSubgoal,
    SpeakToLylaTerminateMetric,
    NextToLylaSubgoal,
    BuyHorseSaddleTerminateMetric,
    NextToHorseSaddleSubgoal,
    BuyFlowerVaseTerminateMetric,
    NextToVaseSubgoal,
    BuyMealSetTerminateMetric,
    SelectMealSetSubgoal,
    BuyCoffeeTerminateMetric,
    NextToCoffeeSubgoal,
    SelectCoffeeSubgoal,
    FillCowFodderBlock3TerminateMetric,
    NextToCowFodderBlock3Subgoal,
    FarmEntranceTerminateMetric,
    NearFarmSubgoal,
    VillageEntranceTerminateMetric,
    NearVillageSubgoal,
    GrasslandEntranceTerminateMetric,
    NearGrasslandSubgoal,
    ForestEntranceTerminateMetric,
    NearForestSubgoal,
    CliffEntranceTerminateMetric,
    NearCliffSubgoal,
    MountainEntranceTerminateMetric,
    NearMountainSubgoal,
    ShoppingMallEntranceTerminateMetric,
    NearShoppingMallSubgoal,
    ShoppingMallSecondFloorTerminateMetric,
    NextToStairsSubgoal,
    FarmersUnionEntranceTerminateMetric,
    NearFarmersUnionSubgoal,
    AquariumEntranceTerminateMetric,
    NearAquariumSubgoal,
    TheatreEntranceTerminateMetric,
    NearTheatreSubgoal,
    HotSpringEntranceTerminateMetric,
    NearHotSpringSubgoal,
)
from gameboy_worlds.utils import log_info
from gameboy_worlds.emulation.tracker import (
    StateTracker,
    TestTrackerMixin,
    DummySubGoalMetric,
    make_subgoal_metric_class,
)
from gameboy_worlds.emulation.harvest_moon.parsers import (
    AgentState,
)
from typing import Optional


class CoreHarvestMoonTracker(StateTracker):
    """
    StateTracker for core Harvest Moon metrics.
    """

    _REMOVE_GRID_OVERLAY = False
    """ Whether to remove the grid overlay drawn by the state parser when the agent is in FREE ROAM. This is useful for VLM based agents may need a coordinate grid overlayed onto the frame, but may cause issues for agents that do not understand that it is not a part of the game. """

    def start(self):
        super().start()
        self.metric_classes.extend([CoreHarvestMoonMetrics, HarvestMoonTestMetric])

    def step(self, *args, **kwargs):
        """
        Calls on super().step(), but then modifies the current frame to overlay the grid if the agent is in FREE ROAM.
        """
        super().step(*args, **kwargs)
        if self._REMOVE_GRID_OVERLAY:
            state = self.episode_metrics["harvest_moon_core"]["agent_state"]
            # if agent_state is in FREE ROAM, draw the grid, otherwise do not
            if state == AgentState.FREE_ROAM:
                screen = self.episode_metrics["core"]["current_frame"]
                screen = self.state_parser.draw_grid_overlay(current_frame=screen)
                self.episode_metrics["core"]["current_frame"] = screen
                previous_screens = self.episode_metrics["core"]["passed_frames"]
                if previous_screens is not None:
                    self.episode_metrics["core"]["passed_frames"][-1, :] = screen


class HarvestMoonOCRTracker(CoreHarvestMoonTracker):
    def start(self):
        super().start()
        self.metric_classes.extend([HarvestMoonOCRMetric])
        
class HarvestMoonTestTracker(TestTrackerMixin, HarvestMoonOCRTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = CowBarnTerminateMetric
    SUBGOAL_METRIC = DummySubGoalMetric

class HarvestMoonCowBarnTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = CowBarnTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideCowBarnSubgoal])
    
class HarvestMoonChickenCoopTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = ChickenCoopTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideChickenCoopSubgoal])

class HarvestMoon3ChickenCoopTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = ChickenCoopTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideChickenCoop3Subgoal])
    
class HarvestMoonStorageTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = StorageTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideStorageSubgoal])

class HarvestMoonPickupWaterCanTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = PickupWaterCanTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToWaterCanSubgoal])

class HarvestMoonPickupCowBellTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = PickupCowBellTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCowBellSubgoal])

class HarvestMoonPickupSickleTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = PickupSickleTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToSickleSubgoal])

class HarvestMoonPickupHoeTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = PickupHoeTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToHoeSubgoal])

class HarvestMoonPickupHammerTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = PickupHammerTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToHammerSubgoal])

class HarvestMoonPickupGrassSeedTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = PickupGrassSeedTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToGrassSeedSubgoal])

class HarvestMoonGoToSleepTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = GoToSleepTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([SleepOptionSubgoal])
    
class HarvestMoonFeedSpiritTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = FeedSpiritTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToSpiritSubgoal])

class HarvestMoonHelpSpiritEarthquakeTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HelpSpiritEarthquakeTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToEarthquakeSpiritSubgoal])

class HarvestMoonWaterTurnipTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = WaterTurnipTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToTurnipSubgoal])

class HarvestMoonBuyMaterialTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyMaterialTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideCarpenter1Subgoal, ShopForMaterialSubgoal, SelectMaterialSubgoal])

class HarvestMoonBuyChickenTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyChickenTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideAnimalShop1Subgoal, ShopForAnimalSubgoal, SelectChickenSubgoal])

class HarvestMoonBuyCowTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyCowTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([SelectCowSubgoal])

class HarvestMoonSellChickenTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SellChickenTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideAnimalShop1Subgoal, ShopForAnimalSubgoal, SelectSellingChickenSubgoal])

class HarvestMoonBuyCowBrushTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyCowBrushTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideToolShop1Subgoal, ShopForToolsSubgoal, SelectCowBrushSubgoal])

class HarvestMoonBuySaddlebagTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuySaddlebagTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideToolShop1Subgoal, ShopForToolsSubgoal, SelectSaddlebagSubgoal])

class HarvestMoonBuyMilkerTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyMilkerTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideToolShop1Subgoal, ShopForToolsSubgoal, SelectMilkerSubgoal])

class HarvestMoonBuyRiceBallTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = BuyRiceBallTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideRestaurantSubgoal, ShopForFoodSubgoal, SelectRiceBallSubgoal, BuyRiceBallOptionSubgoal])

class HarvestMoonBuyCroissantTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyCroissantTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideRestaurantSubgoal, ShopForFoodSubgoal, SelectCroissantSubgoal, BuyCroissantOptionSubgoal])

class HarvestMoonBuyCakeTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyCakeTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideRestaurantSubgoal, ShopForFoodSubgoal, SelectCakeSubgoal, BuyCakeOptionSubgoal])

class HarvestMoonBuyGrapeJuiceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyGrapeJuiceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideJuiceBarSubgoal, ShopForJuiceSubgoal, SelectGrapeJuiceSubgoal, BuyGrapeJuiceOptionSubgoal])

class HarvestMoonGoToChurchPrayTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = GoToChurchPrayTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideChurchSubgoal, InsideChurchSubgoal, PrayOptionSubgoal])

class HarvestMoonOpenStorageListTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = OpenStorageListTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToStorageListSubgoal])

class HarvestMoonFindRainyMoneyTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = FindRainyMoneyTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToSafeSubgoal])

class HarvestMoonFindLostBirdTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = FindLostBirdTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToLostBirdSubgoal])

class HarvestMoonSpeakToBlueHairGirlTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = SpeakToBlueHairGirlTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToBlueHairGirlSubgoal])

class HarvestMoonSpeakToGoldenHairGirlTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToGoldenHairGirlTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToGoldenHairGirlSubgoal])

class HarvestMoonSpeakToPinkHairGirlTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToPinkHairGirlTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToPinkHairGirlSubgoal])

class HarvestMoon1SpeakToBlueHairGirlWGTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToBlueHairGirlWGTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToBlueHairGirlWGSubgoal])

class HarvestMoon1SpeakToPinkHairGirlWGTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToPinkHairGirlWGTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToPinkHairGirlWGSubgoal])

class HarvestMoon1SpeakToRedHairGirlWGTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToRedHairGirlWGTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToRedHairGirlWGSubgoal])

class HarvestMoonFillChickenFodderTracker(HarvestMoonTestTracker):
    """
    Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
    """

    TERMINATION_TRUNCATION_METRIC = FillChickenFodderBlock1TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToChickenSiloSubgoal, PickupChickenFodderSubgoal, NextToChickenFodderBlock1Subgoal])

class HarvestMoon1FillCowFodderTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = FillUpperRightCowStallTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCowFeedingStallSubgoal])



class HarvestMoonOpenMenuTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = OpenMenuTerminateMetric

# HM2
class HarvestMoon2CowBarnTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = CowBarnTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideCowBarn2Subgoal])

class HarvestMoon2ChickenCoopTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ChickenCoopTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideChickenCoop2Subgoal])

class HarvestMoon2FindLuckyMoneyTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = FindLuckyMoneyTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToClockSubgoal])

class HarvestMoon2HospitalEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HospitalEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideHospitalSubgoal])

class HarvestMoon2ToolShopEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ToolShopEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideToolShop2Subgoal])

class HarvestMoon2CarpenterEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = CarpenterEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideCarpenter2Subgoal])

class HarvestMoon2AnimalShopEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = AnimalShopEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideAnimalShop2Subgoal])

class HarvestMoon2LibraryEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = LibraryEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideLibrarySubgoal])

class HarvestMoon2FlowerShopEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = FlowerShopEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideFlowerShop2Subgoal])

class HarvestMoon2GetBridgeEstimateTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = GetBridgeEstimateTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideCarpenter2Subgoal, ShopForConstructionEstimatesSubgoal, SelectBridgeSubgoal])

class HarvestMoon2BuyMilkerTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyMilkerTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideToolShop2Subgoal, ShopForToolsSubgoal, SelectMilkerSubgoal])

class HarvestMoon2RestaurantEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = RestaurantEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideRestaurant2Subgoal])

class HarvestMoon2BuyLunchSetTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyLunchSetTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([SelectLunchSetSubgoal, BuyLunchSetOptionSubgoal])

class HarvestMoon2BuyBeverageSetTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyBeverageSetTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([SelectBeverageSetSubgoal, BuyBeverageSetOptionSubgoal])

class HarvestMoon2BuyTodaysSpecialTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyTodaysSpecialTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([SelectTodaysSpecialSubgoal, BuyTodaysSpecialOptionSubgoal])

class HarvestMoon2GoToBedTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = GoToSleepTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToDiarySubgoal, DiaryOptionSubgoal])

class HarvestMoon2ReadSecretGardenSignTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadSecretGardenSignTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToSecretGardenSignSubgoal])

class HarvestMoon2ReadCropFieldSignTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadCropFieldSignTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCropFieldSignSubgoal])

class HarvestMoon2EquipSickleTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = EquipSickleTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([EmptyHandsSelectedSubgoal, ReadyToPickSickleSubgoal])

class HarvestMoon2EquipHammerTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = EquipHammerTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([EmptyHandsSelectedSubgoal, ReadyToPickHammerSubgoal])

class HarvestMoon2EquipFishingRodTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = EquipFishingRodTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([EmptyHandsSelectedSubgoal, ReadyToPickFishingRodSubgoal])

class HarvestMoon2EquipNetReplacingAxTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = EquipNetReplacingAxTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([AxeSelected2Subgoal, ReadyToPickNetSubgoal])

class HarvestMoon2EquipRosemarySeedsReplacingAxTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = EquipRosemarySeedsReplacingAxTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([AxeSelected2Subgoal, ReadyToPickRosemarySeedsSubgoal])

class HarvestMoon2EquipSickleReplacingSprinklerTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = EquipSickleReplacingSprinklerTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([SprinklerSelected1Subgoal, ReadyToPickSickleSubgoal])

class HarvestMoon2EquipNetReplacingHoeTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = EquipNetReplacingHoeTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([HoeSelected3Subgoal, ReadyToPickNetSubgoal])

class HarvestMoon1HatchEggTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HatchEggTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToEggSubgoal])

class HarvestMoon1BreakRockTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BreakRockTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToRockFromLeftSubgoal])

class HarvestMoon1BreakRightmostRockTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BreakRightmostRockTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToRightmostRockAboveSubgoal])

class HarvestMoon1RemoveLowestWeedTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = RemoveLowestWeedTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToLowestWeedFromAboveSubgoal])

class HarvestMoon1CutLowestWeedTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = CutLowestWeedTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToLowestWeedFromAboveSubgoal])

class HarvestMoon1RemoveTopLeftWeedTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = RemoveTopLeftWeedTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToTopLeftWeedFromRightSubgoal])

class HarvestMoon1CutTopLeftWeedTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = CutTopLeftWeedTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToTopLeftWeedFromRightSubgoal])

class HarvestMoon1HarvestCenterGrasslineTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HarvestCenterGrasslineTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToGrasslandFromLeftSubgoal])

class HarvestMoon1RestoreFenceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = RestoreFenceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([PickedUpBrokenFenceSubgoal])

class HarvestMoon1HarvestCenterTurnipTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HarvestCenterTurnipTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterTurnipSubgoal])

class HarvestMoon1WaterCenterTurnipTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = WaterCenterTurnipTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterTurnipLeftSubgoal])

class HarvestMoon1WaterCenterPotatoTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = WaterCenterPotatoTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterPotatoSubgoal])

class HarvestMoon1HarvestCenterPotatoTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HarvestCenterPotatoTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterPotatoBelowSubgoal])

class HarvestMoon1GetHomeExpansionEstimateTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = GetHomeExpansionEstimateTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideCarpenter1Subgoal, ShopForMaterialSubgoal, SelectHomeExpansionSubgoal])

# class HarvestMoon2ShipEggplantTracker(HarvestMoonTestTracker):
#     TERMINATION_TRUNCATION_METRIC = ShipEggplantTerminateMetric
#     SUBGOAL_METRIC = make_subgoal_metric_class([NextToShippingBoxSubgoal])

class HarvestMoon2Cross500mLineTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = Cross500mLineTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([AtTheStartLineSubgoal])

class HarvestMoon2Cross1000mLineTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = Cross1000mLineTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([AtTheStartLineSubgoal])

class HarvestMoon2HarvestCenterEggplantTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HarvestCenterEggplantTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterEggplantSubgoal])

class HarvestMoon2HarvestCenterCarrotTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HarvestCenterCarrotTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterCarrotSubgoal])

class HarvestMoon2WaterCenterPotatoTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = WaterCenterPotatoTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterPotatoSubgoal])

class HarvestMoon2WaterCenterAsparagusTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = WaterCenterAsparagusTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterAsparagusSubgoal])

class HarvestMoon2WaterCornFieldTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = WaterCornFieldTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([AtCornCenterSubgoal])

class HarvestMoon2WaterCabbageFieldTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = WaterCabbageFieldTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([AtCabbageCenterSubgoal])

class HarvestMoon2CutCenterCornTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = CutCenterCornTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterCornSubgoal])

class HarvestMoon2ReadComputersArticleTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadComputersArticleTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([ComputersArticleSelectedSubgoal])

class HarvestMoon2ReadBouldersArticleTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadBouldersArticleTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([BouldersArticleSelectedSubgoal])

class HarvestMoon2ReadCropsArticleTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadCropsArticleTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([CropsArticleSelectedSubgoal])

class HarvestMoon2RemoveLeftmostWeedTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = RemoveLeftmostWeedTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToLeftmostWeedSubgoal])

class HarvestMoon2PickBerryTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = PickBerryTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToBerrySubgoal])

class HarvestMoon2PickBerryAboveTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = PickBerryAboveTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToBerryAboveSubgoal])

class HarvestMoon2SpeakToBlueHairGirlTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToBlueHairGirl2TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToBlueHairGirl2Subgoal])

class HarvestMoon2SpeakToPurpleHairGirlTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToPurpleHairGirlTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToPurpleHairGirlSubgoal])

class HarvestMoon2SpeakToBlondeGirlTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToBlondeGirlTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToBlondeGirlSubgoal])

class HarvestMoon2HatchEggTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HarvestMoon2HatchEggTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([HarvestMoon2NextToHatchingBoxSubgoal])

class HarvestMoon2BuyCowTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyCowTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([SelectCowSubgoal])

class HarvestMoon2SellCowTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SellCowTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([ShopForAnimalSubgoal, SelectSellingCowSubgoal])

class HarvestMoon2SellChickenTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SellChickenTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([ShopForAnimalSubgoal, SelectSellingChickenSubgoal])

class HarvestMoon2GetHothouseEstimateTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = GetHothouseEstimateTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([OutsideCarpenter2Subgoal, ShopForConstructionEstimatesSubgoal, SelectHothouseSubgoal])

class HarvestMoon2BuyChickenTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyChickenTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([ShopForAnimalSubgoal, SelectChickenSubgoal])

class HarvestMoon2FillChickenFodderTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = FillChickenFodderBlock1TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToChickenSilo2Subgoal, PickupChickenFodder2Subgoal, NextToChickenFodderBlock1Subgoal])

## TO DO
class HarvestMoonReadNoticeBoardTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadNoticeBoardTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToNoticeBoardSubgoal])

class HarvestMoonReadVillageSignTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadVillageSignTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToVillageSignSubgoal])

class HarvestMoonReadFarmSignTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadFarmSignTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToFarmSignSubgoal])


# class HarvestMoonCleanRockTracker(HarvestMoonTestTracker):
#     """
#     Inherit this class and set TERMINATION_TRUNCATION_METRIC to create a TestTracker for Harvest Moon games.
#     """

#     TERMINATION_TRUNCATION_METRIC = PickupWaterCanTerminateMetric
#     SUBGOAL_METRIC = make_subgoal_metric_class([NextToWaterCanSubgoal])


## HM3
class HarvestMoon3ReadSecretGardenSignTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadSecretGardenSignTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToSecretGardenSign3Subgoal])

class HarvestMoon3ReadFerrySignTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadFerrySignTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToFerrySignSubgoal])

class HarvestMoon3FindSecretSavingsTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = FindSecretSavingsTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToFireplaceSubgoal])

class HarvestMoon3ChooseTeaTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ChooseTea3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToTea3Subgoal])

class HarvestMoon3ChooseAsparagusSeedsTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ChooseAsparagusSeedsTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToAsparagusSeeds3Subgoal])

class HarvestMoon3BuyPotatoSeedsTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyPotatoSeeds3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToPotatoSeeds3Subgoal])

class HarvestMoon3BuyTurnipSeedsTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyTurnipSeeds3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToTurnipSeeds3Subgoal])

class HarvestMoon3ReadMorningMarketSignTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadMorningMarketSignTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToMorningMarketSignSubgoal])

class HarvestMoon3ReadStorageSignTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadStorageSignTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToStorageSign3Subgoal])

class HarvestMoon3SpeakToKirkVillageTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToKirkVillageTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToKirkVillageSubgoal])

class HarvestMoon3TakeFerryTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = TakeFerryTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToKirkMainlandSubgoal])

class HarvestMoon3SpeakToJoeTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToJoeTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToJoeSubgoal])

class HarvestMoon3SpeakToLukiaTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToLukiaTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToLukiaSubgoal])

class HarvestMoon3SpeakToLucusTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToLucusTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToLucusSubgoal])

class HarvestMoon3SpeakToLylaTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToLylaTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToLylaSubgoal])

class HarvestMoon3BuyHorseSaddleTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyHorseSaddleTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToHorseSaddleSubgoal])

class HarvestMoon3BuyFlowerVaseTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyFlowerVaseTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToVaseSubgoal])

class HarvestMoon3BuyMealSetTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyMealSetTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([SelectMealSetSubgoal])

class HarvestMoon3BuyCoffeeTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyCoffeeTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCoffeeSubgoal])

class HarvestMoon3FeedCowFodderTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = FillCowFodderBlock3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCowFodderBlock3Subgoal])

class HarvestMoon3FarmEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = FarmEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearFarmSubgoal])

class HarvestMoon3VillageEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = VillageEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearVillageSubgoal])

class HarvestMoon3GrasslandEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = GrasslandEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearGrasslandSubgoal])

class HarvestMoon3ForestEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ForestEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearForestSubgoal])

class HarvestMoon3CliffEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = CliffEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearCliffSubgoal])

class HarvestMoon3MountainEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = MountainEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearMountainSubgoal])

class HarvestMoon3ShoppingMallEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ShoppingMallEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearShoppingMallSubgoal])

class HarvestMoon3ShoppingMallSecondFloorTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ShoppingMallSecondFloorTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToStairsSubgoal])

class HarvestMoon3FarmersUnionEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = FarmersUnionEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearFarmersUnionSubgoal])

class HarvestMoon3AquariumEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = AquariumEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearAquariumSubgoal])

class HarvestMoon3TheatreEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = TheatreEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearTheatreSubgoal])

class HarvestMoon3HotSpringEntranceTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HotSpringEntranceTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NearHotSpringSubgoal])

class HarvestMoon3BreakRockTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BreakRockTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToRockFromLeftSubgoal])

class HarvestMoon3RemoveWeedTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = RemoveWeed3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToWeed3Subgoal])

class HarvestMoon3PickUpCherryTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = PickUpCherry3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCherrySubgoal])

class HarvestMoon3HatchEggTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HarvestMoon3HatchEggTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([HarvestMoon3NextToHatchingBoxSubgoal])

class HarvestMoon3FillChickenFodderTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = FillTopmostChickenStallBlockTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToChickenSilo3Subgoal, PickupChickenFodder3Subgoal, NextToTopmostChickenStallBlockSubgoal])

class HarvestMoon3BuyFodderSetTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyFodderSet3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToFodderSetSubgoal, SelectedFodderSetSubgoal])

class HarvestMoon3BuyHorseMedicineTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = BuyHorseMedicine3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToHorseMedicineSubgoal, SelectedHorseMedicineSubgoal])

class HarvestMoon3SpeakToKateTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SpeakToKateTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToKateSubgoal])

class HarvestMoon3WaterCenterWatermelonTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = WaterCenterWatermelon3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterWatermelonSubgoal])

class HarvestMoon3WaterCenterSPotatoTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = WaterCenterSPotato3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterSPotatoSubgoal])

class HarvestMoon3HarvestTargetPotatoTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HarvestTargetPotato3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToTargetPotatoBelowSubgoal])

class HarvestMoon3ReadAnimalCh2Tracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = ReadAnimalCh2TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToBookshelfSubgoal])

class HarvestMoon3HarvestCenterTurnipTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HarvestCenterTurnip3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterTurnip3Subgoal])

class HarvestMoon3SellChickenTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = SellChicken3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToSellChicken3Subgoal])

class HarvestMoon3PickBerryTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = PickBerry3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToBerry3Subgoal])

class HarvestMoon3CheckPlayerMoneyTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = CheckPlayerMoneyTerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([CheckPlayerMoneySubgoal])

class HarvestMoon3HarvestCenterEggplantTopTracker(HarvestMoonTestTracker):
    TERMINATION_TRUNCATION_METRIC = HarvestCenterEggplantTop3TerminateMetric
    SUBGOAL_METRIC = make_subgoal_metric_class([NextToCenterEggplantTopSubgoal])