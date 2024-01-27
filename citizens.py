__author__ = "6963879, Tverdohleb, 8291925, Hoffmann"

from building import BasicBuilding
from satisfaction_factors import SatisfactionFactors

INCOME_PER_CITIZEN = 2500
DEFAULT_CITIZEN_COUNT = 10_000

SMALL_CITY_THRESHOLD = 100_000
BIGGER_CITY_THRESHOLD = 300_000
LARGE_CITY_THRESHOLD = 700_000
MILION_CITY_THRESHOLD = 1_000_000

EMIGRATION_THRESHOLD = 30.0
IMMIGRATION_THRESHOLD = 40.0

class Citizens:
    def __init__(self, initial_count):
        self.count = initial_count
    
    def collect_taxes(self, tax_rate) -> int:
        return int(INCOME_PER_CITIZEN * tax_rate) * self.count
    
    def get_total_satisfaction(self, tax_rate: float, buildings: list[object], event: object) -> float:
        base = self.get_satisfaction_factors(buildings, event).average()
        base_modifier = 1
        base_modifier *= self.tax_rate_satisfaction_penalty(tax_rate)
        for building in buildings:
            if isinstance(building, BasicBuilding):
                base_modifier *= building.get_satisfaction_penalty(self.count)
        return max(0.0, min(100.0, base * base_modifier))
    
    def get_satisfaction_factors(self, buildings: list[object], event: object) -> object:
        base = self.base_satisfaction_factors()
        for building in buildings:
            base = base * building.get_satisfaction_factor_influence()
        return base
    
    @staticmethod
    def tax_rate_satisfaction_penalty(tax_rate: float):
        return 1 - (400 * ((tax_rate - 0.07) ** 3))

    def base_satisfaction_factors(self) -> object:
        if self.count < SMALL_CITY_THRESHOLD:
            return SatisfactionFactors(35.0, 35.0, 35.0, 35.0)
        elif self.count < BIGGER_CITY_THRESHOLD:
            return SatisfactionFactors(30.0, 30.0, 30.0, 30.0)
        elif self.count < LARGE_CITY_THRESHOLD :
            return SatisfactionFactors(25.0, 25.0, 25.0, 25.0)
        elif self.count < MILION_CITY_THRESHOLD:
            return SatisfactionFactors(20.0, 20.0, 20.0, 20.0)

    def determine_migration(self, satisfaction) -> int:
        clamped_satisfaction = min(max(satisfaction, 0), 60)
        return 0.03*((clamped_satisfaction - 35.0) ** 3)
    
