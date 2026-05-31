class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])
        sum = 0
        visited = []
        i = 0
        j = 0
        while i < r and j < c:
            if (i,j) not in visited:
                visited.append((i,j))
                sum += mat[i][j]
            i+=1
            j+=1
        print(visited)

        i = 0
        j = c-1
        while i >=0 and j>=0:
            if (i,j) not in visited:
                visited.append((i,j))
                sum += mat[i][j]
            i+=1
            j-=1
        print(visited)

        return sum