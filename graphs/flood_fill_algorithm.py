class FloodFillAlgorithm:
    @staticmethod
    def flood_fill(matrix, x, y, new_color):
        rows, cols = len(matrix), len(matrix[0])
        original_color = matrix[x][y]
        if original_color == new_color:
            return matrix

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] != original_color:
                return
            matrix[r][c] = new_color
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                dfs(r + dr, c + dc)

        dfs(x, y)
        return matrix