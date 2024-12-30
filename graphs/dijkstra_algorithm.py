class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}

class DijkstraAlgorithm(Graph):
    def dijkstra(self, src):
        import heapq
        distances = {i: float('inf') for i in range(self.V)}
        distances[src] = 0
        pq = [(0, src)]

        while pq:
            curr_dist, curr_vertex = heapq.heappop(pq)
            if curr_dist > distances[curr_vertex]:
                continue

            for neighbor, weight in self.adj_list[curr_vertex]:
                distance = curr_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances