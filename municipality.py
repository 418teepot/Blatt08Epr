import random
from citizens import Citizens
from event import Event
from satisfaction_factors import SatisfactionFactors
from building import BusStation, CoalPowerPlant, ElectircityGrid, FitnessStudio, Hospital, Kindergarden, Kino, PoliceStation, School, TennisCourt, University

class Municipality:
    def __init__(self):
        self.name = "Metropolis"
        self.citizens = Citizens(10000)
        self.buildings = []
        self.current_event = None
        self.balance = 100_000
        self.tax_rate = 0.1
        self.month = 0
        self.enable_immigration = True

        # Initialize the Building
        self.buildings.append(School(0.05, 2))
        self.buildings.append(PoliceStation(0.06, 2))
        self.buildings.append(ElectircityGrid(0.07, 2))
        self.buildings.append(BusStation(0.4, 10))
        self.buildings.append(University())
        self.buildings.append(CoalPowerPlant())
        self.buildings.append(FitnessStudio())
        self.buildings.append(Kindergarden())
        self.buildings.append(Hospital())
        self.buildings.append(Kino())
        self.buildings.append(TennisCourt())
    
    def simulate_one_round(self):
        self.balance += self.citizens.collect_taxes(self.tax_rate)
        for building in self.buildings:
            self.balance += building.get_income(self.citizens.count)
            self.balance -= building.get_expenses()
        if self.current_event:
            self.balance += self.current_event.balance_effect

        satisfaction = self.get_satisfaction()
        self.sim_migration(satisfaction)
        self.current_event = None
        self.month += 1
        self.citizens.count = int(self.citizens.count)
        self.balance = int(self.balance)
        self.create_event()
    
    def get_satisfaction(self) -> float:
        return self.citizens.get_total_satisfaction(self.tax_rate, self.buildings, self.current_event)
    
    def get_satisfaction_factors(self) -> object:
        return self.citizens.get_satisfaction_factors(self.buildings, self.current_event)
        
    def debug_print_stats(self):
        print(f'Citizens: {self.citizens}')
        print(f'Balance: {self.balance}')

    def add_building(self, name: str):
        for building in self.buildings:
            if building.name == name:
                building.build()
                self.balance -= building.get_build_cost()
    
    def demolish_building(self, name: str):
        for building in self.buildings:
            if building.name == name:
                building.destroy()
    
    def sim_migration(self, satisfaction: float):
        rate = self.citizens.determine_migration(satisfaction)
        if rate > 0:
            if self.enable_immigration:
                self.citizens.count += rate
        else:
            self.citizens.count += rate
    
    def create_event(self):
        events = [Event("Earthquake", "Whoopsie", SatisfactionFactors(0.85, 0.85, 0.95, 1.0), -2500),
                  Event("Concert", "Yaaaay", SatisfactionFactors(0.99, 0.99, 1.0, 1.20), 2000)]
        if random.randint(0, 6) < 5:
            self.current_event = random.choice(events)
        else:
            self.current_event = None
    
    def predict_migration(self) -> int:
        return self.citizens.determine_migration(self.get_satisfaction())