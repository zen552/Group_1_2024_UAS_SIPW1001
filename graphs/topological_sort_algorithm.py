class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(vertices)}

class TopologicalSortAlgorithm(Graph):
    def topological_sort(self):
        visited = [False] * self.V
        stack = []

        def dfs(v):
            visited[v] = True
            for neighbor in self.adj_list[v]:
                if not visited[neighbor]:
                    dfs(neighbor)
            stack.append(v)

        for i in range(self.V):
            if not visited[i]:
                dfs(i)

        return stack[::-1]