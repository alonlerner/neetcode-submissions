class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        pac = set([(0, j) for j in range(len(heights[0]))] + [(i, 0) for i in range(len(heights))])
        atl = set([(len(heights) - 1, j) for j in range(len(heights[0]))] + [(i, len(heights[0]) - 1) for i in range(len(heights))])
        q = list(pac)
        while q:
            h = q.pop()
            for r, c in directions:
                i, j = h[0] + r, h[1] + c
                if i >= 0 and i < len(heights) and j >= 0 and j < len(heights[i]) and not (i, j) in pac and heights[h[0]][h[1]] <= heights[i][j]:
                    pac.add((i, j))
                    q.append((i, j))
        q = list(atl)
        while q:
            h = q.pop()
            for r, c in directions:
                i, j = h[0] + r, h[1] + c
                if i >= 0 and i < len(heights) and j >= 0 and j < len(heights[i]) and not (i, j) in atl and heights[h[0]][h[1]] <= heights[i][j]:
                    atl.add((i, j))
                    q.append((i, j))
        res = []
        for i in range(len(heights)):
            for j in range(len(heights[i])):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res