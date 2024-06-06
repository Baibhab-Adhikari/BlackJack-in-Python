"""
Main game logic for BlackJack game.
"""

# Global variables and imports
import game_classes_functions as gcf


def main():
    while True:
        game = gcf.BlackjackGame()  # initialize the game
        # welcome statement
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
            Dealer hits until he/she reaches 17. Aces count as 1 or 11.')

        # prompt player for bet
        gcf.take_bet(game.chips)  # call the take bet function

        # Show cards (but keep one dealer card hidden)
        gcf.show_some(game.player_hand, game.dealer_hand)

        while game.playing:
            # prompt the player for next action
            gcf.hit_or_stand(game.deck, game.player_hand, game)  # call the hit or stand function
            # Show cards (but keep one dealer card hidden)
            gcf.show_some(game.player_hand, game.dealer_hand)

            # If player's hand exceeds 21,
            if game.player_hand.value > 21:
                gcf.player_busts(game.player_hand, game.dealer_hand, game.chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 (soft 17 rule)
        if game.player_hand.value <= 21:

            while game.dealer_hand.value < 17:
                gcf.hit(game.deck, game.dealer_hand)  # calling the hit function for the dealer

            # Show all cards
            gcf.show_all(game.player_hand, game.dealer_hand)

            # Run different winning scenarios
            if game.dealer_hand.value > 21:
                gcf.dealer_busts(game.player_hand, game.dealer_hand, game.chips)

            elif game.dealer_hand.value > game.player_hand.value:
                gcf.dealer_wins(game.player_hand, game.dealer_hand, game.chips)

            elif game.dealer_hand.value < game.player_hand.value:
                gcf.player_wins(game.player_hand, game.dealer_hand, game.chips)

            else:
                gcf.push(game.player_hand, game.dealer_hand)

        # display the total hand value of the player
        print("Total cards value in hand: {}".format(game.player_hand.value))

        # display the total chips of the player
        print("Player has {} chips in total...".format(game.chips.total))

        # Ask to play again

        while True:

            new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

            if new_game[0].lower() == 'y':
                game.reset_game()  # reset the game state
                break
            elif new_game[0].lower() == 'n':
                print("Thanks for playing! Exiting the game....")
                return  # exit the main function
            else:
                print("Please enter either 'y' or 'n'.")


# running the main script
if __name__ == '__main__':
    main()
