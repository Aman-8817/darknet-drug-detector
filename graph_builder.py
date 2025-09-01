# graph_builder.py

import networkx as nx
import matplotlib.pyplot as plt

# Sample entities and relations
buyers = ["BuyerA", "BuyerB"]
sellers = ["SellerX", "SellerY"]
wallets = ["W1", "W2"]

# Relations: (source, target, relation)
edges = [
    ("BuyerA", "SellerX", "buys_from"),
    ("BuyerB", "SellerX", "buys_from"),
    ("SellerX", "W1", "uses_wallet"),
    ("SellerY", "W2", "uses_wallet")
]

def build_graph(nodes, edges):
    G = nx.DiGraph()
    for node in nodes:
        G.add_node(node)
    for src, tgt, label in edges:
        G.add_edge(src, tgt, label=label)
    return G

def visualize_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, arrowsize=20)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.show()

if __name__ == "__main__":
    nodes = buyers + sellers + wallets
    G = build_graph(nodes, edges)
    visualize_graph(G)
