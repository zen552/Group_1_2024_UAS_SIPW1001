
from collections import deque

# Directions for moving: Up, Down, Left, Right
row_directions = [-1, 1, 0, 0]
col_directions = [0, 0, -1, 1]

def is_valid_move(grid, visited, row, col):
    rows, cols = len(grid), len(grid[0])
    return 0 <= row < rows and 0 <= col < cols and not visited[row][col] and grid[row][col] == 1

def lee_algorithm(grid, start, destination):
    if not grid or not grid[0]:
        return -1  # Invalid grid
    
    rows, cols = len(grid), len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])  # (row, col, distance)
    visited[start[0]][start[1]] = True

    while queue:
        current_row, current_col, distance = queue.popleft()
        
        # Check if we've reached the destination
        if (current_row, current_col) == destination:
            return distance

        # Explore neighbors
        for direction in range(4):
            new_row = current_row + row_directions[direction]
            new_col = current_col + col_directions[direction]
            
            if is_valid_move(grid, visited, new_row, new_col):
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, distance + 1))

    return -1  # Destination cannot be reached

# Example usage
if __name__ == "__main__":
    maze = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [0, 1, 0, 1, 1],
        [1, 1, 1, 1, 0],
        [1, 0, 1, 1, 1]
    ]
    start = (0, 0)
    destination = (4, 4)

    result = lee_algorithm(maze, start, destination)
    print("Shortest Path Distance:", result)
