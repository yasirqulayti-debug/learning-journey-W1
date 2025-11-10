import requests 

def fetch_api(url,label):
    print(f"=={label.upper()}==")
    try:

        response = requests.get(url,timeout=5)
        response.raise_for_status()

        data = response.json()

        if "setup" in data:
            print("Type:", data["type"])
            print("setup:", data["setup"])
            print("Punchline:", data["punchline"])
        elif "fact" in data:
            print("Fact:", data["fact"])
            print("Length:", data["length"])
        elif "name" in data:
            print("Pokemon name:", data["name"])
            

    except requests.exceptions.RequestException as e:
        print("Requests faild",e)
    
fetch_api("https://official-joke-api.appspot.com/random_joke","Joke API")

fetch_api("https://catfact.ninja/fact","Cat Fact API")

fetch_api("https://pokeapi.co/api/v2/pokemon/pikachu","Pokemon API")

    

    





