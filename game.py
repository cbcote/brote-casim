from deck import Deck
from player import Player
from dealer import Dealer
from hand import Hand
from strategy.basic_strategy import BasicStrategy



class BlackjackGame:
    def __init__(self, player_balance: int, num_decks=6, use_basic_strategy: bool = False) -> None:
        """
        Initialize a Blackjack game with a player and a dealer
        
        Args:
            player_balance (int): The starting balance of the player
            use_basic_strategy (str): Whether to use basic strategy or not
        
        Attributes:
            deck (Deck): The deck of cards
            player (Player): The player
            dealer (Dealer): The dealer
        """
        self.deck = Deck(num_decks) # Initialize a deck
        self.player = Player(player_balance) # Initialize a player with the given balance
        self.dealer = Dealer()
        self.use_basic_strategy = use_basic_strategy
        
        # Initialize basic strategy if needed
        if self.use_basic_strategy:
            self.basic_strategy = BasicStrategy()

    def play_round(self, bet_amount: int):
        """
        Play a round of Blackjack
        
        Args:
            bet_amount (int): The amount to bet on the round
        """
        if self.deck.cards_remaining() < 15: # Arbitrary number to trigger reshuffling
            self.deck = Deck(self.deck.num_decks)  # Reshuffle the deck
        
        self.player.hand = Hand()
        self.dealer.hand = Hand()

        # Place bet
        self.player.place_bet(bet_amount)

        # Initial deal
        # Deal to player first
        self.player.hand.add_card(self.deck.deal_card())
        self.player.hand.add_card(self.deck.deal_card())
        
        # Deal to dealer
        self.dealer.hand.add_card(self.deck.deal_card())
        self.dealer.hand.add_card(self.deck.deal_card())

        # Show cards
        self.show_some()

        # Check for blackjack
        if self.check_for_blackjack():
            return

        while self.player.hand.value < 21:
            # Ask player for move
            if self.use_basic_strategy:
                # Use basic strategy
                move = self.basic_strategy.decide_move(self.player.hand, self.dealer.hand.cards[1])
                print(f"Basic Strategy suggests to {move}")

                if move == 'hit':
                    # Deal card to player
                    self.player.hand.add_card(self.deck.deal_card())
                    self.show_some()
                    
                    # Check for player bust
                    if self.player.hand.value > 21:
                        self.player_busts()
                        return
                else:
                    break
            else:
                # Placeholder for player input
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
