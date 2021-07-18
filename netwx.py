import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

G = nx.DiGraph()
# G.add_edges_from([('A', 'B'), ('A', 'E')])
# G.add_edges_from([('B', 'F'), ('A', 'C'), ('A', 'D')])
# G.add_edges_from([('B', 'G')])
G.add_edges_from([('www.link1.com', 'www.link2.com')])
G.add_edges_from([('www.link1.com', 'www.link3.com')])
G.add_edges_from([('www.link1.com', 'www.link4.com')])
G.add_edges_from([('www.link2.com', 'www.link5.com')])
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