class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows_no = len(grid)
        columns_no = len(grid[0])
        possible_moves = [(0,1), (0,-1), (1,0), (-1, 0)]

        def in_bounds(row: int, col: int) -> bool:
            return 0 <= row < rows_no and 0 <= col < columns_no
        
        def dfs(row: int, col: int) -> int:
            #base case
            if not in_bounds(row, col) or grid[row][col] != '1':
                return

            grid[row][col] = -1
            for dr, dc in possible_moves:
                candidate_row = dr + row
                candidate_col = dc + col
                dfs(candidate_row, candidate_col)
            return
        
        counter = 0 
        for row in range(rows_no):
            for col in range(columns_no):
                if grid[row][col] == '1':
                    dfs(row, col)
                    counter += 1

        return counter

        

        