from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        cols = len(grid[0])

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols
        
        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            grid[r][c] = "-1"

            while queue:
                r, c = queue.popleft()
                for dr, dc in possible_moves:
                    next_r = r + dr
                    next_c = c + dc
                    if in_bounds(next_r, next_c) and grid[next_r][next_c] == '1':
                        queue.append((next_r, next_c))
                        grid[next_r][next_c] = '-1'
        
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    islands += 1

        return islands


        