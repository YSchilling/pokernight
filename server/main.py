from fastapi import FastAPI
from lib.poker.poker_game import PokerGame
from lib.poker.player import Player

app = FastAPI()

players: list[player] = []


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/add-player/{player_name}")
async def add_player(name: str):
    players.append(Player(name))


@app.get("get-players")
async def get_players() -> list[Player]:
    return players
