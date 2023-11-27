from lib.poker.poker_game import PokerGame

def create_game() -> PokerGame:
    return PokerGame()

def join_player(game: PokerGame, name: str) -> None:
    game.join_player(name)

def start_game(game: PokerGame) -> None:
    game.start_game()