import random
from citizens import Citizens
from event import Event
from satisfaction_factors import SatisfactionFactors

class Municipality:
    def __init__(self):
        self.name = "Metropolis"
        self.citizens = Citizens(10000)
        self.buildings = []
        self.balance = 100_000
        self.tax_rate = 0.1
        self.month = 0
        self.enable_immigration = True
    
    def simulate_one_round(self):
        self.balance += self.citizens.collect_taxes(self.tax_rate)
        for building in self.buildings:
            self.balance += building.get_income()
            self.balance -= building.get_expenses()

        satisfaction = self.citizens.get_total_satisfaction(self.tax_rate, self.buildings)
        self.sim_migration(satisfaction)
    
    def satisfaction(self) -> float:
        return self.citizens.get_total_satisfaction(self.tax_rate, self.buildings)
        
    def debug_print_stats(self):
        print(f'Citizens: {self.citizens}')
        print(f'Balance: {self.balance}')

    def add_building(self, index: int):
        self.balance -= self.buildings[index].get_build_cost()
        self.buildings[index].build()
    
    def sim_migration(self, satisfaction: float):
        rate = self.citizens.determine_migration(satisfaction)
        if rate > 0:
            if self.enable_immigration:
                self.citizens += rate
        else:
            self.citizens += rate
    
    def get_events(self) -> object:
        events = [Event("Earthquake", "Whoopsie", SatisfactionFactors(0.85, 0.85, 0.95, 1.0), -2500)]
        if random.randint(0, 20) < 5:
            return random.choice(events)