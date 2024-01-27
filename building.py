from abc import ABCMeta, abstractmethod
from satisfaction_factors import SatisfactionFactors

class Building(metaclass=ABCMeta):
    def __init__(self, name: str, initial_count: int):
        self.name = name
        self.count = initial_count
    
    @abstractmethod
    def get_income(self, citizen_count) -> int:
        pass

    @abstractmethod
    def get_expenses(self) -> int:
        pass

    def build(self):
        self.count += 1

    @staticmethod
    @abstractmethod
    def get_build_cost() -> int:
        pass

    @abstractmethod
    def get_satisfaction_factor_influence(self) -> object:
        pass


ERR_MARGIN = 100

class BasicBuilding(Building, metaclass=ABCMeta):
    def __init__(self, name: str, per_population: int, penalty: float, count: int, construction_cost: int, build_time: int):
        super().__init__(name, count)
        self.per_population = per_population
        self.penalty = penalty
    
    def get_satisfaction_penalty(self, citizen_count) -> int:
        capacity = self.count * self.per_population
        if capacity + ERR_MARGIN < citizen_count:
            return (1 - self.penalty) ** (citizen_count // capacity)
        return 0
    
    def get_satisfaction_factor_influence(self) -> object:
        return SatisfactionFactors(1.0, 1.0, 1.0, 1.0)

    def get_income(self, citizen_count: int) -> int:
        return 0

    @abstractmethod
    def get_expenses(self) -> int:
        pass

class School(BasicBuilding):
    def __init__(self, weight, count):
        super().__init__("Schule", 5000, weight, count, 10000, 6)
    
    def get_expenses(self) -> int:
        return 200 * self.count
    
    def get_income(self, citizen_count: int) -> int:
        return 0
    
    @staticmethod
    def get_build_cost() -> int:
        return 2000
    

class ElectiveBuilding(Building):
    def __init__(self, name):
        super().__init__(name, 0)
        self.weight = 0.1

    @abstractmethod
    def get_income(self, citizen_count) -> int:
        return 0
    
    def calculate_weight(self):
        return self.count * self.weight