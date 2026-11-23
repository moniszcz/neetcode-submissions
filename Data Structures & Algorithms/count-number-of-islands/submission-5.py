class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols

        possible_moves = [(0,1), (0,-1), (1,0), (-1, 0)]

        def dfs(r: int, c: int) -> None:
            # iterative DFS
            grid[r][c] = '-1'
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                for dr, dc in possible_moves:
                    next_r = dr + r
                    next_c = dc + c
                    if in_bounds(next_r, next_c) and grid[next_r][next_c] == '1':
                        grid[next_r][next_c] = '-1'
                        stack.append((next_r, next_c))

            return

        island = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    island += 1

        return island