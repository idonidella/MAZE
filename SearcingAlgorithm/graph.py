from queue import Queue
import networkx as nx
import matplotlib.pyplot as plt


class Vertex:  # vertex class, represent nodes of Graph
    def __init__(self, data):
        self.edges = []  # list of edges that out from the node
        self.data = data  # value of vertex


class Edge:  # edges connect the vertices each other
    def __init__(self, out, to, weight):
        self.out = out  # vertex that edge come from
        self.to = to  # vertex that edge come to
        self.weight = weight  # associated numerical value with edge


class Graph:
    def __init__(self):  # constructor method for Graph class
        self.vertices = []  # list of vertex
        self.edgeMap = {}  # stores (vertex data, list of edges) pairs
        self.verticesMap = {}  # simple way of reach vertices
        self.start = None

    def addVertex(self, vertex):  # add vertex to graph
        flag = True
        for temp in self.vertices:  # a check if Graph contains corresponding vertex
            if temp.data == vertex.data:
                flag = False
        if flag:
            self.vertices.append(vertex)
            self.edgeMap[vertex.data] = vertex.edges
            self.verticesMap[vertex.data] = vertex

    def addEdge(self, out, to, weight=1):  # add edge to graph, it provides connection between vertices
        vertexOut = self.verticesMap[out.data]
        vertexTo = self.verticesMap[to.data]
        if vertexTo.data == str([-1]) or vertexTo.data == str([1]):
            edge1 = Edge(vertexOut, vertexTo, weight)
            vertexOut.edges.append(edge1)
        else:
            edge1 = Edge(vertexOut, vertexTo, weight)
            edge2 = Edge(vertexTo, vertexOut, weight)
            vertexOut.edges.append(edge1)
            vertexTo.edges.append(edge2)


def depthFirstSearch(visited, vertex):
    if vertex not in visited:
        print(vertex.data)
        visited.add(vertex)
        for edge in vertex.edges:
            depthFirstSearch(visited, edge.to)


maze = [
    [1,1,0,1,1],
    [1,0,0,1,1],
    [1,0,0,0,1],
    [1,0,1,1,1],
    [1,0,0,0,0]
]


def is_valid(i, j, list):
    return 0 <= i < len(list) and 0 <= j < len(list[0])


def find_path(i, j, path):
    if i == len(maze) - 1:
        all_paths.append(path + [[1]])
        for x, y in [(0, 1), (0, -1)]:
            positionx = i + x
            positiony = j + y
            if is_valid(positionx, positiony, maze):
                if maze[positionx][positiony] == 1:
                    if [positionx, positiony] not in path:
                        new_path = path + [[positionx, positiony]]
                        find_path(positionx, positiony, new_path)
        return
    possibilities = []
    for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
        positionx = i + x
        positiony = j + y

        if is_valid(positionx, positiony, maze):
            if maze[positionx][positiony] == 1:
                if [positionx, positiony] not in path:
                    possibilities.append([positionx, positiony])

    if len(possibilities) == 0:
        all_paths.append(path + [[-1]])
        return
    for coord in possibilities:
        find_path(coord[0], coord[1], path + [coord])


all_paths = []

find_path(0, 0, [[0, 0]])

print(all_paths)

graph = Graph()

for path in all_paths:
    for i in range(0, len(path) - 1):
        vertexOut = None
        vertexTo = None
        if str(path[i]) not in graph.verticesMap:
            vertexOut = Vertex(str(path[i]))
            graph.addVertex(vertexOut)
        else:
            vertexOut = graph.verticesMap[str(path[i])]
        if str(path[i + 1]) not in graph.verticesMap:
            vertexTo = Vertex(str(path[i + 1]))
            graph.addVertex(vertexTo)
        else:
            vertexTo = graph.verticesMap[str(path[i + 1])]
        flag = True
        for edge in vertexOut.edges:
            if edge.to.data == vertexTo.data:
                flag = False
        if flag:
            graph.addEdge(vertexOut, vertexTo)

nodes = []
edges = []
for node in graph.vertices:
    nodes.append(node.data)

for k, edgeList in graph.edgeMap.items():
    for edge in edgeList:
        edges.append((edge.out.data, edge.to.data))

G = nx.DiGraph()

# Düğümleri ekle
G.add_nodes_from(nodes)

# Kenarları ekle
G.add_edges_from(edges)

# Ağı çizin
pos = nx.circular_layout(G)  # Düğümleri dairesel bir düzen içinde yerleştirin
nx.draw(G, pos, with_labels=True, arrowsize=20, font_size=10, font_color='white', node_size=800, node_color='skyblue',
        edge_color='gray', font_weight='bold')

# Ağı göster
plt.title('Test')
plt.show()