class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        possible_moves = [(0,1), (0,-1), (1,0), (-1,0)]

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols
        
        def dfs(r: int, c: int) -> None:
            # base case
            if not in_bounds(r, c) or grid[r][c] != '1':
                return

            grid[r][c] = '-1'
            for dr, dc in possible_moves:
                dfs(dr + r, dc + c)

        
        islands = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands

        

        