class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def in_bounds(r: int, c: int) -> bool:
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r: int, c: int) -> int:
            if not in_bounds(r, c) or grid[r][c] != 1:
                return 0

            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += dfs(dr + r, dc + c)

            return area

        max_area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area,dfs(r, c))
        
        return max_area
                
                

             
        