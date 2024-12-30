import unittest
from sorting.heap_sort import heap_sort
from sorting.insertion_sort import insertion_sort
from sorting.merge_sort import merge_sort
from sorting.quick_sort import quick_sort
from sorting.selection_sort import selection_sort
from sorting.counting_sort import counting_sort


class TestSortingAlgorithms(unittest.TestCase):

    # Test for Heap Sort
    def test_heap_sort(self):
        self.assertEqual(heap_sort([4, 10, 3, 5, 1]), [1, 3, 4, 5, 10])  # [1, 3, 4, 5, 10]
        self.assertEqual(heap_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])    # [1, 2, 3, 4, 5]
        self.assertEqual(heap_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])    # [1, 2, 3, 4, 5]
        self.assertEqual(heap_sort([]), [])                              # []

    # Test for Insertion Sort
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([4, 3, 2, 1]), [1, 2, 3, 4])     # [1, 2, 3, 4]
        self.assertEqual(insertion_sort([5, 1, 4, 2]), [1, 2, 4, 5])     # [1, 2, 4, 5]
        self.assertEqual(insertion_sort([1]), [1])                       # [1]
        self.assertEqual(insertion_sort([]), [])                         # []

    # Test for Merge Sort
    def test_merge_sort(self):
        self.assertEqual(merge_sort([5, 3, 8, 6, 2]), [2, 3, 5, 6, 8])   # [2, 3, 5, 6, 8]
        self.assertEqual(merge_sort([1, 4, 3, 2]), [1, 2, 3, 4])         # [1, 2, 3, 4]
        self.assertEqual(merge_sort([1]), [1])                           # [1]
        self.assertEqual(merge_sort([]), [])                             # []

    # Test for Quick Sort
    def test_quick_sort(self):
        self.assertEqual(quick_sort([4, 2, 7, 1, 9]), [1, 2, 4, 7, 9])   # [1, 2, 4, 7, 9]
        self.assertEqual(quick_sort([3, 3, 2, 1]), [1, 2, 3, 3])         # [1, 2, 3, 3]
        self.assertEqual(quick_sort([1]), [1])                           # [1]
        self.assertEqual(quick_sort([]), [])                             # []

    # Test for Selection Sort
    def test_selection_sort(self):
        self.assertEqual(selection_sort([3, 2, 5, 1]), [1, 2, 3, 5])     # [1, 2, 3, 5]
        self.assertEqual(selection_sort([1, 1, 1, 1]), [1, 1, 1, 1])     # [1, 1, 1, 1]
        self.assertEqual(selection_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]) # [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort([]), [])                         # []

    # Test for Counting Sort
    def test_counting_sort(self):
        self.assertEqual(counting_sort([4, 2, 2, 8, 3, 3, 1]), [1, 2, 2, 3, 3, 4, 8]) # [1, 2, 2, 3, 3, 4, 8]
        self.assertEqual(counting_sort([5, 5, 5, 5]), [5, 5, 5, 5])                   # [5, 5, 5, 5]
        self.assertEqual(counting_sort([1, 4, 1, 2]), [1, 1, 2, 4])                   # [1, 1, 2, 4]
        self.assertEqual(counting_sort([]), [])                                       # []

if __name__ == "__main__":
    unittest.main()