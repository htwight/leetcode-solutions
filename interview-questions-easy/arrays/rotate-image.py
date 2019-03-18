from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix[:] = matrix[::-1]
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
