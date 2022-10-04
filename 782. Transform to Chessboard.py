class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j] == 1:
                    return -1
        cntR = cntC = 0
        cntR1 = cntC1 = 0
        for i in range(n):
            cntR += board[0][i]
            cntC += board[i][0]
            if board[i][0] == i % 2:
                cntC1 += 1
            if board[0][i] == i % 2:
                cntR1 += 1
        if cntR != n // 2 and cntR != (n + 1) // 2:
            return -1
        if cntC != n // 2 and cntC != (n + 1) // 2:
            return -1
        if n % 2 == 1:
            if cntC1 % 2 == 1:
                cntC1 = n - cntC1
            if cntR1 % 2 == 1:
                cntR1 = n - cntR1
        else:
            cntC1 = min(cntC1, n - cntC1)
            cntR1 = min(cntR1, n - cntR1)
        return (cntC1 + cntR1) // 2
