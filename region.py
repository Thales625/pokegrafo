import pokedex

class Region:
	def __init__(self, name):
		self.name = name

		self.pokemon = pokedex.get_random()

	def get_name(self):
		return self.name.replace("-", " ").capitalize()

	def __repr__(self):
		return f"{self.get_name()}\n<{self.pokemon.name}>"

	def __hash__(self):  
		return hash(self.name)  # hash based on Region name

	def __eq__(self, other):  
		return isinstance(other, Region) and self.name == other.name # equality comparison