
import matplotlib.pyplot as plt
import networkx as nx

# Define the vertices and edges
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [
    ('A', 'B', 1),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 6),
    ('C', 'D', 4),
    ('C', 'E', 2),
    ('D', 'E', 5),
]

# Create a graph and add all edges
G = nx.Graph()
G.add_weighted_edges_from(edges)

# Kruskal's Algorithm classes
class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)
        if root1 != root2:
            self.parent[root2] = root1
            return True
        return False

def kruskal_mst(vertices, edges):
    mst_edges = []
    ds = DisjointSet(vertices)
    edge_objects = [Edge(u, v, w) for u, v, w in edges]
    edge_objects.sort()
    for edge in edge_objects:
        if ds.union(edge.u, edge.v):
            mst_edges.append((edge.u, edge.v, edge.weight))
    return mst_edges

mst_edges = kruskal_mst(vertices, edges)

# Create MST graph for visualization
MST = nx.Graph()
MST.add_weighted_edges_from(mst_edges)

# Draw original and MST graphs
plt.figure(figsize=(12, 6))
pos = nx.spring_layout(G, seed=42)

# Original Graph
plt.subplot(1, 2, 1)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Original Graph")

# MST Graph
plt.subplot(1, 2, 2)
nx.draw(MST, pos, with_labels=True, node_color='lightgreen', node_size=1000, font_weight='bold', edge_color='green', width=2)
labels_mst = nx.get_edge_attributes(MST, 'weight')
nx.draw_networkx_edge_labels(MST, pos, edge_labels=labels_mst)
plt.title("Minimum Spanning Tree (MST)")

plt.tight_layout()
plt.show()
