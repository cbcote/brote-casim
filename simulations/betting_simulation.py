from game import BlackjackGame
from strategy.betting_strategy import BettingStrategy, MartingaleStrategy
from typing import List, Tuple

class BettingSimulation:
    def __init__(self, initial_balance: int, strategy: BettingStrategy, use_basic_strategy=False, num_decks=6) -> None:
        """
        Initialize a betting simulation with an initial balance and a betting strategy
        
        Args:
            initial_balance (int): The initial balance of the player
            strategy (BettingStrategy): The betting strategy to use
            use_basic_strategy (bool): Whether to use basic strategy or not
            num_decks (int): Number of decks to use in the game
        
        Attributes:
            initial_balance (int): The initial balance of the player
            strategy (BettingStrategy): The betting strategy to use
            game (BlackjackGame): The Blackjack game
            num_decks (int): Number of decks to use in the game
        """
        self.initial_balance = initial_balance
        self.strategy = strategy
        self.use_basic_strategy = use_basic_strategy
        self.num_decks = num_decks

    def run_simulation(self, num_rounds: int) -> Tuple[List[int], List[int]]:
        """
        Run a betting simulation for a given number of rounds
        
        Args:
            num_rounds (int): The number of rounds to simulate
        
        Returns:
            Tuple[List[int], List[int]]: A tuple containing two lists - 
                                         one with player balances after each round and 
                                         another with the bet amounts for each round
        """
        bets = []
        results = []
        game = BlackjackGame(self.initial_balance, num_decks=self.num_decks, use_basic_strategy=self.use_basic_strategy) # Initialize a Blackjack game
        
        for round_num in range(num_rounds):
            if game.player.balance <= 0:
                print(f"Simulation stopped at round {round_num} due to insufficient balance.")
                break
            
            bet_amount = self.strategy.decide_bet(game.player.balance)
            bets.append(bet_amount)

            try:
                game.play_round(bet_amount)
            except ValueError as e:
                print(e)
                break

            if isinstance(self.strategy, MartingaleStrategy):
                if game.player.hand.value > 21:
                    self.strategy.record_outcome('lose')
                elif game.dealer.hand.value > 21 or game.player.hand.value > game.dealer.hand.value:
                    self.strategy.record_outcome('win')
                elif game.player.hand.value < game.dealer.hand.value:
                    self.strategy.record_outcome('lose')
                else:
                    self.strategy.record_outcome('push')  # This might reset the bet in some implementations

            print(f"Round {round_num}: Balance = {game.player.balance}")
            results.append(game.player.balance)
        
        return results, bets
