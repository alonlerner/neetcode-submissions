class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def calculateArea(grid, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + calculateArea(grid, i-1, j) + calculateArea(grid, i+1, j) + calculateArea(grid, i, j-1) + calculateArea(grid, i, j+1)
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(res, calculateArea(grid, i, j))
        return res