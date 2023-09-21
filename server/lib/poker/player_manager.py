from player import Player

class PlayerManager:
    def __init__(self, player_names: list(str), player_money: int) -> None:
        self.players = [Player(name, player_money) for name in player_names]
        self.active_player = None
        self.dealer_button_pos = 0