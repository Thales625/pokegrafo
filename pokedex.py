from json import load
from random import choice

from pokemon import Pokemon

# load pokemons
f = open("pokemons.json", "r")
data = load(f)

pokemons = []

for id, p in enumerate(data):
	pokemons.append(Pokemon(p["name"], p["stats"], id))

del data
f.close()

def get_by_name(name):
	for poke in pokemons:
		if poke.name == name:
			return poke

	print(f"> Pokedex error, pokemon {name} not found!")
	return None

def get_random():
	return choice(pokemons)