import networkx as nx
import matplotlib.pyplot as plt

from graph import Graph
from region import Region
from player import Player
import pokedex

class Game:
	def __init__(self):
		# matplotlib
		self.fig, self.ax = plt.subplots()
		plt.ion() # matplotlib enable interactive mode
		self.fig.canvas.mpl_connect('button_press_event', self.on_click) # mouse click event listener

		# load graph
		self.graph, r0, rf, p0, pf = self.load_config("./config.txt", self.fig, self.ax)

		# create player
		player_name = input("Digite seu nome: ")
		self.player = Player(player_name, r0, self.graph, p0)

		# TODO: find better solution
		self.graph.draw(self.player.region)

		while True:
			if not plt.fignum_exists(self.fig.number):
				break
			plt.pause(0.1)

		plt.ioff() # matplotlib disable interactive mode

	def on_click(self, event): # handle mouse click
		if event.inaxes == self.ax:
			click_x, click_y = event.xdata, event.ydata

			# search valid node
			for node, (x, y) in self.graph.pos.items():
				distance = ((x - click_x) ** 2 + (y - click_y) ** 2) ** 0.5
				if distance < 0.1:
					if self.player.travel(node):
						print(f"Voce chegou em {self.player.region.get_name()}")
						self.graph.draw(self.player.region)
					break

	def load_config(self, file_path, fig, ax): # static method
		graph = Graph(fig, ax)

		pokemon_initial = None
		pokemon_final = None

		region_inital = None
		region_final = None
		
		with open(file_path, 'r') as f:
			lines = f.readlines()

			for i, line in enumerate(lines):
				line = line.strip()

				if not line: continue  # ignore empty lines

				if line.count("[") == 1 and line.count("]") == 1:
					region = Region(line.strip("[]"))

					if region_inital is None: region_inital = region
					else: region_final = region
				elif line.count("[") == 2 and line.count("]") == 2:
					parts = line.split()
					region1, distance, region2 = Region(parts[0].strip("[]")), int(parts[1]), Region(parts[2].strip("[]"))
					graph.add_edge(region1, region2, weight=distance)
				else:
					poke = pokedex.get_by_name(line)

					if pokemon_initial is None:
						pokemon_initial = poke
					else:
						pokemon_final = poke
			
			graph.pos = nx.spring_layout(graph)  # Generate positions for all nodes

			return graph, region_inital, region_final, pokemon_initial, pokemon_final