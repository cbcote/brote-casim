class BettingStrategy:
    def decide_bet(self, balance):
        raise NotImplementedError("This method should be overridden by subclasses.")

class FlatBettingStrategy(BettingStrategy):
    def __init__(self, fixed_bet):
        self.fixed_bet = fixed_bet

    def decide_bet(self, balance):
        return self.fixed_bet

class MartingaleStrategy(BettingStrategy):
    def __init__(self, initial_bet):
        self.initial_bet = initial_bet
        self.current_bet = initial_bet
        self.last_outcome = None

    def decide_bet(self, balance):
        if self.last_outcome == 'lose':
            self.current_bet *= 2
        else:
            self.current_bet = self.initial_bet
        return self.current_bet

    def record_outcome(self, outcome):
        self.last_outcome = outcome
