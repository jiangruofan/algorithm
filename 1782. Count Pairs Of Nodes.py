class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        entry = [0 for _ in range(n+1)]
        repeated = defaultdict(lambda: Counter())

        for x, y in edges:
            entry[x] += 1
            entry[y] += 1
            repeated[min(x, y)][max(x, y)] += 1
        entry_old = entry[::]
        entry.sort()
        leng = len(entry)
        res = []
        for k in queries:
            cnt = 0
            l = 1
            r = leng - 1
            while l < r:
                while r > l and entry[l] + entry[r] > k:
                    r -= 1
                cnt += leng - 1 - r
                l += 1
            cnt += (leng - 1 - l) * (leng - l) // 2
            for x in repeated:
                for y in repeated[x]:
                    if entry_old[x] + entry_old[y] > k and entry_old[x] + entry_old[y] - repeated[x][y] <= k:
                        cnt -= 1
            res.append(cnt)
        return res