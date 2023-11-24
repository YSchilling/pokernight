from lib.poker.poker_game import PokerGame

game = PokerGame()

for i in range(1, 5):
    game.join_player(f"Player {i}")

game.try_start_game()
