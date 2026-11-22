class Solution:
    def solve(self, board: List[List[str]]) -> None:
        r, c = len(board), len(board[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        nonSurO = set([(i, 0) for i in range(r) if board[i][0] == 'O'] + [(i, c-1) for i in range(r) if board[i][c-1] == 'O'] + [(0, i) for i in range(c) if board[0][i] == 'O'] + [(r-1, i) for i in range(c) if board[r-1][i] == 'O'])

        q = deque(list(nonSurO))
        while q:
            cell = q.popleft()
            for dr, dc in directions:
                row, col = cell[0] + dr, cell[1] + dc
                if row >= 0 and row < r and col >= 0 and col < c and not (row, col) in nonSurO and board[row][col] == 'O':
                    q.append((row, col))
                    nonSurO.add((row, col))
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O' and not (i, j) in nonSurO:
                    board[i][j] = 'X'