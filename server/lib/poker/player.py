from ..playing_cards.card import Card

class Player:
    def __init__(self, name: str, money: int) -> None:
        self.name: str = name
        self.money: int = money
        self.cards: list(Card) = []
        self.bet: int = None