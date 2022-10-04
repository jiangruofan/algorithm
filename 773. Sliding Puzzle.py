class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ""
        for i in range(2):
            for j in range(3):
                s += str(board[i][j])

        deq = deque([(0, s)])
        seen = set([s])
        while deq:
            num, s1 = deq.popleft()
            if s1 == "123450":
                return num
            pos = s1.index("0")
            pos_x, pos_y = pos // 3, pos % 3
            for x, y in ((pos_x+1, pos_y), (pos_x-1, pos_y), (pos_x, pos_y+1), (pos_x, pos_y-1)):
                if 0 <= x < 2 and 0 <= y < 3:
                    new_pos = x * 3 + y
                    s2 = list(s1)
                    s2[pos] = s2[new_pos]
                    s2[new_pos] = "0"
                    s2 = "".join(s2)
                    if s2 not in seen:
                        deq.append((num+1, s2))
                        seen.add(s2)
        return -1