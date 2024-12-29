import importlib

ALGORITHM_MAP = {
    "Arrays": {
        "kadane": ("Arrays.kadane", "Kadane"),
        "floyd": ("Arrays.floyd", "Floyd"),
        "KMP": ("Arrays.KMP", "KMP"),
        "quick_select": ("Arrays.quick_select", "QuickSelect"),
        "boyer_moore": ("Arrays.boyer_moore", "BoyerMoore"),
    },    
    "Basic": {
        "euclidian": ("Basic.euclidian", "Euclid"),
        "huffman": ("Basic.huffman", "Huffman"),
        "union_find": ("Basic.union_find", "UnionFind"),
    },
    "graphs": {
        "bellman_ford": ("graphs.bellman_ford", "BellmanFord"),
        "dijkstra": ("graphs.djikstra", "Djikstra"),
        "flood_fill": ("graphs.flood_fill", "FloodFill"),
        "floyd_warshall": ("graphs.floyd_warshall", "FloydWarshall"),
        "kruskal": ("graphs.kruskal", "Kruskal"),
        "lee": ("graphs.lee", "Lee"),
        "topological_sort": ("graphs.topological_sort", "TopologicalSort"),
    },
    "searching": {
        "binary": ("searching.binary", "BinarySearch"),
        "depth_first": ("searching.depth_first", "DepthFirst"),
        "breadth_first": ("searching.breadth_first", "BreadthFirst"),
        "linear": ("searching.linear", "LinearSearch"),
    },
    "sorting": {
        "insertion_sort": ("sorting.insertion_sort", "InsertionSort"),
        "selection_sort": ("sorting.selection_sort", "SelectionSort"),
        "heap_sort": ("sorting.heap_sort", "HeapSort"),
        "merge_sort": ("sorting.merge_sort", "MergeSort"),
        "quick_sort": ("sorting.quick_sort", "QuickSort"),
        "counting_sort": ("sorting.counting_sort", "CountingSort"),
    },
}

def get_available_algorithms():
    return ALGORITHM_MAP

def load_algorithm(category, algorithm):
    if category not in ALGORITHM_MAP:
        raise ValueError(f"Category '{category}' is not available. Use '--help' to list available categories.")
    if algorithm not in ALGORITHM_MAP[category]:
        raise ValueError(f"Algorithm '{algorithm}' is not available in category '{category}'. Use '--help' to list available algorithms.")

    module_name, class_name = ALGORITHM_MAP[category][algorithm]
    
    try:
        module = importlib.import_module(module_name)
        return getattr(module, class_name)()
    except Exception as e:
        raise ValueError(f"Error loading algorithm '{algorithm}' from category '{category}': {e}")
