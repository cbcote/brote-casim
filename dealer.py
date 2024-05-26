from hand import Hand
from deck import Deck

class Dealer:
    def __init__(self):
        """Initialize a dealer object"""
        self.hand = Hand()

    def play(self, deck: Deck) -> None:
        """
        Play the dealer's turn
        
        Args:
            deck (Deck): The deck of cards
        
        Returns:
            None
        """
        while self.hand.value < 17:
            self.hand.add_card(deck.deal_card())

    def is_hitting(self):
        return self.hand.value < 17
