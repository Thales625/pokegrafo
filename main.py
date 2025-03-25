import networkx as nx
import matplotlib.pyplot as plt

from region import Region

def load_config(file_path):
	graph = nx.Graph()

	pokemon_initial = None
	pokemon_final = None

	region_inital = None
	region_final = None
	
	with open(file_path, 'r') as f:
		lines = f.readlines()

		for i, line in enumerate(lines):
			line = line.strip()

			if not line: continue # ignore empty lines

			if line.count("[") == 1 and line.count("]") == 1:
				region = line.strip("[]")

				if region_inital is None: region_inital = region
				else: region_final = region
			elif line.count("[") == 2 and line.count("]") == 2:
				parts = line.split()
				region1, distance, region2 = Region(parts[0].strip("[]")), int(parts[1]), Region(parts[2].strip("[]"))
				graph.add_edge(region1, region2, weight=distance)
			else:
				if pokemon_initial is None:
					pokemon_initial = line
				else:
					pokemon_final = line

		return graph, region_inital, region_final, pokemon_initial, pokemon_final

if __name__ == "__main__":
	graph, r0, rf, p0, pf = load_config("./config.txt")

	print(r0, rf)
	print(p0, pf)

	# draw the graph
	pos = nx.spring_layout(graph)  # positions for all nodes
	nx.draw(graph, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=700)

	# draw edge labels (weights)
	edge_labels = nx.get_edge_attributes(graph, 'weight')
	nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

	plt.show()