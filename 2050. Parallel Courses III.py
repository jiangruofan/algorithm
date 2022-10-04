class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        entry = [0 for _ in range(n+1)]
        cnt = [0 for _ in range(n+1)]
        dic = defaultdict(list)
        for x, y in relations:
            entry[y] += 1
            dic[x].append(y)
        res = 0
        deq = deque([i for i in range(1, n+1) if entry[i] == 0])
        while deq:
            x = deq.popleft()
            if not dic[x]:
                res = max(res, cnt[x] + time[x-1])
                continue
            for val in dic[x]:
                entry[val] -= 1
                cnt[val] = max(cnt[val], cnt[x] + time[x-1])
                if entry[val] == 0:
                    deq.append(val)
        return res