import unittest
from Basic.huffman import Huffman
from Basic.union_find import UnionFind
from Basic.euclidian import Euclid

class TestBasicAlgorithms(unittest.TestCase):

    # Test for Huffman Encoding
    def test_huffman(self):
        text = "huffman example"
        huffman = Huffman()

        encoded = huffman.encode(text)
        decoded = huffman.decode(encoded)

        self.assertEqual(decoded, text, "Decoded text should match the original text")

    # Test for Union-Find (Disjoint Set Union)
    def test_union_find(self):
        n = 5
        uf = UnionFind(n)

        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(3, 4)

        self.assertEqual(uf.find(0), uf.find(1), "Elements 0 and 1 should have the same representative")
        self.assertEqual(uf.find(1), uf.find(2), "Elements 1 and 2 should have the same representative")
        self.assertNotEqual(uf.find(0), uf.find(3), "Elements 0 and 3 should not have the same representative")

    # Test for Euclid's GCD
    def test_euclid_gcd(self):
        euc = Euclid(48, 18)
        self.assertEqual(euc.gcd(), 6, "GCD of 48 and 18 should be 6")

        euc = Euclid(101, 103)
        self.assertEqual(euc.gcd(), 1, "GCD of 101 and 103 should be 1")

if __name__ == "__main__":
    unittest.main()