from .player import Player
from .player import PlayerAction
from ..playing_cards.deck import Deck
from ..playing_cards.card import Card
from .calculate_winner import PokerHand
from .calculate_winner import calculate_winner

import enum

class RoundPhase(enum.Enum):
    PREFLOP = enum.auto()
    FLOP = enum.auto()
    TURN = enum.auto()
    RIVER = enum.auto()

class PokerGame:
    def __init__(self):
        self.deck: Deck = Deck()
        self.players: list[Player] = [Player("Player1"), Player(
            "Player2"), Player("Player3"), Player("Player4")]
        self.community_cards: list[Card] = []

    def run(self):
        self._start_round()

    def _start_round(self):
        self._prepare_round()
        self._play_round()
        self._end_round()

    def _prepare_round(self):
        self.deck.shuffle()
        self._give_players_cards()
    
    def _give_players_cards(self):
        CARD_COUNT = 2
        for _ in range(CARD_COUNT):
            for player in self.players:
                player.cards.append(self.deck.draw_card())
    
    def _play_round(self):
        for round_phase in RoundPhase:
            self._deal_community_cards(round_phase)
            print("PLAYER ACTIONS")
    
    def _deal_community_cards(self, round_phase: RoundPhase) -> None:
        match round_phase:
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

    def _end_round(self):
        winners = calculate_winner(self.players, self.community_cards)
        if len(winners) == 1:
            print(winners[0].name)
        else:
            for player in winners:
                print(player.name)

        self._reset_round()

    def _reset_round(self):
        self.deck = Deck()
        for player in self.players:
            player.cards = []