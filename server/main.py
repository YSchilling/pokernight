import api

game = api.create_game()

for i in range(1, 5):
    api.join_player(game, f"Player {i}")

api.start_game(game)
