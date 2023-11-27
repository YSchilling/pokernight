from lib.poker.poker_game import PokerGame
from lib.poker.player import PlayerAction

def create_game() -> PokerGame:
    return PokerGame()

def join_player(game: PokerGame, name: str) -> None:
    game.join_player(name)

def start_game(game: PokerGame) -> None:
    game.start_game()

def player_action(game: PokerGame, action: PlayerAction) -> None:
    game.player_action(action)