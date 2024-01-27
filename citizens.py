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
    
    def get_total_satisfaction(self, tax_rate: float, buildings: list[object]) -> float:
        base = self.get_satisfaction_factors(buildings).average()
        base_modifier = 1
        base_modifier *= self.tax_rate_satisfaction_penalty(tax_rate)
        for building in buildings:
            if isinstance(building, BasicBuilding):
                base_modifier *= building.get_satisfaction_penalty()
        return max(0.0, min(100.0, base * base_modifier))
    
    def get_satisfaction_factors(self, buildings: list[object]) -> object:
        base = self.base_satisfaction_factors()
        for building in buildings:
            base *= building.get_satisfaction_factor_influence()
        return base
    
    @staticmethod
    def tax_rate_satisfaction_penalty(tax_rate: float):
        return 1 - (400 * ((tax_rate - 0.07) ** 3))

    def base_satisfaction_factors(self) -> object:
        return SatisfactionFactors(40.0, 40.0, 40.0, 40.0)

    def determine_migration(self, satisfaction) -> int:
        if satisfaction > EMIGRATION_THRESHOLD and satisfaction < IMMIGRATION_THRESHOLD:
            return 0
    
