from ..poker.player import Player
from ..poker.player import PlayerAction
from ..playing_cards.deck import Deck
from ..playing_cards.card import Card
from .calculate_winner import calculate_winner
from .game_config import GameConfig

import enum


class RoundPhase(enum.Enum):
    PREFLOP = enum.auto()
    FLOP = enum.auto()
    TURN = enum.auto()
    RIVER = enum.auto()

class PokerRound:
    def __init__(self, players: list[Player], dealer_button_position: int):
        self.players: list[Player] = players[dealer_button_position:] + \
            players[:dealer_button_position]
        self.deck: Deck = Deck()
        self.community_cards: list[Card] = []
        self.pot: int = 0
        self.highest_bet: int = 0

    def play_round(self):
        self._prepare_round()

        for phase in RoundPhase:
            self.phase = phase
            self.highest_bet = 0
            self._deal_community_cards()
            self._get_player_actions()
            print(self.pot)

            if len(self.players) <= 1:
                return

        winners = calculate_winner(self.players, self.community_cards)
        if len(winners) == 1:
            print("Winner:", winners[0].name)
        else:
            for player in winners:
                print("Winners:", player.name)

    def _prepare_round(self):
        self.deck.shuffle()
        self._give_players_cards()
        self._make_blinds()

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

    def _get_player_actions(self):

        i = 0
        player_bets = {player: None for player in self.players}
        while True:
            player = self.players[i % len(self.players)]

            print(f"{player.name}:  1: fold, 2: call, 3: raise")
            input_string = input()
            match input_string:
                case "1":
                    self.players.remove(player)
                    player_bets.pop(player)
                    i -= 1
                case "2":
                    player.chips -= self.highest_bet
                    self.pot += self.highest_bet
                    if player_bets[player] == None:
                        player_bets[player] = self.highest_bet
                    else:
                        player_bets[player] += self.highest_bet
                case "3":
                    amount = 0
                    while amount <= self.highest_bet:
                        amount = int(input())
                    self.highest_bet = amount
                    player.chips -= amount
                    self.pot += amount
                    if player_bets[player] == None:
                        player_bets[player] = self.highest_bet
                    else:
                        player_bets[player] += self.highest_bet

            all_betted_same = all(
                [bet == self.highest_bet for bet in player_bets.values()])
            if all_betted_same or len(self.players) == 1:
                return

            i += 1

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
