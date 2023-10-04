from .enums import CardColor
from .enums import CardValue

class Card:
    def __init__(self, color: CardColor, value: CardValue):
        self.color = color
        self.value = value
    
    def __str__(self) -> str:
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
        
        bytes_list[3] += self.value.value
        return bytes(bytes_list).decode()