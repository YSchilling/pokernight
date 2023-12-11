import requests

response = requests.post("http://127.0.0.1:8000/game/create")
print(response.json())

response = requests.post("http://127.0.0.1:8000/player/join?name=Player1")
print(response.json())

response = requests.post("http://127.0.0.1:8000/player/join?name=Player2")
print(response.json())

response = requests.post("http://127.0.0.1:8000/player/join?name=Player3")
print(response.json())

response = requests.post("http://127.0.0.1:8000/game/start")
print(response.json())

response = requests.get("http://127.0.0.1:8000/game/state")
print(response.json())
