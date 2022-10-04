class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        trees =[]
        m, n = len(forest), len(forest[0])
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()

        def calDistance(x, y, x1, y1):
            deq = deque([(x, y)])
            seen = set(deq)
            res = 0
            while deq:
                leng = len(deq)
                for _ in range(leng):
                    x2, y2 = deq.popleft()
                    for i, j in ((x2+1, y2), (x2-1, y2), (x2, y2+1), (x2, y2-1)):
                        if 0 <= i < m and 0 <= j < n and (i, j) not in seen and forest[i][j] != 0:
                            if i == x1 and j == y1:
                                return res + 1
                            deq.append((i, j))
                            seen.add((i, j))
                res += 1
            return -1
        ans = calDistance(0, 0, trees[0][1], trees[0][2]) if trees[0][0] != forest[0][0] else 0
        for i in range(1, len(trees)):
            cnt = calDistance(trees[i-1][1], trees[i-1][2], trees[i][1], trees[i][2])
            if cnt == -1:
                return -1
            ans += cnt
        return ans