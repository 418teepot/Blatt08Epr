__author__ = "6963879, Tverdohleb, 8291925, Hoffmann"

from abc import ABCMeta, abstractmethod
import random
from satisfaction_factors import SatisfactionFactors

class Building(metaclass=ABCMeta):
    def __init__(self, name: str, initial_count: int):
        self.name = name
        self.count = initial_count
    
    @abstractmethod
    def get_income(self, citizen_count) -> int:
        return 0

    @abstractmethod
    def get_expenses(self) -> int:
        pass

    def build(self):
        self.count += 1
    
    def destroy(self):
        if self.count > 1:
            self.count -= 1

    @staticmethod
    @abstractmethod
    def get_build_cost() -> int:
        pass

    @abstractmethod
    def get_satisfaction_factor_influence(self) -> object:
        pass


ERR_MARGIN = 100

class BasicBuilding(Building, metaclass=ABCMeta):
    def __init__(self, name: str, per_population: int, penalty: float, count: int):
        super().__init__(name, count)
        self.per_population = per_population
        self.penalty = penalty
    
    def get_satisfaction_penalty(self, citizen_count) -> int:
        if self.count == 0:
            return 1
        capacity = self.count * self.per_population
        if capacity + ERR_MARGIN < citizen_count:
            return (1 - self.penalty) ** (citizen_count // capacity)
        return 1
    
    @abstractmethod
    def get_satisfaction_factor_influence(self) -> object:
        pass

    def get_income(self, citizen_count: int) -> int:
        return 0

    @abstractmethod
    def get_expenses(self) -> int:
        pass

class School(BasicBuilding):
    def __init__(self, weight, count):
        super().__init__("Schule", 5000, weight, count)
    
    def get_expenses(self) -> int:
        return 200 * self.count
    
    def get_income(self, citizen_count: int) -> int:
        return 0
    
    @staticmethod
    def get_build_cost() -> int:
        return 2000
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.0, 1.0, 1.0, 1.0).pow(self.count)

class ElectircityGrid(BasicBuilding):
    def __init__(self, weight, count):
        super().__init__("Stromverteiler", 2000, weight, count)
    
    @staticmethod
    def get_build_cost() -> int:
        return 400
    
    def get_expenses(self) -> int:
        return 50

    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.01, 1.0, 1.0, 1.0).pow(self.count)
    
class BusStation(BasicBuilding):
    def __init__(self, weight, count):
        super().__init__("Busstation", 3000, weight, count)
    
    @staticmethod
    def get_build_cost() -> int:
        return 300
    
    def get_expenses(self) -> int:
        return 1000
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.01, 1.0, 1.0, 1.0).pow(self.count)
    
class PoliceStation(BasicBuilding):
    def __init__(self, weight, count):
        super().__init__("Polizeistation", 5000, weight, count)
    
    @staticmethod
    def get_build_cost() -> int:
        return 5000
    
    def get_expenses(self) -> int:
        return 2000
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.0, 1.01, 1.0, 1.0).pow(self.count)


class ElectiveBuilding(Building):
    def __init__(self, name):
        super().__init__(name, 0)
        self.weight = 0.1

    @abstractmethod
    def get_income(self, citizen_count) -> int:
        return 0
    
    def calculate_weight(self):
        return self.count * self.weight

class University(ElectiveBuilding):
    def __init__(self):
        super().__init__("Universität")
    
    @staticmethod
    def get_build_cost() -> int:
        return 5000
    
    def get_expenses(self) -> int:
        return 1500
    
    def get_income(self, citizen_count) -> int:
        if random.randint(0, 100) > 85:
            return random.randint(100, 2000)
        return 0
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.05, 1.0, 1.05, 1.05).pow(self.count)

class Hospital(ElectiveBuilding):
    def __init__(self):
        super().__init__("Krankenhaus")
    
    @staticmethod
    def get_build_cost() -> int:
        return 2000
    
    def get_expenses(self) -> int:
        return 700
    
    def get_income(self, citizen_count) -> int:
        return 0
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.0, 1.01, 1.10, 1.0).pow(self.count)

class Kindergarden(ElectiveBuilding):
    def __init__(self):
        super().__init__("Kindergarten")
    
    @staticmethod
    def get_build_cost() -> int:
        return 1000
    
    def get_expenses(self) -> int:
        return 300
    
    def get_income(self, citizen_count) -> int:
        return 0
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.00, 1.05, 1.05, 1.07).pow(self.count)
    
class CoalPowerPlant(ElectiveBuilding):
    def __init__(self):
        super().__init__("Kohlekraftwerk")
    
    @staticmethod
    def get_build_cost() -> int:
        return 5000
    
    def get_expenses(self) -> int:
        return 400
    
    def get_income(self, citizen_count) -> int:
        return 0
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.15, 1.0, 0.93, 1.0).pow(self.count)

class FitnessStudio(ElectiveBuilding):
    def __init__(self):
        super().__init__("Fitnessstudio")
    
    @staticmethod
    def get_build_cost() -> int:
        return 800
    
    def get_expenses(self) -> int:
        return 100
    
    def get_income(self, citizen_count) -> int:
        return random.randint(0, 10) * citizen_count
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.0, 1.0, 1.15, 1.05).pow(self.count)

class Kino(ElectiveBuilding):
    def __init__(self):
        super().__init__("Kino")
    
    @staticmethod
    def get_build_cost() -> int:
        return 900
    
    def get_expenses(self) -> int:
        return 300
    
    def get_income(self, citizen_count) -> int:
        return citizen_count / random.randint(5, 15) * 10
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.0, 1.0, 0.98, 1.15).pow(self.count)

class TennisCourt(ElectiveBuilding):
    def __init__(self):
        super().__init__("Tennisplatz")
    
    @staticmethod
    def get_build_cost() -> int:
        return 500
    
    def get_expenses(self) -> int:
        return 100
    
    def get_income(self, citizen_count) -> int:
        return citizen_count / random.randint(10, 30) * 50
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.0, 1.0, 1.15, 1.10).pow(self.count)
    
