"""
Main game logic for BlackJack game.
"""

# Global variables and imports
import game_classes_functions as gcf


def main():

    while True:
        playing = True  # bool flag
        # welcome statement
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
            Dealer hits until he/she reaches 17. Aces count as 1 or 11.')

        # create and shuffle a new deck

        new_deck = gcf.Deck()
        new_deck.shuffle_cards()

        # create a player and a dealer and deal 2 cards to each

        player_hand = gcf.Hand()
        player_hand.add_card(new_deck.deal_card())  # card 1 added
        player_hand.add_card(new_deck.deal_card())  # card 2 added

        dealer_hand = gcf.Hand()
        dealer_hand.add_card(new_deck.deal_card())
        dealer_hand.add_card(new_deck.deal_card())

        # player chips setup
        player_chips = gcf.Chips()  # default value is 100

        # prompt player for bet
        gcf.take_bet(player_chips)  # call the take bet function

        # Show cards (but keep one dealer card hidden)
        gcf.show_some(player_hand, dealer_hand)

        while playing:
            # prompt the player for next action
            gcf.hit_or_stand(new_deck, player_hand)  # call the hit or stand function

            # Show cards (but keep one dealer card hidden)
            gcf.show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21,
            if player_hand.value > 21:
                gcf.player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:

            while dealer_hand.value < 17:
                gcf.hit(new_deck, dealer_hand)  # calling the hit function for the dealer

            # Show all cards
            gcf.show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                gcf.dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                gcf.dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                gcf.player_wins(player_hand, dealer_hand, player_chips)

            else:
                gcf.push(player_hand, dealer_hand)

        # display the total hand value of the player
        print("Total cards value in hand: {}".format(player_hand.value))

        # display the total chips of the player
        print("Player has {} chips in total...".format(player_chips.total))
        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        elif new_game[0].lower() == 'n':
            print("Thanks for playing! Exiting the game....")
            break
        else:
            print("Please enter either 'y' or 'n'.")
            continue


# running the main script
if __name__ == '__main__':
    main()
