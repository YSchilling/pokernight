import api
from lib.poker.player import PlayerAction

game = api.create_game()

for i in range(1, 5):
    api.join_player(game, f"Player {i}")

api.start_game(game)

while True:
    print(f"1: fold, 2: call, 3: raise")
    input_string = input()
    match input_string:
        case "1":
            game.player_action(PlayerAction.FOLD)
        case "2":
            game.player_action(PlayerAction.CALL)
        case "3":
            game.player_action(PlayerAction.RAISE)
    
