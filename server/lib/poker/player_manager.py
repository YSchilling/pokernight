from player import Player

class PlayerManager:
    def __init__(self) -> None:
        self.players: list(Player) = []
        self.active_player: Player = None
        self.dealer_button_pos: Player = None