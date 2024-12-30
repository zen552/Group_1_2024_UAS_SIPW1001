class LeeAlgorithm:
    @staticmethod
    def lee_algorithm(grid, start, end):
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        queue = deque([(start[0], start[1], 0)])
        visited = set()
        visited.add((start[0], start[1]))

        while queue:
            x, y, dist = queue.popleft()
            if (x, y) == end:
                return dist

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny, dist + 1))

        return -1