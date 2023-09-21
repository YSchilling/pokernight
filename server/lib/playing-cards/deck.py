from card import Card
from enums import CardColor
from enums import CardValue

class Deck:
    def __init__(self) -> None:
        self.cards = [Card(color, value) for color in CardColor for value in CardValue]
    
    def get_card(self) -> Card:
        return self.cards.pop()

    def add_card(self, card: Card) -> None:
        self.cards.append(card)