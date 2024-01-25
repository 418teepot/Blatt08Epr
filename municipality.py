from citizens import Citizens
from building import Building, BasicBuilding

class Municipality:
    def __init__(self):
        self.name = "Epic Fail City xD"
        self.citizens = Citizens(10000)
        self.buildings = []
        self.balance = 100_000
        self.tax_rate = 0.1
        self.month = 0
    
    def simulate_one_round(self):
        """1. Taxes - (Incomes)
           2. Random Events (?)
           3. Spieler einstellungen Vornehmen
           4. Bezahlen der Kosten
           5. Gebäude / Effekte Simulieren?
           6. Stats -> Bürgerzufriedenheit
           7. Abwandern / Hinzukommen / Gleichbleibt
        """
        # 1. Taxes & Income
        print(f'Starting simulataion of round {self.month}')
        self.debug_print_stats()
        self.balance += self.citizens.collect_taxes(self.tax_rate)
        for building in self.buildings:
            self.balance += building.get_income()
            self.balance -= building.get_expenses()
        self.debug_print_stats()
    
    def debug_print_stats(self):
        print(f'Citizens: {self.citizens}')
        print(f'Balance: {self.balance}')
