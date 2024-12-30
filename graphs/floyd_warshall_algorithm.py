class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

class FloydWarshallAlgorithm(Graph):
    def floyd_warshall(self):
        dist = [[float('inf')] * self.V for _ in range(self.V)]
        for i in range(self.V):
            dist[i][i] = 0

        for u, v, w in self.graph:
            dist[u][v] = w

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist