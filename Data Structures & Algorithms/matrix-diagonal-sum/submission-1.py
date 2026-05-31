class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        m = len(mat)
        n = len(mat[0])
        for i in range(m):
            res += mat[i][i]
            res += mat[i][n-i-1]

        if n & 1:
            res -= mat[m//2][n//2]
        return res