# Create a simple undirected graph and plot it.
# Ref: https://networkx.github.io/documentation/latest/reference/introduction.html

import networkx as nx
import matplotlib.pyplot as plt

def get_graph():
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
    G.add_edge(9, 10)
    G.add_edge(9, 70)
    G.add_edge(9, 20)
    G.add_edge(9, 70)
    G.add_edge(9, 30)
    G.add_edge(9, 50)
    G.add_edge(9, 80)
    G.add_edge(9, 80)
    G.add_edge(9, 80)
    G.add_edge(9, 30)
    return G


def draw_graph(g, pos):
    nx.draw(g, pos, with_labels=True, node_color='#FFA07A', node_size=200, node_shape='8', edge_color='g')
    plt.show()


g = get_graph()
draw_graph(g, None)
draw_graph(g, nx.circular_layout(g))
draw_graph(g, nx.bipartite_layout(g, g.nodes))
draw_graph(g, nx.kamada_kawai_layout(g))
draw_graph(g, nx.random_layout(g))
draw_graph(g, nx.shell_layout(g))
draw_graph(g, nx.spectral_layout(g))

