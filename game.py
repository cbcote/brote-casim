from deck import Deck
from player import Player
from dealer import Dealer
from hand import Hand
import random

class BlackjackGame:
    def __init__(self, player_balance):
        """
        Initialize a Blackjack game with a player and a dealer
        
        Args:
            player_balance (int): The starting balance of the player
        
        Attributes:
            deck (Deck): The deck of cards
            player (Player): The player
            dealer (Dealer): The dealer
        """
        self.deck = Deck()
        self.player = Player(player_balance)
        self.dealer = Dealer()

    def play_round(self):
        """Play a round of Blackjack"""
        self.deck = Deck()  # Reinitialize and shuffle deck
        self.player.hand = Hand()
        self.dealer.hand = Hand()

        self.player.place_bet(10)  # For simplicity, bet is fixed here

        # Initial deal
        self.player.hand.add_card(self.deck.deal_card())
        self.player.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())

        # Show cards
        self.show_some()

        # Check for blackjack
        if self.check_for_blackjack():
            return

        while self.player.hand.value < 21:
            # Prompt player to hit or stand
            action = input("Hit or Stand? (h/s): ")
            if action.lower() == 'h':
                # Player hits
                self.player.hand.add_card(self.deck.deal_card())
                # Show cards
                self.show_some()
                # Check if player busts
                if self.player.hand.value > 21:
                    self.player_busts()
                    return
            else:
                break
        
        # Dealer's turn
        self.dealer.play(self.deck)
        # Show all cards
        self.show_all()

        # Check for dealer bust
        if self.dealer.hand.value > 21:
            self.dealer_busts()
        else:
            self.compare_hands()

    def check_for_blackjack(self):
        # Check for player blackjack
        if self.player.hand.value == 21:
            # Check for dealer blackjack
            if self.dealer.hand.value == 21:
                self.player.push()
            else:
                self.player.win_bet()
            return True
        return False

    def player_busts(self):
        """Handle player busting"""
        print("Player busts!")
        self.player.lose_bet()

    def dealer_busts(self):
        """Handle dealer busting"""
        print("Dealer busts!")
        self.player.win_bet()

    def compare_hands(self):
        """Compare the player's and dealer's hands and determine the winner"""
        if self.player.hand.value > self.dealer.hand.value:
            self.player.win_bet()
        elif self.player.hand.value < self.dealer.hand.value:
            self.player.lose_bet()
        else:
            self.player.push()

    def show_some(self):
        """Show the player's hand and one of the dealer's cards"""
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print('', self.dealer.hand.cards[1])
        print("\nPlayer's Hand:", *self.player.hand.cards, sep='\n ')

    def show_all(self):
        """Show all cards in the player's and dealer's hands"""
        print("\nDealer's Hand:", *self.dealer.hand.cards, sep='\n ')
        print("Dealer's Hand =", self.dealer.hand.value)
        print("\nPlayer's Hand:", *self.player.hand.cards, sep='\n ')
        print("Player's Hand =", self.player.hand.value)
