import requests

url = "https://official-joke-api.appspot.com/random_joke"
respones = requests.get(url)

data = respones.json()

print("Setup:", data["setup"])
print("Punshline:", data["punchline"])