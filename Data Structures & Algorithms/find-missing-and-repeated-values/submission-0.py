class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        temp = [-1] * (n*n)
        res = []
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] in temp:
                    res.append(grid[i][j])
                temp[grid[i][j]-1] = grid[i][j]
                
        for i in range(len(temp)):
            if temp[i] == -1:
                res.append(i+1)
        
        return res

