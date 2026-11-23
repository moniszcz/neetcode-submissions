class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterative DFS
        rows_no = len(grid)
        cols_no = len(grid[0])

        def in_bounds(row: int, col: int) -> bool:
            return 0 <= row < rows_no and 0 <= col < cols_no

        possible_moves = [(0,1), (0,-1), (1,0), (-1, 0)]

        def dfs(row: int, col: int) -> None:
            stack = [(row, col)]
            grid[row][col] = '-1'

            while stack:
                cell = stack.pop()
                curr_row = cell[0]
                curr_col = cell[1]
                for dr, dc in possible_moves:
                    candidate_r = dr + curr_row
                    candidate_c = dc + curr_col
                    candidate_cell = (candidate_r, candidate_c)
                    if (in_bounds(*candidate_cell) 
                    and grid[candidate_r][candidate_c] == '1'):
                        stack.append(candidate_cell)
                        grid[candidate_r][candidate_c] = '-1'
            
            return

        counter = 0
        for curr_row in range(rows_no):
            for curr_col in range(cols_no):
                if grid[curr_row][curr_col] == '1':
                    dfs(curr_row, curr_col)
                    counter += 1

        
        return counter