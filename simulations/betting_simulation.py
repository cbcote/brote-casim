from game import BlackjackGame

class BettingSimulation:
    def __init__(self, initial_balance, strategy):
        self.initial_balance = initial_balance
        self.strategy = strategy
        self.game = BlackjackGame(initial_balance)

    def run_simulation(self, num_rounds):
        results = []
        for _ in range(num_rounds):
            bet_amount = self.strategy.decide_bet(self.game.player.balance)
            self.game.player.place_bet(bet_amount)
            self.game.play_round()
            results.append(self.game.player.balance)
        return results
