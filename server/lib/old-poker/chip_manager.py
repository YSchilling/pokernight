from .game_config import GameConfig
from .player import Player

class ChipManager:
    def __init__(self, config: GameConfig) -> None:
        self.small_blind_value = config.starting_blind_value
        self.dealer_button_pos: int = None
        self.small_blind_pos: int = None
        self.big_blind_pos: int = None
    
    def give_players_money(self, players, money):
        for player in players:
            player.money = money
    
    def give_players_buttons(self, player_amount):
        self.dealer_button_pos = 0
        self.small_blind_pos = 1
        if player_amount == 2:
            self.big_blind_pos = 0
        else:
            self.big_blind_pos = 2