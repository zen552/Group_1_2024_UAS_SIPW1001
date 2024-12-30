class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

# Contoh Penggunaan
if __name__ == "__main__":
    n = 5  # Jumlah elemen (0, 1, 2, 3, 4)
    uf = UnionFind(n)

    uf.union(0, 1)
    uf.union(1, 2)
    uf.union(3, 4)

    print("Representative:", uf.find(0))
    print("Representative:", uf.find(3))  

    print(uf.find(0) == uf.find(2))  
    print(uf.find(1) == uf.find(3))  
