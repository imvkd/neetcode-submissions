class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        dirs = [1, 0, -1, 0, 1]  # Down, Right, Up, Left
        perimeter = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    for d in range(4):
                        ni = i + dirs[d]
                        nj = j + dirs[d + 1]
                        # Check if neighbor is out of bounds or water
                        if ni < 0 or ni >= r or nj < 0 or nj >= c or grid[ni][nj] == 0:
                            perimeter += 1
        return perimeter   