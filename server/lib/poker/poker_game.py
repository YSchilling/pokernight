from .player import Player
from .poker_round import PokerRound


class PokerGame:
    def __init__(self):
        self.players: list[Player] = []
        self.running = False
        self.button_positions = {"dealer": None,
                                 "smallblind": None,
                                 "bigblind": None}

    def try_start_game(self):
        if not self.running and len(self.players) >= 2:
            self.running = True
            self._init_buttons()

            while (self.running):
                self._start_round()
                self._move_buttons()

    def join_player(self, name):
        if len(self.players) <= 8:
            self.players.append(Player(name))

    def _start_round(self):
        round = PokerRound(self.players.copy(), self.button_positions.copy())
        round.play_round()

    def _init_buttons(self):
        # head to head rule if only 2 players play
        if len(self.players) == 2:
            self.button_positions["dealer"] = 0
            self.button_positions["smallblind"] = 0
            self.button_positions["bigblind"] = 1
        else:
            self.button_positions["dealer"] = 0
            self.button_positions["smallblind"] = 1
            self.button_positions["bigblind"] = 2

    def _move_buttons(self):
        # head to head rule if only 2 players play
        if len(self.players) == 2:
            self.button_positions["dealer"] = 0
            self.button_positions["smallblind"] = 0
            self.button_positions["bigblind"] = 0

        else:  # TODO make a function or so for the repeating code
            last_pos = self.button_positions["dealer"]
            new_pos = last_pos + 1
            if new_pos > len(self.players) - 1:
                new_pos = 0
            self.button_positions["dealer"] = new_pos

            last_pos = self.button_positions["smallblind"]
            new_pos = last_pos + 1
            if new_pos > len(self.players) - 1:
                new_pos = 0
            self.button_positions["smallblind"] = new_pos

            last_pos = self.button_positions["bigblind"]
            new_pos = last_pos + 1
            if new_pos > len(self.players) - 1:
                new_pos = 0
            self.button_positions["bigblind"] = new_pos
