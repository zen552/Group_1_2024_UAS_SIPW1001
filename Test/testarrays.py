import unittest
from Arrays.floyd import Node, LinkedList, Floyd
from Arrays.kadane import Kadane
from Arrays.KMP import KMP
from Arrays.quick_select import QuickSelect
from Arrays.boyer_moore import BoyerMoore

#python -m unittest discover -s Test

class TestAlgorithms(unittest.TestCase):

    # Test for Floyd's Cycle Detection
    def test_floyd_cycle_detection(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        # Creating a cycle
        node1.nxt = node2
        node2.nxt = node3
        node3.nxt = node4
        node4.nxt = node2  # Cycle here

        ll = LinkedList(node1)
        result = Floyd.cycle(ll)
        self.assertEqual(result.val, 2, "Cycle should be detected at node with value 2")

        # No cycle case
        node4.nxt = None  # Break the cycle
        result = Floyd.cycle(ll)
        self.assertIsNone(result, "No cycle should be detected")

    def test_floyd_find_duplicate(self):
        arr = [1, 3, 4, 2, 2]
        result = Floyd.find_duplicate(arr)
        self.assertEqual(result, 2, "Duplicate element should be 2")

    # Test for Kadane's Algorithm
    def test_kadane(self):
        arr = [-2, 1, -3, 4, -1, 2, 1, 5, -4]
        result = Kadane.run(arr)
        self.assertEqual(result, 11, "Maximum subarray sum should be 11")

    # Test for KMP Algorithm
    def test_kmp(self):
        text = "ababcabcabababd"
        pattern = "ababd"
        result = KMP.run(text, pattern)
        self.assertEqual(result, 10, "Pattern should be found at index 10")

    # Test for QuickSelect Algorithm
    def test_quick_select(self):
        arr = [10, 4, 5, 8, 6, 11, 26]
        k = 1
        result = QuickSelect.run(arr, 0, len(arr) - 1, k)
        self.assertEqual(result, 4, "1st smallest element should be 4")

    # Test for Boyer-Moore Algorithm
    def test_boyer_moore(self):
        text = "ABAAABCD"
        pattern = "ABC"
        bm = BoyerMoore(pattern)
        result = bm.search(text)
        self.assertEqual(result, [4], "Pattern should be found at position 4")

if __name__ == "__main__":
    unittest.main()