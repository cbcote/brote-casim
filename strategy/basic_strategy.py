from hand import Hand
from card import Card


class BasicStrategy:
    def decide_move(self, player_hand: Hand, dealer_upcard: Card) -> str:
        """
        Decide the move based on the player's hand and the dealer's upcard
        
        Args:
            player_hand (Hand): The player's hand
            dealer_upcard (Card): The dealer's upcard
        """
        player_value = player_hand.value
        dealer_value = dealer_upcard.value
        
        # Hard totals
        if player_value >= 17:
            return 'stand'
        
        if player_value <= 11:
            return 'hit'
        
        if player_value == 12:
            if dealer_value in [4, 5, 6]:
                return 'stand'
            else:
                return 'hit'
        # Hard 13-16
        if player_value in [13, 14, 15, 16]:
            if dealer_value in [2, 3, 4, 5, 6]:
                return 'stand'
            else:
                return 'hit'

        # Soft totals (containing an Ace)
        if player_hand.aces:
            # Soft 13-15
            if player_value == 18:
                if dealer_value in [9, 10, 11]:
                    return 'hit'
                else:
                    return 'stand'
            # Soft 16-18
            if player_value in [19, 20, 21]:
                return 'stand'
            # Soft 17
            if player_value <= 17:
                return 'hit'

        return 'stand'  # Default action
