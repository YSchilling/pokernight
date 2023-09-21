from bet_manager import BetManager
from card_manager import CardManager
from game_config import GameConfig
from player_manager import PlayerManager
from player import Player

class PokerGame:
    def __init__(self, config: GameConfig) -> None:
        self.game_config = config
        self.player_manager = PlayerManager()
        self.card_manager = CardManager()
        self.bet_manager = BetManager()