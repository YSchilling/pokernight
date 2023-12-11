from lib.poker.poker_game import PokerGame
from lib.poker.player import PlayerAction

from fastapi import FastAPI

import json

app = FastAPI()


@app.post("/game/create")
def create_game():
    app.game = PokerGame()
    return {"msg": "Game created"}


@app.post("/player/join")
def join_player(name: str):
    app.game.join_player(name)
    return {"msg": "Player joined"}


@app.post("/game/start")
def start_game():
    app.game.start_game()
    return {"msg": "Game started"}


@app.post("/player/do")
def player_action(action: PlayerAction) -> None:
    app.game.player_action(action)
    return {"msg": "Player took action"}


@app.get("/game/state")
def get_game_state():
    data = json.dumps(app.game.to_dict())
    return data
