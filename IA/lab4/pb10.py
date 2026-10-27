import numpy as np

class Node():

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.neighbours = []

    def edge(self, node):
        self.neighbours.append(node)

nodes = []

with open("graph.txt","r") as f:
    nr_nodes = int(f.readline())

    for i in range(1, nr_nodes + 1):
        nodes.append(Node(i))

    for line in f:
        parts = line.split()
        x = int(parts[0])
        y = int(parts[1])

        nodes[x - 1].edge(nodes[y - 1])

A = np.zeros((nr_nodes, nr_nodes), dtype = int)

for node in nodes:
    i = node.vertex_number - 1

    for neighbour in node.neighbours:
        j = neighbour.vertex_number - 1
        A[i][j] = 1
print(A)