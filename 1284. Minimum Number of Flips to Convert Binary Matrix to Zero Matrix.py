class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        begin = ''
        for i in range(m):
            for j in range(n):
                begin += str(mat[i][j])

        if begin == "0" * m * n:
            return 0

        seen = set([begin])
        deq = deque([begin])
        level = 0

        while deq:
            leng = len(deq)
            for _ in range(leng):
                s = deq.popleft()
                for i in range(len(s)):
                    s1 = list(s)
                    set1 = set([i])
                    x = i // n
                    y = i % n
                    for x1, y1 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                        if 0 <= x1 < m and 0 <= y1 < n:
                            set1.add(x1 * n + y1)
                    for val in set1:
                        s1[val] = "1" if s1[val] == "0" else "0"
                    s1 = "".join(s1)
                    if s1 == "0" * m * n:
                        return level + 1
                    if s1 not in seen:
                        deq.append(s1)
                        seen.add(s1)
            level += 1

        return -1