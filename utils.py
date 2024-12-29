import importlib

ALGORITHM_MAP = {
    "basic": {
        "euclidian": ("basic.euclidian", "Euclid"),
        "huffman": ("basic.huffman", "Huffman"),
        "union_find": ("basic.union_find", "UnionFind"),
    },
    "searching": {
        "binary": ("searching.binary", "BinarySearch"),
        "depth_first": ("searching.depth_first", "DepthFirst"),
        "breadth_first": ("searching.breadth_first", "BreadthFirst"),
        "linear": ("searching.linear", "LinearSearch"),
    },
    "sorting": {
        "insertion_sort": ("sorting.insertion_sort", "InsertionSort"),
        "quick_sort": ("sorting.quick_sort", "QuickSort"),
    },
    # TODO: add more here
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
