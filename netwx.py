import networkx as nx
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

G = nx.DiGraph()
# G.add_edges_from([('A', 'B'), ('A', 'E')])
# G.add_edges_from([('B', 'F'), ('A', 'C'), ('A', 'D')])
# G.add_edges_from([('B', 'G')])

ts = [['h://w.a.c', 'h://w.a.c/sepakbola']]
ts2 = [['www.indosport.com', 'www.indosport.com/sepakbola']]

t = [['https://www.indosport.com', 'www.indosport.com/sepakbola'], ['https://www.indosport.com/sepakbola', 'www.indosport.com/liga-indonesia'], ['https://www.indosport.com/liga-indonesia', 'www.indosport.com/liga-spanyol'], ['https://www.indosport.com/liga-spanyol', 'www.indosport.com/liga-italia']]
G.add_edges_from(ts2)
pos = graphviz_layout(G, prog="dot")
# nx.draw_networkx_nodes(G, pos, node_size=300)
# nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
# nx.draw_networkx_labels(G, pos)
# nx.draw(G, pos, with_labels=False, arrows=True)
nx.draw(G, pos, node_color='#A0CBE2', edge_color='#BB0000', width=2, edge_cmap=plt.cm.Blues, with_labels=True)
plt.savefig("graph.png", dpi=1000)
# plt.savefig("graph.pdf")

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