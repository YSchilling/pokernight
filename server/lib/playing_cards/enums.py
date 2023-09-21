from enum import Enum

class CardColor(Enum):
    CLUBS = 0
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3

class CardValue(Enum):
    TWO = 0
    THREE = 1
    FOUR = 2
    FIVE = 3
    SIX = 4
    SEVEN = 5
    EIGHT = 6
    NINE = 7
    TEN = 8
    JACK = 9
    QUEEN = 10
    KING = 11
    ACE = 12