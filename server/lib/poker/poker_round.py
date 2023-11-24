from ..poker.player import Player
from ..poker.player import PlayerAction
from ..playing_cards.deck import Deck
from ..playing_cards.card import Card
from .calculate_winner import calculate_winner

import enum


class RoundPhase(enum.Enum):
    PREFLOP = enum.auto()
    FLOP = enum.auto()
    TURN = enum.auto()
    RIVER = enum.auto()


class PokerRound:
    def __init__(self, players: list[Player]):
        self.players: list[Player] = players
        self.deck: Deck = Deck()
        self.community_cards: list[Card] = []

    def play_round(self):
        self._prepare_round()

        for phase in RoundPhase:
            self.phase = phase
            self._deal_community_cards()
            self._get_player_actions()

        winners = calculate_winner(self.players, self.community_cards)
        if len(winners) == 1:
            print("Winner:", winners[0].name)
        else:
            for player in winners:
                print("Winners:", player.name)

    def _prepare_round(self):
        self.deck.shuffle()
        self._give_players_cards()

    def _give_players_cards(self):
        CARD_COUNT = 2
        for _ in range(CARD_COUNT):
            for player in self.players:
                player.cards.append(self.deck.draw_card())

    def _get_player_actions(self):
        for player in self.players.copy():
            action = input()
            print(player.name, action)

            match action:
                case "fold":
                    self.players.remove(player)

    def _deal_community_cards(self) -> None:
        match self.phase:
            case RoundPhase.PREFLOP:
                print("PREFLOP")
            case RoundPhase.FLOP:
                print("FLOP")
                self.community_cards.append(self.deck.draw_card())
                self.community_cards.append(self.deck.draw_card())
                self.community_cards.append(self.deck.draw_card())
            case RoundPhase.TURN:
                print("TURN")
                self.community_cards.append(self.deck.draw_card())
            case RoundPhase.RIVER:
                print("RIVER")
                self.community_cards.append(self.deck.draw_card())
