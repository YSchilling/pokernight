from .card import Card
from .enums import CardColor
from .enums import CardValue
import random

class Deck:
    def __init__(self) -> None:
        self.cards = [Card(color, value) for color in CardColor for value in CardValue]
    
    def __str__(self):
        string = "Deck {"
        string += ", ".join(map(lambda x: str(x), self.cards))
        string += "}"
        return string
    
    def get_card(self) -> Card:
        return self.cards.pop()

    def add_card(self, card: Card) -> None:
        self.cards.append(card)
    
    def add_multiple(self, cards: list[Card]) -> None:
        self.cards += cards
    
    def shuffle(self):
        random.shuffle(self.cards)