class Solution:
    def minDayskVariants(self, points: List[List[int]], k: int) -> int:
        n = len(points)
        cnt = Counter()
        seen = [set() for _ in range(n)]

        up = right = -1
        for x, y in points:
            right = max(right, x)
            up = max(up, y)

        def oneD(x, y):
            return y * right + x

        def twoD(x):
            return (x % right, x // right)

        deq = deque()
        for i, (x, y) in enumerate(points):
            val = oneD(x - 1, y - 1)
            deq.append((val, i))
            seen[i].add(val)
            cnt[val] += 1
            if cnt[val] == k:
                return 0

        res = 0
        while deq:
            res += 1
            leng = len(deq)
            for _ in range(leng):
                point, index = deq.popleft()
                x, y = twoD(point)
                for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                    if 0 <= i < right and 0 <= j < up and oneD(i, j) not in seen[index]:
                        seen[index].add(oneD(i, j))
                        deq.append((oneD(i, j), index))
                        cnt[oneD(i, j)] += 1
                        if cnt[oneD(i, j)] == k:
                            return res
