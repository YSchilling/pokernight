from .enums import CardColor
from .enums import CardValue


class Card:
    def __init__(self, color: CardColor, value: CardValue):
        self.color = color
        self.value = value

    def __eq__(self, other):
        return self.color == other.color and self.value == other.value

    def __str__(self) -> str:
        return f"({self.color.name} {self.value.name})"

    def to_symbol(self):
        card_to_value = {
            CardValue.ACE: 0,
            CardValue.TWO: 1,
            CardValue.THREE: 2,
            CardValue.FOUR: 3,
            CardValue.FIVE: 4,
            CardValue.SIX: 5,
            CardValue.SEVEN: 6,
            CardValue.EIGHT: 7,
            CardValue.NINE: 8,
            CardValue.TEN: 9,
            CardValue.JACK: 10,
            CardValue.QUEEN: 12,
            CardValue.KING: 13,
        }
        bytes_list = list("🂡".encode())
        bytes_list = [240, 159, 0, 0]
        match self.color:
            case CardColor.SPADES:
                bytes_list[2] = 130
                bytes_list[3] = 161
            case CardColor.HEARTS:
                bytes_list[2] = 130
                bytes_list[3] = 177
            case CardColor.DIAMONDS:
                bytes_list[2] = 131
                bytes_list[3] = 129
            case CardColor.CLUBS:
                bytes_list[2] = 131
                bytes_list[3] = 145

        bytes_list[3] += card_to_value[self.value]
        return bytes(bytes_list).decode()

    def eq_value(self, other) -> bool:
        return self.value == other.value

    def eq_color(self, other) -> bool:
        return self.color == other.color
