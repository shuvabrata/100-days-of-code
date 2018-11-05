# https://plot.ly/python/network-graphs/#create-network-graph
# https://networkx.github.io/documentation/latest/tutorial.html
import networkx as nx
import matplotlib.pyplot as plt

G = nx.random_geometric_graph(20, 0.2)
nx.draw(G)
plt.show()
