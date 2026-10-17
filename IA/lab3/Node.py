class Node():

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.neighbours = []

    def edge(self, node):
        self.neighbours.append(node)

    def __str__(self):
        return f'({self.vertex_number})'
    def printNeighbours(self):
        return self.neighbours
    def __repr__(self):
        return str(self)

nodes = []
# for i in range(7):
#     nodes.append(Node(i))
# nodes[1].edge(nodes[3])
# nodes[1].edge(nodes[6])
# nodes[2].edge(nodes[6])
# nodes[3].edge(nodes[3])
# nodes[3].edge(nodes[4])
# nodes[5].edge(nodes[2])
# nodes[6].edge(nodes[3])
# nodes[6].edge(nodes[4])
# nodes[6].edge(nodes[5])

with open("graph1.txt","r") as f:
    nr_node = int(f.readline())

    for i in range(nr_node + 1):
        nodes.append(Node(i))

    for line in f:
        node1, node2 = map(int,line.split())
        nodes[node1].edge(nodes[node2])

print(nodes[4].printNeighbours())
    