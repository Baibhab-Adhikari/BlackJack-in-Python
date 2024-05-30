import unittest
from unittest import mock
from game_classes_functions import Card, Deck, Hand, Chips, take_bet, hit, hit_or_stand, show_some, show_all, \
    player_busts, player_wins, dealer_busts, dealer_wins, push


class TestCard(unittest.TestCase):
    def test_card_creation(self):
        card = Card('Hearts', 'Two')
        self.assertEqual(card.suit, 'Hearts')
        self.assertEqual(card.rank, 'Two')
        self.assertEqual(card.value, 2)

    def test_card_str(self):
        card = Card('Hearts', 'Two')
        self.assertEqual(str(card), 'Two of Hearts')


class TestDeck(unittest.TestCase):
    def test_deck_creation(self):
        deck = Deck()
        self.assertEqual(len(deck.deck), 52)
        self.assertEqual(str(deck.deck[0]), 'Two of Hearts')

    def test_shuffle(self):
        deck = Deck()
        cards_before_shuffle = deck.deck.copy()
        deck.shuffle_cards()
        self.assertNotEqual(deck.deck, cards_before_shuffle)

    def test_deal_card(self):
        deck = Deck()
        card = deck.deal_card()
        self.assertIsInstance(card, Card)
        self.assertEqual(len(deck.deck), 51)


class TestHand(unittest.TestCase):
    def test_hand_creation(self):
        hand = Hand()
        self.assertEqual(len(hand.cards), 0)
        self.assertEqual(hand.value, 0)
        self.assertEqual(hand.aces, 0)

    def test_add_card(self):
        hand = Hand()
        card = Card('Hearts', 'Ace')
        hand.add_card(card)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(hand.value, 11)
        self.assertEqual(hand.aces, 1)

    def test_adjust_for_ace(self):
        hand = Hand()
        card1 = Card('Hearts', 'Ace')
        card2 = Card('Clubs', 'Ten')
        card3 = Card('Diamonds', 'Ace')
        hand.add_card(card1)
        hand.add_card(card2)
        hand.add_card(card3)
        hand.adjust_for_ace()
        self.assertEqual(hand.value, 22)  # Ace adjusted from 11 to 1


class TestChips(unittest.TestCase):
    def test_chips_creation(self):
        chips = Chips()
        self.assertEqual(chips.total, 100)
        self.assertEqual(chips.bet, 0)

    def test_win_bet(self):
        chips = Chips()
        chips.bet = 10
        chips.win_bet()
        self.assertEqual(chips.total, 110)

    def test_lose_bet(self):
        chips = Chips()
        chips.bet = 10
        chips.lose_bet()
        self.assertEqual(chips.total, 90)



class TestFunctions(unittest.TestCase):
    @mock.patch('builtins.input', side_effect=['50'])
    def test_take_bet(self, mock_input):
        chips = Chips()
        input_values = ['50']


if __name__ == '__main__':
    unittest.main()
