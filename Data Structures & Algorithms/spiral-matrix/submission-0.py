class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])

        left, right = 0, cols - 1
        top, bottom = 0, rows - 1

        result = []

        while left <= right and top <= bottom:
            # top row, from left to right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # last column, from top to bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # check if matrix is single row or single col
            if top > bottom or left > right:
                break

            # bottom row, from right to left
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i])
                result.append(matrix[bottom][i])
            bottom -= 1
            
            # left column, from bottom to top
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

        return result

