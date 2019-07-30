import requests
from functools import lru_cache

POKEAPI_ENDPOINT = "https://pokeapi.co/api/v2/pokemon/{}/"

@lru_cache(maxsize=None)
def get_pokemon(id_or_name):
    print("Executando requisicao: " +id_or_name)
    response = requests.get(POKEAPI_ENDPOINT.format(id_or_name))
    data = response.json()

    return data