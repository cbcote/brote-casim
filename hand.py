from card import Card


class Hand:
    def __init__(self):
        """Initialize a hand object with no cards in it"""
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card: Card):
        """
        Add a card to the hand and adjust the value of the hand accordingly
        
        Args:
            card (Card): The card to add to the hand
        
        Returns:
            None
        """
        self.cards.append(card)
        self.value += card.value
        if card.rank == 'A':
            self.aces += 1
        self.adjust_for_ace()

    def adjust_for_ace(self):
        """Adjust the value of the hand if there are aces and the value is over 21"""
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def calculate_value(self):
        """Calculate the value of the hand based on the cards in it"""
        self.value = sum(card.value for card in self.cards)
        self.adjust_for_ace()
