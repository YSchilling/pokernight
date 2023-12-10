from ..playing_cards.card import Card
from .game_config import GameConfig

import enum


class PlayerAction(enum.Enum):
    FOLD = enum.auto()
    CALL = enum.auto()
    RAISE = enum.auto()


class Player:
    def __init__(self, name: str):
        self.name = name
        self.cards: list[Card] = []
        self.chips: int = GameConfig.STARTING_CHIPS
