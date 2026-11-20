class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque
        possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows = len(grid)
        columns = len(grid[0])

        def in_bound(cell):
            return 0 <= cell[0] < rows and 0 <= cell[1] < columns
        
        def bfs(cell):
            queue = deque([cell])
            grid[cell[0]][cell[-1]] = "-1"

            while queue:
                curr_cell = queue.popleft()
                for dr, dc in possible_moves:
                    candidate_cell = [curr_cell[0] + dr, curr_cell[1] + dc]
                    if in_bound(candidate_cell) and grid[candidate_cell[0]][candidate_cell[1]] == '1':
                        queue.append(candidate_cell)
                        grid[candidate_cell[0]][candidate_cell[1]] = '-1'
        
        count = 0
        for row in range(rows):
            for col in range(columns):
                if grid[row][col] == '1':
                    bfs([row, col])
                    count += 1

        
        return count


        