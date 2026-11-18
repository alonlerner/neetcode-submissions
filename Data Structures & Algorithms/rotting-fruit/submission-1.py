class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        freshCount = 0
        rotten = [[]]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    rotten[-1].append((i, j))
        while freshCount > 0 and len(rotten[-1]) > 0:
            rotten.append([])
            for i, j in rotten[-2]:
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    freshCount -= 1
                    rotten[-1].append((i - 1, j))
                if i + 1 < len(grid) and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    freshCount -= 1
                    rotten[-1].append((i + 1, j))
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    freshCount -= 1
                    rotten[-1].append((i, j - 1))
                if j + 1 < len(grid[i]) and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    freshCount -= 1
                    rotten[-1].append((i, j + 1))
        return len(rotten) - 1 if freshCount == 0 else -1