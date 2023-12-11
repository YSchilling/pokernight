from ..poker.player import Player
from ..poker.player import PlayerAction
from ..playing_cards.deck import Deck
from ..playing_cards.card import Card
from .calculate_winner import calculate_winners
from .game_config import GameConfig

import enum


class RoundPhase(enum.Enum):
    PREFLOP = enum.auto()
    FLOP = enum.auto()
    TURN = enum.auto()
    RIVER = enum.auto()


class RoundState(enum.Enum):
    RUNNING = enum.auto()
    ENDED = enum.auto()


class PokerRound:
    def __init__(self, players: list[Player], dealer_button_position: int):
        self.players: list[Player] = players[dealer_button_position:] + \
            players[:dealer_button_position]
        self.deck: Deck = Deck()
        self.community_cards: list[Card] = []
        self.pot: int = 0
        self.highest_bet: int = 0
        self.player_bets = {player: None for player in self.players}
        self.phase = RoundPhase.PREFLOP
        self.active_player = 0
        self.state = RoundState.RUNNING

        self.deck.shuffle()
        self._give_players_cards()
        self._make_blinds()

    def to_dict(self):
        return {
            "players": [player.to_dict() for player in self.players],
            "deck": self.deck.to_dict(),
            "community_cards": [card.to_dict() for card in self.community_cards],
            "pot": self.pot,
            "highest_bet": self.highest_bet,
            "player_bets": {player.name: bet for (player, bet) in self.player_bets.items()},
            "phase": self.phase.name,
            "active_player": self.active_player,
            "state": self.state.name
        }

    def player_action(self, action: PlayerAction):
        self._process_action(action)

        self.active_player += 1

        if self._check_phase_end():
            self._next_phase()
            if len(self.players) <= 1:
                self._end_round()

    def _end_round(self):
        self.state = RoundState.ENDED
        winners = calculate_winners(self.players, self.community_cards)
        if len(winners) == 1:
            print("Winner:", winners[0].name)
        else:
            for player in winners:
                print("Winners:", player.name)

    def _next_phase(self):
        self.highest_bet = 0
        self.player_bets = {player: None for player in self.players}
        self.active_player = 0
        self._deal_community_cards()
        match self.phase:
            case RoundPhase.PREFLOP:
                self.phase = RoundPhase.FLOP
            case RoundPhase.FLOP:
                self.phase = RoundPhase.TURN
            case RoundPhase.TURN:
                self.phase = RoundPhase.RIVER
            case RoundPhase.RIVER:
                self._end_round()

    def _give_players_cards(self):
        CARD_COUNT = 2
        for _ in range(CARD_COUNT):
            for player in self.players:
                player.cards.append(self.deck.draw_card())

    def _make_blinds(self):
        small_blind = GameConfig.MINIMUM_BET / 2
        big_blind = GameConfig.MINIMUM_BET

        if len(self.players) >= 3:
            self.players[1].chips -= small_blind
            self.pot += small_blind

            self.players[2].chips -= big_blind
            self.pot += big_blind
        else:  # head to head rule
            self.players[0].chips -= small_blind
            self.pot += small_blind

            self.players[1].chips -= big_blind
            self.pot += big_blind

    def _process_action(self, action: PlayerAction):
        player = self.players[self.active_player % len(self.players)]
        match action:
            case PlayerAction.FOLD:
                self.players.remove(player)
                self.player_bets.pop(player)
                self.active_player -= 1
            case PlayerAction.CALL:
                player.chips -= self.highest_bet
                self.pot += self.highest_bet
                if self.player_bets[player] == None:
                    self.player_bets[player] = self.highest_bet
                else:
                    self.player_bets[player] += self.highest_bet
            case PlayerAction.RAISE:
                amount = 0
                while amount <= self.highest_bet:
                    amount = int(input())
                self.highest_bet = amount
                player.chips -= amount
                self.pot += amount
                if self.player_bets[player] == None:
                    self.player_bets[player] = self.highest_bet
                else:
                    self.player_bets[player] += self.highest_bet

    def _deal_community_cards(self) -> None:
        match self.phase:
            case RoundPhase.PREFLOP:
                pass
            case RoundPhase.FLOP:
                self.community_cards.append(self.deck.draw_card())
                self.community_cards.append(self.deck.draw_card())
                self.community_cards.append(self.deck.draw_card())
            case RoundPhase.TURN:
                self.community_cards.append(self.deck.draw_card())
            case RoundPhase.RIVER:
                self.community_cards.append(self.deck.draw_card())

    def _check_phase_end(self):
        all_betted_same = all(
            [bet == self.highest_bet for bet in self.player_bets.values()])
        return all_betted_same or len(self.players) == 1
