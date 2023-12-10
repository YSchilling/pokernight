from lib.poker.poker_game import PokerGame
from lib.poker.player import PlayerAction

from fastapi import FastAPI

import redis

app = FastAPI()

redis_db = redis.Redis(host='localhost', port=6379)


@app.post("/create")
def create_game() -> None:
    game = PokerGame()
    data = [player.name for player in game.players]
    redis_db.json().set("players", "$", data)
    return {"None": True}


def join_player(game: PokerGame, name: str) -> None:
    game.join_player(name)


def start_game(game: PokerGame) -> None:
    game.start_game()


def player_action(game: PokerGame, action: PlayerAction) -> None:
    game.player_action(action)


@app.get("/gamestate")
def get_game_state() -> str:
    return redis_db.json().get("game", "$")
