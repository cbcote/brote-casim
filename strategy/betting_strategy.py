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
        Initialize a flat betting strategy with a fixed bet amount for each round.
        
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
        return min(self.fixed_bet, balance)



class MartingaleStrategy(BettingStrategy):
    def __init__(self, initial_bet: int) -> None:
        """
        Initialize a Martingale betting strategy with an initial bet amount
        
        Martingale is a betting strategy that doubles the bet after each loss
        and resets the bet to the initial amount after each win. This is a
        simple example and there are many variations of the Martingale strategy.
        
        Args:
            initial_bet (int): The initial bet amount
        """
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
            self.current_bet = min(self.current_bet * 2, balance)
        else:
            self.current_bet = min(self.initial_bet, balance)
        return self.current_bet

    def record_outcome(self, outcome: str) -> None:
        """
        Record the outcome of the previous round
        
        Args:
            outcome (str): The outcome of the previous round ('win' or 'lose')
        """
        self.last_outcome = outcome



class PercentageBettingStrategy(BettingStrategy):
    def __init__(self, percentage: float) -> None:
        """
        Initialize a percentage betting strategy with a percentage of the balance to bet
        
        Args:
            percentage (float): The percentage of the balance to bet
        """
        self.percentage = percentage

    def decide_bet(self, balance: int) -> int:
        """
        Decide the bet amount based on the current balance and percentage
        
        Args:
            balance (int): The current balance of the player
        
        Returns:
            int: The bet amount
        """
        return min(int(balance * self.percentage), balance)


class FibonacciStrategy(BettingStrategy):
    def __init__(self) -> None:
        self.fib_sequence = [1, 1]
        self.current_index = 0
        self.last_outcome = None

    def decide_bet(self, balance: int) -> int:
        if self.last_outcome == 'lose':
            self.current_index = min(self.current_index + 1, len(self.fib_sequence) - 1)
        elif self.last_outcome == 'win':
            self.current_index = max(self.current_index - 1, 0)

        if self.current_index >= len(self.fib_sequence):
            self.fib_sequence.append(self.fib_sequence[-1] + self.fib_sequence[-2])

        return min(self.fib_sequence[self.current_index], balance)

    def record_outcome(self, outcome: str) -> None:
        self.last_outcome = outcome