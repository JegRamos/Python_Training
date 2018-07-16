class Card:
    suits = ("Hearts", "Diamonds", "Spades", "Clubs")
    values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self, value, suits):
        self.value = value
        self.suits = suits

    def __repr__(self):
        return f"{self.value} of {self.suits}"

class Deck(Card):
    STDR_DECK_NUM = 52

    def __init__(self):
        self.cards = [Card(value, suit) for suit in Card.suits for value in Card.values]

    def __repr__(self):
        return f"A Deck of {len(self.cards)} cards"

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        dealt_cards = []
        if self.count() == 0:
            raise ValueError(f"All {Deck.STDR_DECK_NUM} cards have been dealt")

        if num > self.count():
            print(f"Insufficient cards in Deck, removing {self.count()} cards instead")
            num = len(self.cards)

        while num > 0:
            dealt_cards.append(self.cards.pop(-1))
            num -= 1

        return dealt_cards

    def deal_card(self):
        card_dealt = self._deal(1)[0]
        return card_dealt

    def deal_hand(self, num):
        hand_dealt = self._deal(num)
        return hand_dealt

    def shuffle(self):
        from random import shuffle

        if self.count() < Deck.STDR_DECK_NUM:
            raise ValueError("Only Full Decks can be shuffled")
        else:
            shuffle(self.cards)

        return self.cards

deck1 = Deck()
print(deck1.count())
print(deck1.shuffle())

print(deck1.deal_hand(5))
print(deck1.deal_card())
print(deck1.count())
print(deck1.cards)

print(deck1.deal_hand(11))
print(deck1.deal_card())
print(deck1.count())
