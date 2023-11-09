from .player import Player
from ..playing_cards.deck import Deck
from ..playing_cards.card import Card
from .calculate_winner import PokerHand
from .calculate_winner import calculate_winner


class PokerGame:
    def __init__(self):
        self.deck: Deck = Deck()
        self.players: list[Player] = [Player("Player1"), Player(
            "Player2"), Player("Player3"), Player("Player4")]
        self.community_cards: list[Card] = []

    def run(self):
        # shuffle deck
        self.deck.shuffle()

        # give players cards
        for _ in range(2):
            for player in self.players:
                player.cards.append(self.deck.draw_card())
        # deal community cards
        for _ in range(5):
            self.community_cards.append(self.deck.draw_card())
        # print game state
        winners = calculate_winner(self.players, self.community_cards)
        if len(winners) == 1:
            print(winners[0].name)
        else:
            for player in winners:
                print(player.name)
