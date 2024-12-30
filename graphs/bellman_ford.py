class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

class BellmanFordAlgorithm(Graph):
    def bellman_ford(self, src):
        distances = {i: float('inf') for i in range(self.V)}
        distances[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    distances[v] = distances[u] + w

        for u, v, w in self.graph:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                raise ValueError("Graph contains a negative weight cycle")

        return distances