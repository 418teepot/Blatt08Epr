from building import Building, BasicBuilding
from dataclasses import dataclass

INCOME_PER_CITIZEN = 2500

@dataclass
class SatisfactionFactors:
    """Class for keeping track of the satisfaction Factors."""
    infrastructure: float
    safety: float
    health: float
    entertainment: float

    def __init__(self, infrastructure, safety, health, entertainment):
        self.infrastructure = infrastructure
        self.safety = safety
        self.health = health
        self.entertainment = entertainment
    
    def __mul__(self, other):
        SatisfactionFactors(self.infrastructure * other.infrastructure,
                            self.safety * other.safety,
                            self.health * other.health,
                            self.entertainment * other.entertainment)
    
    def average(self) -> float:
        return (self.infrastructure + self.safety + self.health + self.entertainment) / 4

class Citizens:
    SatisfactionFactors(30.0, 30.0, 30.0, 30.0)
    def __init__(self, initial_count):
        self.count = initial_count
        self.satisfaction = SatisfactionFactors(30.0, 30.0, 30.0, 30.0)
    
    def collect_taxes(self, tax_rate) -> int:
        return int(INCOME_PER_CITIZEN * tax_rate) * self.count
    
    def update_satisfaction(self, buildings: list[Building]):
        for building in buildings:
            self.satisfaction = building.update_satisfaction(self.satisfaction)
        