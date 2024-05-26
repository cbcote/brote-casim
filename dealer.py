from hand import Hand

class Dealer:
    def __init__(self):
        self.hand = Hand()

    def play(self, deck):
        while self.hand.value < 17:
            self.hand.add_card(deck.deal_card())

    def is_hitting(self):
        return self.hand.value < 17
