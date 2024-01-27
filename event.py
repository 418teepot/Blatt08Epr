from satisfaction_factors import SatisfactionFactors


class Event:
    def __init__(self, name: str, description: str, satisfaction_factors_effect: SatisfactionFactors, balance_effect: int):
        self.name = name
        self.description = description
        self.satisfaction_factors = satisfaction_factors_effect
        self.balance_effect = balance_effect