from .player import Player
from .player import PlayerAction
from .poker_round import PokerRound
from .poker_round import RoundState
from .game_config import GameConfig

import enum

class PokerGameState(enum.Enum):
    CREATING = enum.auto()
    RUNNING = enum.auto()
    ENDED = enum.auto()

class PokerGame:
    def __init__(self):
        self.players: list[Player] = []
        self.state: PokerGameState = PokerGameState.CREATING
        self.dealer_button_position: int = 0
        self.round: PokerRound | None = None

    def join_player(self, name):
        if not (self.state == PokerGameState.CREATING) or len(self.players) >= GameConfig.MAX_PLAYERS:
            return
        
        self.players.append(Player(name))

    def start_game(self):
        if not (self.state == PokerGameState.CREATING) or len(self.players) < 2:
            return

        self.state = PokerGameState.RUNNING
        self.round = PokerRound(self._get_active_players(), self.dealer_button_position)

    def player_action(self, action: PlayerAction) -> None:
        if self.state == PokerGameState.RUNNING:
            self.round.player_action(action)
        
        if self.round.state == RoundState.ENDED:
            self._move_dealer_button()
            self.round = PokerRound(self._get_active_players(), self.dealer_button_position)

    def _move_dealer_button(self):
        new_pos = self.dealer_button_position + 1
        if new_pos > len(self._get_active_players()) - 1:
            new_pos = 0
        self.dealer_button_position = new_pos

    def _get_active_players(self):
        return [player for player in self.players if player.chips > 0]
