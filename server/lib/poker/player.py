from ..playing_cards.card import Card

class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.money: int = None
        self.cards: list(Card) = []
        self.bet: int = None
    
    def __str__(self) -> str:
        string = self.name + ": {"
        string += f"money: {self.money}, cards: {self.cards}, bet: {self.bet}"
        string += "}"
        return string