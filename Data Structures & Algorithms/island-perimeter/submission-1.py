class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    perimeter += (i-1 < 0 or grid[i-1][j] == 0)
                    perimeter += (i+1 == r or grid[i+1][j] == 0)
                    perimeter += (j-1 < 0 or grid[i][j-1] == 0)
                    perimeter += (j+1 == c or grid[i][j+1] == 0)
        return perimeter