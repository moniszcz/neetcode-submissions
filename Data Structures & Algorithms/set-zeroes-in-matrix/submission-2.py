"""
1. Use a hashset to keep track on cells containing zeros
Time complexity O(n*m) - one pass to populate hashset, second pass to change values
Memory complexity O(n*m) - at worst case, all elements are zero

2. We don't need coordinates of cell containing zero, we need info about which row and which column should be zeroed out. We can keep this info in first row and column. 
This means that we need additional bools to know wheter zeroes were in first column/row in the first place.
Time complexity O(n*m)
Memory complexity O(1)
"""

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        first_row_contains_zero = False
        first_col_contains_zero = False

        rows = len(matrix)
        columns = len(matrix[0])

        for c in range(columns):
            if matrix[0][c] == 0:
                first_row_contains_zero = True
        
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_contains_zero = True


        for r in range(1, rows):
            for c in range(1, columns):
                if matrix[r][c] == 0:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
        
        for r in range(1, rows):
            for c in range(1, columns):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
        
        if first_row_contains_zero:
            for c in range(columns):
                matrix[0][c] = 0
        
        if first_col_contains_zero:
            for r in range(rows):
                matrix[r][0] = 0
            













        