import client

def test_get_bulbasaur_by_id():
    pokemon = client.get_pokemon("1")

    assert pokemon['name'] == 'bulbassaur'
