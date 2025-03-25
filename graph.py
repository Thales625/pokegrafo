import networkx as nx
import matplotlib.pyplot as plt

class Graph(nx.Graph):
	def __init__(self, fig, ax):
		super().__init__()
		self.pos = None

		self.fig = fig
		self.ax = ax
	
	def draw(self, player_region):
		self.ax.clear()
		nx.draw(self, self.pos, with_labels=True, node_color='lightblue', node_size=700, ax=self.ax)

		# draw weights
		edge_labels = nx.get_edge_attributes(self, 'weight')
		nx.draw_networkx_edge_labels(self, self.pos, edge_labels=edge_labels, ax=self.ax)

		# player region node
		nx.draw_networkx_nodes(self, self.pos, nodelist=[player_region], node_color='red', node_size=800, ax=self.ax)

		self.fig.canvas.draw() # draw canvas
		self.fig.canvas.flush_events() # process events

	def draw_path(self, player_region, path):
		self.ax.clear()
		nx.draw(self, self.pos, with_labels=True, node_color='lightblue', node_size=700, ax=self.ax)

		# draw weights
		edge_labels = nx.get_edge_attributes(self, 'weight')
		nx.draw_networkx_edge_labels(self, self.pos, edge_labels=edge_labels, ax=self.ax)

		# path region
		nx.draw_networkx_nodes(self, self.pos, nodelist=path, node_color='blue', node_size=800, ax=self.ax)

		# player region node
		nx.draw_networkx_nodes(self, self.pos, nodelist=[player_region], node_color='red', node_size=800, ax=self.ax)

		# target region node
		nx.draw_networkx_nodes(self, self.pos, nodelist=[path[-1]], node_color='green', node_size=800, ax=self.ax)

		self.fig.canvas.draw() # draw canvas
		self.fig.canvas.flush_events() # process events

	def _shortest_path(self, origin_node, target_node, algorithm):
		try:
			# G = nx.DiGraph(self)
			# path = nx.shortest_path(G, source=origin_node, target=target_node, weight='weight', method=algorithm)
			path = nx.shortest_path(self, source=origin_node, target=target_node, weight='weight', method=algorithm)
			return path
		except nx.NetworkXNoPath:
			return None
