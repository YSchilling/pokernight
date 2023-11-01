from .chip_manager import ChipManager
from .card_manager import CardManager
from .game_config import GameConfig
from .player_manager import PlayerManager
from .enums import GameState
from .player import Player


class PokerGame:
    def __init__(self, config: GameConfig) -> None:
        self.config = config
        self.state = GameState.CREATING
        self.player_manager = PlayerManager()
        self.card_manager = CardManager()
        self.chip_manager = ChipManager(config)

    def start(self) -> None:
        self.state = GameState.RUNNING
        self.chip_manager.give_players_money(
            self.player_manager.players, self.config.player_starting_money)
        self.chip_manager.give_players_buttons()
        self.start_round()

    def start_round(self) -> None:
        self.card_manager.deck.shuffle()
        self.card_manager.give_players_cards(self.player_manager.players)

    def join_player(self, player: Player) -> None:
        if self.state != GameState.CREATING:
            raise ValueError(
                "Player can't join while game is not in creating state!")

        self.player_manager.players.append(player)
