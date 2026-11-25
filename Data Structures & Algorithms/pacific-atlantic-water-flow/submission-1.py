class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        pac = set([(0,c) for c in range(COL)] + [(r, 0) for r in range(ROW)])
        atl = set([(ROW - 1,c) for c in range(COL)] + [(r, COL - 1) for r in range(ROW)])
        
        q = list(pac)
        while q:
            cell = q.pop()
            for r, c in directions:
                i, j = cell[0] + r, cell[1] + c
                if i >= 0 and i < ROW and j >= 0 and j < COL and not (i, j) in pac and heights[cell[0]][cell[1]] <= heights[i][j]:
                    pac.add((i, j))
                    q.append((i, j))
        
        q = list(atl)
        while q:
            cell = q.pop()
            for r, c in directions:
                i, j = cell[0] + r, cell[1] + c
                if i >= 0 and i < ROW and j >= 0 and j < COL and not (i ,j) in atl and heights[cell[0]][cell[1]] <= heights[i][j]:
                    atl.add((i, j))
                    q.append((i, j))

        res = []
        for i in range(ROW):
            for j in range(COL):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res