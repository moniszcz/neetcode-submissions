class Solution:
    from collections import deque
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        possible_moves = [(0,1), (0,-1), (1,0), (-1,0)]
        max_area = 0

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols


        def bfs(r: int, c: int) -> None:
            queue = deque([(r, c)])
            grid[r][c] = 0
            area = 0

            while queue:
                r, c = queue.popleft()
                area += 1
                for dr, dc in possible_moves:
                    next_r = dr + r
                    next_c = dc + c
                    if in_bounds(next_r, next_c) and grid[next_r][next_c] == 1:
                        grid[next_r][next_c] = 0
                        queue.append((next_r, next_c))
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(bfs(r, c), max_area)
        
        return max_area
