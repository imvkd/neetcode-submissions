class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        visited = set()
        res = []
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] in visited:
                    res.append(grid[i][j])
                visited.add(grid[i][j])

        for i in range(1, n*n+1):
            if i not in visited:
                res.append(i)
                break
        
        return res

