# Create a simple undirected graph and plot it.
# Ref: https://networkx.github.io/documentation/latest/reference/introduction.html

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
plt.subplot(121)

# Create the nodes and edges
G.add_edge(0, 1)
G.add_edge(0, 7)
G.add_edge(1, 2)
G.add_edge(2, 7)
G.add_edge(2, 3)
G.add_edge(2, 5)
G.add_edge(2, 8)
G.add_edge(5, 8)
G.add_edge(3, 8)
G.add_edge(7, 3)


# Plot the graph

nx.draw(G, None, with_labels=True)
plt.show()
