from .bet_manager import BetManager
from .card_manager import CardManager
from .game_config import GameConfig
from .player_manager import PlayerManager
from .enums import GameState
from .player import Player
import sys

class PokerGame:
    def __init__(self, config: GameConfig) -> None:
        self.game_config = config
        self.state = GameState.CREATING
        self.player_manager = PlayerManager()
        self.card_manager = CardManager()
        self.bet_manager = BetManager(config)
    
    def start(self) -> None:
        self.state = GameState.RUNNING
    
    def join_player(self, player: Player) -> None:
        if self.state != GameState.CREATING:
            print("Player can't join while game is not in creating state!")
            sys.exit(0)
        
        self.player_manager.players.append(player)