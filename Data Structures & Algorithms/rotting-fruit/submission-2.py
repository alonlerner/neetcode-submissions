class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        freshCount = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        if freshCount == 0: return 0
        minutes = 0
        while q:
            qLen  = len(q)
            minutes += 1
            for m in range(qLen):
                rotten = q.popleft()
                for col, row in directions:
                    i = rotten[0] + col
                    j = rotten[1] + row
                    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]) and grid[i][j] == 1:
                        q.append((i, j))
                        grid[i][j] = 2
                        freshCount -= 1
                        if freshCount == 0:
                            return minutes
            print(q, freshCount)
        return -1