from abc import ABCMeta, abstractmethod

class Building(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_expenses(self) -> int:
        pass

    @abstractmethod
    def get_income(self) -> int:
        pass

ERR_MARGIN = 100

class BasicBuilding(Building):
    def __init__(self, name, per_population, weight, count):
        super().__init__(name)
        self.per_population = per_population
        self.weight = weight
        self.count = count
    
    def get_satisfaction_penalty(self, citizen_count) -> int:
        capacity = self.count * self.per_population
        if capacity + ERR_MARGIN < citizen_count:
            return (citizen_count // capacity) * self.weight
            

class School(BasicBuilding):
    def __init__(self, weight, count):
        super().__init__("Schule", 5000, weight, count)
    
    def get_expenses(self) -> int:
        return 1000 * self.count
    
    def get_income(self) -> int:
        return 0 * self.count
    