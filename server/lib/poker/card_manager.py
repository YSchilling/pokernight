from ..playing_cards.deck import Deck
from .player import Player
from ..playing_cards.card import Card

class CardManager:
    def __init__(self) -> None:
        self.deck = Deck()
        self.community_cards = []
    
    def shuffle_deck(self):
        self.deck.shuffle()
    
    def give_players_cards(self, players: list[Player]):
        for _ in range(2):
            for player in players:
                player.cards.append(self.deck.get_card())
    
    def next_community_cards(self):
        if len(self.community_cards) == 0:
            for _ in range(3):
                self.community_cards.append(self.deck.get_card())
        
        if len(self.community_cards) == 3 or len(self.community_cards) == 4:
            self.community_cards.append(self.deck.get_card())
    
    def collect_community_cards(self):
        self.deck.add_multiple(self.community_cards)
        self.community_cards = []