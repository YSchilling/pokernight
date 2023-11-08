from .player import Player
from ..playing_cards.deck import Deck
from ..playing_cards.card import Card


class PokerGame:
    def __init__(self):
        self.deck: Deck = Deck()
        self.players: list[Player] = [Player(), Player()]
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
        print("Players:")
        for player in self.players:
            print([card for card in map(str, player.cards)])

        print("Community Card:")
        print([card for card in map(str, self.community_cards)])

        print("Deck:")
        print(self.deck)
        # collect cards
        for player in self.players:
            self.deck.add_multiple(player.cards)
            player.cards = []
