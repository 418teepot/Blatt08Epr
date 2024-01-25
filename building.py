from abc import ABCMeta, abstractmethod

from citizens import SatisfactionFactors

class Building(metaclass=ABCMeta):
    def __init__(self, name, construction_cost, build_time, count):
        self.name = name
        self.construction_cost = construction_cost 
        self.build_time = build_time
        self.count = 0

    @abstractmethod
    def try_construct(self, balance) -> int:
          if self.construction_cost <= balance.get_balance():
             self.construction_cost = balance.withdraw(self.construction_cost) # 
             self.count += 1
          else:
             print(f"Insufficient balance to construct {self.name}.")

    
    @abstractmethod
    def get_income(self) -> int:
        pass

ERR_MARGIN = 100

class BasicBuilding(Building, metaclass=ABCMeta):
    def __init__(self, name, per_population, penalty, count):
        super().__init__(name)
        self.per_population = per_population
        self.penalty = penalty
    
    def get_satisfaction_penalty(self, citizen_count) -> int:
        capacity = self.count * self.per_population
        if capacity + ERR_MARGIN < citizen_count:
            return (citizen_count // capacity) * self.weight
            return (1 - self.penalty) ** (citizen_count // capacity)
        return 0
    
    @abstractmethod
    def update_satisfaction(self, factors: SatisfactionFactors) -> SatisfactionFactors:
        pass

    @abstractmethod
    def get_income(self) -> int:
        pass

    @abstractmethod
    def get_expenses(self) -> int:
        pass

class School(BasicBuilding):
    def __init__(self, weight, count):
        super().__init__("Schule", 5000, weight, count)
    
    def get_expenses(self) -> int:
        return 1000 * self.count
    
    def get_income(self) -> int:
        return 0 * self.count
    

class ElectiveBuilding(Building):
    def __init__(self, name, construction_cost, build_time):
        super().__init__(name, construction_cost, build_time)
        self.weight = 0.1

    def build(self, balance):
        super().try_construct(balance)

    def get_income(self, citizen_count) -> int:
        return super().get_income(citizen_count)
    
    def calculate_weight(self):
        return self.count * self.weight