from fastapi import FastAPI

app = FastAPI()

players: list[str] = []


@app.get("/add-player/{name}")
async def add_player(name: str):
    players.append(name)
    return "OK"


@app.get("/get-players")
async def get_players():
    return players
