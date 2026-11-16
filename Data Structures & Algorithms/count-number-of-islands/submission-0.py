class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(grid, cell, visited, unvisited):
            if cell[0] >= 0 and cell[0] < len(grid) and cell[1] >= 0 and cell[1] < len(grid[0]) and not cell in visited and cell in unvisited:
                print(cell)
                visited.add(cell)
                unvisited.remove(cell)
                explore(grid, (cell[0]-1, cell[1]), visited, unvisited)
                explore(grid, (cell[0]+1, cell[1]), visited, unvisited)
                explore(grid, (cell[0], cell[1]-1), visited, unvisited)
                explore(grid, (cell[0], cell[1]+1), visited, unvisited)

        visited, unvisited = set(), set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    unvisited.add((i, j))
        print(unvisited)
        res = 0
        while len(unvisited) > 0:
            print('hi')
            res += 1
            explore(grid, next(iter(unvisited)), visited, unvisited)
        return res