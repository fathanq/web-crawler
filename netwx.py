import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('B', 'C')])
G.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D')])
pos = graphviz_layout(G, prog="dot")
nx.draw_networkx_nodes(G, pos, node_size=300)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
nx.draw_networkx_labels(G, pos)
nx.draw(G, pos, with_labels=False, arrows=True)
plt.show()

# T = nx.balanced_tree(2, 5)

# pos = graphviz_layout(T, prog="dot")
# nx.draw(T, pos)
# plt.show()


# pos = nx.spiral_layout(G)
# nx.draw_networkx_nodes(G, pos, node_size=500)
# nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
# nx.draw_networkx_labels(G, pos)

# import pandas as pd
# import numpy as np