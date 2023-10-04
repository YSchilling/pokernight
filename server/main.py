from lib.poker.game_config import GameConfig
from lib.poker.poker_game import PokerGame
from lib.poker.player import Player

def main():
    # create game
    config = GameConfig(1000, 2, 50)
    game = PokerGame(config)

    # add players
    for i in range(1, 5):
        player = Player(f"Player {i}")
        game.join_player(player)
    
    for player in game.player_manager.players:
        print(player)
    
    print(game.card_manager.deck)

if __name__ == "__main__":
    main()