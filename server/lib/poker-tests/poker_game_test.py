from poker.poker_game import PokerGame
from poker.game_config import GameConfig

def main():
    config = GameConfig(1000, 2, 50)
    game = PokerGame(config)