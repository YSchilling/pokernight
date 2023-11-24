from .player import Player
from .poker_round import PokerRound


class PokerGame:
    def __init__(self):
        self.players: list[Player] = []
        self.running = False
        self.button_positions = []

    def try_start_game(self):
        if not self.running and len(self.players) >= 2:
            self.running = True
            while (self.running):
                self._start_round()

    def join_player(self, name):
        if len(self.players) <= 8:
            self.players.append(Player(name))

    def _start_round(self):
        round = PokerRound(self.players.copy(), self.button_positions.copy())
        round.play_round()
