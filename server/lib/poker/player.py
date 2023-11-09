from ..playing_cards.card import Card


class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards: list[Card] = []
