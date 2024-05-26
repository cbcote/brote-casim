class BettingStrategy:
    def decide_bet(self, balance: int) -> int:
        """
        Decide the bet amount based on the current balance
        
        Args:
            balance (int): The current balance of the player
        
        Returns:
            int: The bet amount
        """
        raise NotImplementedError("This method should be overridden by subclasses.")

class FlatBettingStrategy(BettingStrategy):
    def __init__(self, fixed_bet: int) -> None:
        """
        Initialize a flat betting strategy with a fixed bet amount
        
        Args:
            fixed_bet (int): The fixed bet amount
        
        Attributes:
            fixed_bet (int): The fixed bet amount
        """
        self.fixed_bet = fixed_bet

    def decide_bet(self, balance: int) -> int:
        """
        Decide the bet amount based on the current balance
        
        Args:
            balance (int): The current balance of the player
        
        Returns:
            int: The fixed bet amount
        """
        return self.fixed_bet

class MartingaleStrategy(BettingStrategy):
    def __init__(self, initial_bet: int) -> None:
        """Initialize a Martingale betting strategy with an initial bet amount"""
        self.initial_bet = initial_bet
        self.current_bet = initial_bet
        self.last_outcome = None

    def decide_bet(self, balance: int) -> int:
        """
        Decide the bet amount based on the current balance and previous outcome
        
        Args:
            balance (int): The current balance of the player
        
        Returns:
            int: The bet amount
        """
        if self.last_outcome == 'lose':
            self.current_bet *= 2
        else:
            self.current_bet = self.initial_bet
        return self.current_bet

    def record_outcome(self, outcome: str) -> None:
        """
        Record the outcome of the previous round
        
        Args:
            outcome (str): The outcome of the previous round ('win' or 'lose')
        """
        self.last_outcome = outcome
