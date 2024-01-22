from building import Building, BasicBuilding
INCOME_PER_CITIZEN = 2500

from dataclasses import dataclass

@dataclass
class SatisfactionFactors:
    """Class for keeping track of the satisfaction Factors."""
    infrastructure: float
    safety: float
    health: float
    etertainment: float 

    def __mul__(self, other):
        SatisfactionFacotrs(self.infrastructure * other.infrastructure, self.safety * other.safety, self.health * other.health, self.entertainment * other.entertainment)
    
    def average(self):
        return (self.infrastructure + self.safety + self.health + self.entertainment) / 4

class Citizens:
    def __init__(self, initial_count):
        self.count = initial_count
    
    def collect_taxes(self, tax_rate) -> int:
        return int(INCOME_PER_CITIZEN * tax_rate) * self.count
    
class CitizenSatisfaction:
    def __init__(self, infrastructure, safety, entertainment, health):
        self.infrastructure = infrastructure
        self.safety = safety
        self.entertainment = entertainment
        self.health = health
    
    def calculate_satisfaction(self, buildings: list[Building]) -> int:
        satisfaction_penalties = 1
        for building in buildings:
            if isinstance(building, BasicBuilding):
                satisfaction_penalties *= building.get_satisfaction_penalty()
        return (self.infrastructure + self.safety + self.health + self.entertainment) / 4 * (1 - satisfaction_penalties)
    
    
    def calculate_infrastructure(self, buildings: list[Building], citizen: Citizens) -> int:
        pass

    def calculate_safety(self, buildings: list[Building], citizen: Citizens) -> int:
        pass
    
    def calculate_entertainment(self, buildings: list[Building], citizen: Citizens) -> int:
        pass

    def calculate_health(self, buildings: list[Building], citizen: Citizens) -> int:
        pass