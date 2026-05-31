class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        perimeter = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += (i+1>=row or grid[i+1][j] == 0)
                    perimeter += (j+1>=col or grid[i][j+1] == 0)
                    perimeter += (i-1<0 or grid[i-1][j] == 0)
                    perimeter += (j-1<0 or grid[i][j-1] == 0)

        return perimeter