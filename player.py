import networkx as nx

class Player:
	def __init__(self, name, region, graph, initial_pokemon):
		self.name = name
		self.region = region
		self.graph = graph
		self.pokemons = [initial_pokemon]
	
	def show_status(self):
		return "status"
	
	def combat(self, player_pokemon, gym_pokemon):
		while player_pokemon.stats["hp"] > 0 and gym_pokemon.stats["hp"] > 0:
			# player pokemon attack
			gym_pokemon.stats["hp"] -= player_pokemon.stats["attack"]
			print(f"{player_pokemon.name} atacou! HP de {gym_pokemon.name}: {gym_pokemon.stats["hp"]}")

			if gym_pokemon.stats["hp"] <= 0:
				print(f"{gym_pokemon.name} foi derrotado!")
				break

			# gym pokemon attack
			player_pokemon.stats["hp"] -= gym_pokemon.stats["attack"]
			print(f"{gym_pokemon.name} atacou! HP de {player_pokemon.name}: {player_pokemon.stats["hp"]}")

			if player_pokemon.stats["hp"] <= 0:
				print(f"{player_pokemon.name} foi derrotado!")
				return False
		return True

	def travel(self, node) -> bool:
		algorithms = ["dijkstra", "bellman-ford"]
		text = "Algoritmos disponiveis:"
		for i, alg in enumerate(algorithms):
			text += f"\n\t({i}) {alg}"
		print(text)
		algorithm = algorithms[int(input(f"Digite o indice do algoritmo que deseja usar: "))]

		path = self.graph._shortest_path(self.region, node, algorithm)

		if path:
			print("Menor caminho encontrado!\n")
			print("Para chegar ao destino voce tera que passar por")
			for region in path:
				print(f" -> <{region.get_name()}> onde enfrentara o pokemon {region.pokemon.name.capitalize()}")
			
			self.graph.draw_path(self.region, path)
			
			r = input("Deseja prosseguir (y/n)? ")

			print("")

			if r.lower().startswith("y"):
			
				for i, region in enumerate(path[1::]):
					self.graph.draw_path(region, path[i+1::])

					print(f"------Enfrentando o pokemon {region.pokemon.name.capitalize()} em {region.get_name()}------")

					text = "\nEscolha um Pokémon para a batalha:"
					for i, pokemon in enumerate(self.pokemons):
						text += f"\n\t{i}: {pokemon.name} (HP: {pokemon.stats["hp"]})"
					print(text)
					
					while True:
						try:
							choice = int(input("Digite o índice do Pokémon que deseja usar: "))
							if 0 <= choice < len(self.pokemons):
								player_pokemon = self.pokemons[choice]
								break
							else:
								print("Índice inválido. Tente novamente.")
						except ValueError:
							print("Entrada inválida. Digite um número.")
						
					print("\n----Iniciando o combate!----")
					
					if (self.combat(player_pokemon, region.pokemon)): # player win
						print("Voce ganhou o combate!")
						player_pokemon.stats = player_pokemon.initial_stats.copy() # restore stats
						region.pokemon.stats = region.pokemon.initial_stats.copy() # restore stats
						self.pokemons.append(region.pokemon)
					else:
						print("Voce perdeu o combate!")
						# TODO: go back region
						self.pokemons.remove(player_pokemon)
						if len(self.pokemons) == 0:
							print("VOCE FICOU SEM POKEMONS!")
							exit()

				print("------------------")

				self.region = node
				return True
			else:
				self.graph.draw(self.region)
				return False
		else:
			print("Não foi possível encontrar um caminho.")
			return False