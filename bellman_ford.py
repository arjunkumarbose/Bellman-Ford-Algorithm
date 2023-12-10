class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        distance = [float("inf")] * self.V
        distance[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distance[u] != float("inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        # Check for negative cycles
        for u, v, w in self.graph:
            if distance[u] != float("inf") and distance[u] + w < distance[v]:
                print("Graph contains negative cycle")
                return

        return distance

# Taking user input to create the graph
vertices = int(input("Enter the number of vertices in the graph: "))
edges = int(input("Enter the number of edges in the graph: "))

g = Graph(vertices)

print("Enter edges for the graph with weights (format: 'source destination weight'):")
for _ in range(edges):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

source_vertex = int(input("Enter the source vertex to find shortest paths from: "))

shortest_distances = g.bellman_ford(source_vertex)

if shortest_distances:
    print("\nShortest distances from vertex {}:".format(source_vertex))
    for vertex, distance in enumerate(shortest_distances):
        print("Vertex {}: Distance from source = {}".format(vertex, distance))
