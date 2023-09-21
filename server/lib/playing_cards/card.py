from enums import CardColor
from enums import CardValue

class Card:
    def __init__(self, color: CardColor, value: CardValue):
        self.color = color
        self.value = value