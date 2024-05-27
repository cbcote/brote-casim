from hand import Hand

class Player:
    def __init__(self, balance: int) -> None:
        """
        Initialize a player object with a starting balance
        
        Args:
            balance (int): The starting balance of the player
        
        Attributes:
            hand (Hand): The player's hand
            balance (int): The player's balance
            bet (int): The player's bet
        
        Returns:
            None
        """
        self.hand = Hand()
        self.balance = balance
        self.bet = 0

    def place_bet(self, amount):
        """
        Place a bet for the player
        
        Args:
            amount (int): The amount to bet
        """
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.bet = amount
        self.balance -= amount

    def win_bet(self):
        """Win the bet and add the winnings to the balance"""
        self.balance += self.bet * 2
        self.bet = 0

    def lose_bet(self):
        """Lose the bet and reset the bet amount to 0"""
        self.bet = 0

    def push(self):
        """Push the bet and reset the bet amount to 0"""
        self.balance += self.bet
        self.bet = 0
