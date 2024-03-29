__author__ = "6963879, Tverdohleb, 8291925, Hoffmann"

from dataclasses import dataclass

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
        return SatisfactionFactors(self.infrastructure * other.infrastructure,
                            self.safety * other.safety,
                            self.health * other.health,
                            self.entertainment * other.entertainment)
    
    def pow(self, power):
        return SatisfactionFactors(self.infrastructure ** power, self.safety ** power, self.health ** power, self.entertainment ** power)
    
    def scale(self, scalar: float) -> object:
        SatisfactionFactors(
            self.infrastructure * scalar,
            self.safety * scalar,
            self.health * scalar,
            self.entertainment * scalar,
        )
    
    def average(self) -> float:
        return (self.infrastructure + self.safety + self.health + self.entertainment) / 4
