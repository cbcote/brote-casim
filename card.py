class Card:
    def __init__(self, suit: str, rank: str) -> None:
        """
        Initialize a card object
        
        Args:
            suit (str): The suit of the card
            rank (str): The rank of the card
        
        Attributes:
            suit (str): The suit of the card
            rank (str): The rank of the card
            value (int): The value of the card
        
        Returns:
            None
        """
        self.suit = suit
        self.rank = rank
        self.value = self.determine_value()

    def __str__(self) -> str:
        return f"{self.rank} of {self.suit}"

    def determine_value(self) -> int:
        """
        Return the value of the card
        
        Returns:
            int: The value of the card
        """
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)
