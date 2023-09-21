from ..playing_cards.deck import Deck

class CardManager:
    def __init__(self) -> None:
        self.deck = Deck()
        self.community_cards = []