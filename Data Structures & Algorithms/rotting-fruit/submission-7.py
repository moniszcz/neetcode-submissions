from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        possible_moves = [(0,1), (0,-1), (1,0), (-1,0)]

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols


        queue = deque([])
        fresh_fruits = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_fruits += 1
        
        mins = 0
        while queue:
            r, c, mins = queue.popleft()
            for dr, dc in possible_moves:
                next_r = r + dr
                next_c = c + dc
                if in_bounds(next_r, next_c) and grid[next_r][next_c] == 1:
                    grid[next_r][next_c] = 2
                    fresh_fruits -= 1
                    queue.append((next_r, next_c, mins + 1))

        return -1 if fresh_fruits > 0 else mins         