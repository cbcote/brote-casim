import random
from card import Card

class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self, num_decks=6):
        """Initialize a deck object with 52 cards in it and shuffle it"""
        self.num_decks = num_decks
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()
    
    def _create_deck(self):
        """Create a deck of cards"""
        return [Card(suit, rank) for suit in self.suits for rank in self.ranks] * self.num_decks

    def shuffle(self):
        """Shuffle the deck of cards"""
        random.shuffle(self.cards)

    def deal_card(self):
        """Deal a card from the deck"""
        if len(self.cards) == 0:
            self.cards = self._create_deck()
            self.shuffle()
        return self.cards.pop()
    
    def cards_remaining(self):
        """Return the number of cards remaining in the deck"""
        return len(self.cards)
