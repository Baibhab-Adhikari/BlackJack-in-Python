"""
BlackJack Game in Python, by <Baibhab Adhikari>
"""

# Global variables and imports
import random


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    """
    A class to represent a card
    """

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    """
    A class to represent a deck
    """

    def __init__(self):
        self.deck = []  # list to store all the card objects

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit, rank)  # using the card class to create 52 cards
                self.deck.append(created_card)  # append to the list of card objects

    def shuffle_cards(self) -> None:
        """
        Shuffle the cards randomly
        :return: None
        """
        random.shuffle(self.deck)

    def deal_card(self) -> object:
        """
        Deal a card from the deck
        :return: A card object from the deck 
        """
        return self.deck.pop()

    def __str__(self):
        return f"There are {len(self.deck)} cards in the deck"


class Hand:
    """
    A class to represent a hand containing cards
    """

    def __init__(self):
        self.cards = []  # stores a list of cards currently in hand
        self.value = 0  # start with total value = 0
        self.aces = 0  # keeping track of number of Ace cards in hand

    def add_card(self, card) -> None:
        """
        Add a card to the cards list in hand
        :param card: object
        :return: None
        """
        self.cards.append(card)
        self.value += values[card.rank]  # add the value of the cards in hand
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces

    def adjust_for_ace(self) -> None:
        """
        Adjust the value of the hand for ace cards
        :return: None
        """

        if self.value > 21 and self.aces:  # if total value > 21 and Ace is present
            self.value -= 10  # reduce 10 from total value (Ace value is 1 now)
            self.aces -= 1  # remove one Ace from the hand


class Chips:
    """
    A class to represent a chips of the player
    """

    def __init__(self):
        self.total = 100  # default total chip value of 100
        self.bet = 0

    def win_bet(self) -> None:
        """
        Add bet to total chips when player wins.
        :return: None
        """
        self.total += self.bet  # add bet to total

    def lose_bet(self) -> None:
        """
        Add bet to total chips when player loses.
        :return: None
        """
        self.total -= self.bet  # subtract bet from total


def take_bet(chips) -> None:
    """
    Take a bet from the player.
    :param chips: Chips object
    :return: None
    """

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet "))

        except ValueError:
            print('Sorry, a bet must be an integer!')

        else:
            if chips.bet > chips.total:
                print('Sorry, the bet cannot be greater than the available chips!')
            else:
                break


def hit(deck, hand) -> None:
    """
    Prompt the player to hit or stand.
    :param deck: Deck object
    :param hand: Hand object
    :return: None
    """
    hand.add_card(deck.deal_card())  # add card in hand
    hand.adjust_for_ace()  # adjust ace value based on current card value in hand


def hit_or_stand(deck, hand, game) -> None:
    """
    Hit or stand
    :param deck: Deck object
    :param hand: Hand object
    :param game: Game object
    :return: None
    """

    while True:

        x = input("Would you like to Hit or Stand? Enter 'h' or 's': ")

        if not x:  # Check if input is empty
            print('Sorry, you have to enter a valid character!')
            continue

        if x[0].lower() == "h":
            hit(deck, hand)  # calling the hit function

        elif x[0].lower() == "s":
            print("Player stands! Dealer is playing...")
            game.playing = False  # dealer starts playing now
        else:
            print('Sorry, you have to enter either h or s!')
            continue
        break


def show_some(player, dealer) -> None:
    """
    Show some cards
    :param player: Hand object
    :param dealer: Hand object
    :return: None
    """
    print("\nDealer's Hand:")  # dealer shows only one card
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')  # player shows all the cards


def show_all(player, dealer) -> None:
    """
    Show all cards for both dealer and player
    :param player: Hand object
    :param dealer: Hand object
    :return: None
    """
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print(f"Dealer's Hand = {dealer.value}")
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print(f"Player's Hand ={player.value}")


def player_busts(player, dealer, chips) -> None:
    """
    Player busts if card value > 21.
    :param player: Hand object
    :param dealer: Hand object
    :param chips: Chips object
    :return: None
    """
    print("Player busts!")
    chips.lose_bet()  # call lose bet method from chips class


def player_wins(player, dealer, chips) -> None:
    """
    Player wins if card value = 21
    :param player: Hand object
    :param dealer: Hand object
    :param chips: Chips object
    :return: None
    """
    print("Player wins!")
    chips.win_bet()  # call win bet method from chips class


def dealer_busts(player, dealer, chips) -> None:
    """
    Dealer busts if card value > 21
    :param player: Hand object
    :param dealer: Hand object
    :param chips: Chips object
    :return: None
    """
    print("Dealer busts! Player WINS!!!!")
    chips.win_bet()  # calling win bet method from chips class


def dealer_wins(player, dealer, chips) -> None:
    """
    Dealer wins if card value = 21
    :param player: Hand object
    :param dealer: Hand object
    :param chips: Chips object
    :return: None
    """
    print("Dealer wins!")
    chips.lose_bet()  # calling the lose bet method from chips class


def push(player, dealer) -> None:
    """
    Player and Dealer are tied in the game
    :param player: Hand object
    :param dealer: Hand object
    :return: None
    """
    print("Dealer and Player tie! It's a push!")


class BlackjackGame:
    """
    A class to encapsulate the game state
    """
    def __init__(self):
        self.playing = True  # bool flag
        self.deck = Deck()  # make new deck
        self.deck.shuffle_cards()  # shuffle deck
        self.player_hand = Hand()  # new player
        self.dealer_hand = Hand()  # new dealer
        self.chips = Chips()  # initialize total chips (100)
        self.player_hand.add_card(self.deck.deal_card())  # deal 2 cards to player
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())  # deal 2 cards to dealer
        self.dealer_hand.add_card(self.deck.deal_card())

    def reset_game(self):
        self.deck = Deck()
        self.deck.shuffle_cards()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.playing = True
