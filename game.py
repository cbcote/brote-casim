from deck import Deck
from player import Player
from dealer import Dealer
import random

class BlackjackGame:
    def __init__(self, player_balance):
        self.deck = Deck()
        self.player = Player(player_balance)
        self.dealer = Dealer()

    def play_round(self):
        self.deck = Deck()  # Reinitialize and shuffle deck
        self.player.hand = Hand()
        self.dealer.hand = Hand()

        self.player.place_bet(10)  # For simplicity, bet is fixed here

        # Initial deal
        self.player.hand.add_card(self.deck.deal_card())
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())

        self.show_some()

        if self.check_for_blackjack():
            return

        while self.player.hand.value < 21:
            action = input("Hit or Stand? (h/s): ")
            if action.lower() == 'h':
                self.player.hand.add_card(self.deck.deal_card())
                self.show_some()
                if self.player.hand.value > 21:
                    self.player_busts()
                    return
            else:
                break

        self.dealer.play(self.deck)
        self.show_all()

        if self.dealer.hand.value > 21:
            self.dealer_busts()
        else:
            self.compare_hands()

    def check_for_blackjack(self):
        if self.player.hand.value == 21:
            if self.dealer.hand.value == 21:
                self.player.push()
            else:
                self.player.win_bet()
            return True
        return False

    def player_busts(self):
        print("Player busts!")
        self.player.lose_bet()

    def dealer_busts(self):
        print("Dealer busts!")
        self.player.win_bet()

    def compare_hands(self):
        if self.player.hand.value > self.dealer.hand.value:
            self.player.win_bet()
        elif self.player.hand.value < self.dealer.hand.value:
            self.player.lose_bet()
        else:
            self.player.push()

    def show_some(self):
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print('', self.dealer.hand.cards[1])
        print("\nPlayer's Hand:", *self.player.hand.cards, sep='\n ')

    def show_all(self):
        print("\nDealer's Hand:", *self.dealer.hand.cards, sep='\n ')
        print("Dealer's Hand =", self.dealer.hand.value)
        print("\nPlayer's Hand:", *self.player.hand.cards, sep='\n ')
        print("Player's Hand =", self.player.hand.value)
