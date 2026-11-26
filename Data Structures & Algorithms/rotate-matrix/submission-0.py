class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # (i, j) - > (j, n - 1 - i)
        n = len(matrix)
        matrix.reverse()

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        