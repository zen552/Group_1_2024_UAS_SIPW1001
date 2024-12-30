import unittest
from searching.binary import binary_search
from searching.breadth_first import bfs
from searching.depth_first import dfs
from searching.linear import linear_search


class TestSearchingAlgorithms(unittest.TestCase):

    # Test for Binary Search
    def test_binary_search(self):
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 3), 2)   # Elemen ditemukan di indeks 2
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 6), -1)  # Elemen tidak ditemukan
        self.assertEqual(binary_search([], 3), -1)               # Array kosong
        self.assertEqual(binary_search([1, 2, 3, 4, 5], 1), 0)   # Elemen ditemukan di indeks 0

    # Test for Breadth-First Search
    def test_bfs(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }
        self.assertEqual(bfs(graph, 'A'), {'A', 'B', 'C', 'D', 'E', 'F'})  # Semua node dijelajahi
        self.assertEqual(bfs(graph, 'D'), {'D', 'B', 'A', 'E', 'C', 'F'})  # Mulai dari 'D'

    # Test for Depth-First Search
    def test_dfs(self):
        graph = {
            'A': ['B', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F'],
            'D': ['B'],
            'E': ['B', 'F'],
            'F': ['C', 'E']
        }
        self.assertEqual(dfs(graph, 'A'), {'A', 'B', 'C', 'D', 'E', 'F'})  # Semua node dijelajahi
        self.assertEqual(dfs(graph, 'D'), {'D', 'B', 'A', 'E', 'C', 'F'})  # Mulai dari 'D'

    # Test for Linear Search
    def test_linear_search(self):
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 3), 2)  # Elemen ditemukan di indeks 2
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 6), -1) # Elemen tidak ditemukan
        self.assertEqual(linear_search([], 3), -1)              # Array kosong
        self.assertEqual(linear_search([1, 2, 3, 4, 5], 1), 0)  # Elemen ditemukan di indeks 0


if __name__ == "__main__":
    unittest.main()