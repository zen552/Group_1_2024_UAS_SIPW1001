import unittest
from graphs.flood_fill import FloodFillAlgorithm
from graphs.floyd_warshall import FloydWarshallAlgorithm
from graphs.kruskal import KruskalAlgorithm
from graphs.lee_algorithm import LeeAlgorithm
from graphs.topological_sort_algorithm import TopologicalSortAlgorithm
from graphs.bellman_ford import BellmanFordAlgorithm
from graphs.dijkstra import DijkstraAlgorithm


class TestGraphAlgorithms(unittest.TestCase):

    # Test for Flood Fill Algorithm
    def test_flood_fill(self):
        matrix = [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1]
        ]
        result = FloodFillAlgorithm.flood_fill(matrix, 1, 1, 2)
        expected = [
            [2, 2, 2],
            [2, 2, 0],
            [2, 0, 1]
        ]
        self.assertEqual(result, expected)

    # Test for Floyd-Warshall Algorithm
    def test_floyd_warshall(self):
        graph = FloydWarshallAlgorithm(4)
        graph.graph = [
            [0, 1, 5],
            [1, 2, 3],
            [2, 3, 1],
            [0, 3, 10]
        ]
        result = graph.floyd_warshall()
        expected = [
            [0, 5, 8, 9],
            [float('inf'), 0, 3, 4],
            [float('inf'), float('inf'), 0, 1],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        self.assertEqual(result, expected)

    # Test for Kruskal's Algorithm
    def test_kruskal(self):
        graph = KruskalAlgorithm(4)
        graph.add_edge(0, 1, 10)
        graph.add_edge(0, 2, 6)
        graph.add_edge(0, 3, 5)
        graph.add_edge(1, 3, 15)
        graph.add_edge(2, 3, 4)
        result = graph.kruskal()
        expected = [
            [2, 3, 4],
            [0, 3, 5],
            [0, 1, 10]
        ]
        self.assertEqual(result, expected)

    # Test for Lee Algorithm
    def test_lee_algorithm(self):
        grid = [
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [1, 1, 0, 0]
        ]
        start = (0, 0)
        end = (3, 3)
        result = LeeAlgorithm.lee_algorithm(grid, start, end)
        self.assertEqual(result, 6)

    # Test for Topological Sort Algorithm
    def test_topological_sort(self):
        graph = TopologicalSortAlgorithm(6)
        graph.adj_list = {
            5: [2, 0],
            4: [0, 1],
            2: [3],
            3: [1],
            0: [],
            1: []
        }
        result = graph.topological_sort()

        # Validasi: semua edges mengikuti aturan topological order
        position = {node: index for index, node in enumerate(result)}
        for u in graph.adj_list:
            for v in graph.adj_list[u]:
                self.assertLess(position[u], position[v])  # u harus datang sebelum v

    # Test for Bellman-Ford Algorithm
    def test_bellman_ford(self):
        graph = BellmanFordAlgorithm(5)
        graph.graph = [
            [0, 1, -1],
            [0, 2, 4],
            [1, 2, 3],
            [1, 3, 2],
            [1, 4, 2],
            [3, 2, 5],
            [3, 1, 1],
            [4, 3, -3]
        ]
        result = graph.bellman_ford(0)
        expected = {0: 0, 1: -1, 2: 2, 3: -2, 4: 1}
        self.assertEqual(result, expected)

    # Test for Dijkstra's Algorithm
    def test_dijkstra(self):
        graph = DijkstraAlgorithm(5)
        graph.adj_list = {
            0: [(1, 10), (2, 3)],
            1: [(2, 1), (3, 2)],
            2: [(1, 4), (3, 8), (4, 2)],
            3: [(4, 7)],
            4: [(3, 9)]
        }
        result = graph.dijkstra(0)
        expected = {0: 0, 1: 7, 2: 3, 3: 9, 4: 5}
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()