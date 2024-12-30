import heapq
from collections import Counter

class Tree:
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq


class Huffman:
    def __init__(self) -> None:
        self.root = None
        self.encoding_map = {}

    def build_tree(self, text):
        counter = Counter(text)
        pq = [Tree(ch, counter[ch]) for ch in counter]
        heapq.heapify(pq)
        while len(pq) > 1:
            left = heapq.heappop(pq)
            right = heapq.heappop(pq)
            parent = Tree(None, left.freq + right.freq, left, right)
            heapq.heappush(pq, parent)
        self.root = heapq.heappop(pq)

    def build_map(self, root=None):
        def dfs(node, code):
            if node.ch:
                self.encoding_map[node.ch] = ''.join(code)
                return
            if node.left:
                dfs(node.left, code + ['0'])
            if node.right:
                dfs(node.right, code + ['1'])

        if not root:
            root = self.root
        dfs(root, [])

    def encode(self, text):
        if not self.root:
            self.build_tree(text)
            self.build_map(self.root)
        return ''.join([self.encoding_map[ch] for ch in text])

    def decode(self, encoded):
        decoded = []
        node = self.root
        for bit in encoded:
            node = node.left if bit == '0' else node.right
            if node.ch:
                decoded.append(node.ch)
                node = self.root
        return ''.join(decoded)


# Contoh Penggunaan
if __name__ == "__main__":
    huffman = Huffman()
    text = "huffman example"  
    encoded = huffman.encode(text)
    print(f"Encoded: {encoded}")
    decoded = huffman.decode(encoded)
    print(f"Decoded: {decoded}")