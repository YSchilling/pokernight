from .player import Player
from .poker_round import PokerRound


class PokerGame:
    def __init__(self):
        self.players: list[Player] = [
            Player("Player1"),
            Player("Player2"),
            Player("Player3"),
            Player("Player4")
        ]
        self.running = False

    def run(self):
        self.running = True
        # wait for all players
        while self.running:
            self._start_round()

    def _start_round(self):
        round = PokerRound(self.players)
        round.play_round()
