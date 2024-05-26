from game import BlackjackGame
from strategy import BettingStrategy

from typing import List

class BettingSimulation:
    def __init__(self, initial_balance: int, strategy: BettingStrategy) -> None:
        """
        Initialize a betting simulation with an initial balance and a betting strategy
        
        Args:
            initial_balance (int): The initial balance of the player
            strategy (BettingStrategy): The betting strategy to use
        
        Attributes:
            initial_balance (int): The initial balance of the player
            strategy (BettingStrategy): The betting strategy to use
            game (BlackjackGame): The Blackjack game
        """
        self.initial_balance = initial_balance
        self.strategy = strategy
        self.game = BlackjackGame(initial_balance) # Initialize a Blackjack game

    def run_simulation(self, num_rounds: int) -> List[int]:
        """
        Run a betting simulation for a given number of rounds
        
        Args:
            num_rounds (int): The number of rounds to simulate
        
        Returns:
            list: A list of player balances after each round
        """
        # Reset player balance
        results = []
        # Run simulation
        for _ in range(num_rounds):
            # Place bet and play round
            bet_amount = self.strategy.decide_bet(self.game.player.balance)
            # If bet_amount is None, the strategy decided to skip the round
            self.game.player.place_bet(bet_amount)
            # Play round
            self.game.play_round()
            # Update balance
            results.append(self.game.player.balance)
        return results
