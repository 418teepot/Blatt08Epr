from abc import ABCMeta, abstractmethod
from municipality import Municipality

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
        income_per_person = self.construction_cost / current_population + 0.1
        income = income_per_person * current_population
        return income_per_person, income 
    

ERR_MARGIN = 100

class BasicBuilding(Building):
    def __init__(self, name, construction_cost, build_time, count, population_increment):
        super().__init__(name, construction_cost, build_time)
        self.population_increment = population_increment
        self.pos_weight = 0.05 # should we make it set and private?
        self.weight_penalty = 0.05
        self.count = count
    
    """def get_satisfaction_penalty(self, citizen_count) -> int:
        capacity = self.count * self.population_increment
        if capacity + ERR_MARGIN < citizen_count:
            self.count += 1
            return (citizen_count // capacity) * self.weight"""

    def build(self, citizen_count, balance):
        # Check if enough buildings are constructed proportional to the population
        target_number = citizen_count // self.population_increment
        if self.count < target_number:
            super().try_construct(balance)
        else:


    def get_income(self, citizen_count) -> int:
        return super().get_income(citizen_count)
    
    def calculate_weight(self, target_number):
        # Calculate the weight of the building on citizen satisfaction
        if self.count >= target_number:
            return self.pos_weight * self.count
        else:
            return max(0, self.pos_weight - self.weight_penalty * (target_number - self.count))
        

"""class School(BasicBuilding):
    def __init__(self, weight, count):
        super().__init__("Schule", 5000, weight, count)
    
    def get_expenses(self) -> int:
        return 1000 * self.count
    
    def get_income(self) -> int:
        return 0 * self.count"""
    

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