import random
from card import Card

class Deck:
    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

    def __init__(self):
        """Initialize a deck object with 52 cards in it and shuffle it"""
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck of cards"""
        random.shuffle(self.cards)

    def deal_card(self):
        """Deal a card from the deck"""
        return self.cards.pop()
