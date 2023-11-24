from .player import Player
from .poker_round import PokerRound


class PokerGame:
    def __init__(self):
        self.players: list[Player] = []
        self.running = False
        self.dealer_button_position = 0

    def try_start_game(self):
        if not self.running and len(self.players) >= 2:
            self.running = True

            while (self.running):
                self._start_round()
                self._move_dealer_button()

    def join_player(self, name):
        if len(self.players) <= 8:
            self.players.append(Player(name))

    def _start_round(self):
        print(self.dealer_button_position)
        round = PokerRound(self._get_active_players(),
                           self.dealer_button_position)
        round.play_round()

    def _move_dealer_button(self):
        new_pos = self.dealer_button_position + 1
        if new_pos > len(self._get_active_players()) - 1:
            new_pos = 0
        self.dealer_button_position = new_pos

    def _get_active_players(self):
        return [player for player in self.players if player.chips > 0]
