from ..playing_cards.card import Card

import enum


class PlayerAction(enum.Enum):
    FOLD = enum.auto()
    CALL = enum.auto()
    RAISE = enum.auto()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards: list[Card] = []
