class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        if target == 1 and not edges:
            return 1
        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
        deq = deque([(1, 1)])
        set1 = set([1])
        cnt = 0
        while deq and cnt < t:
            leng = len(deq)
            for _ in range(leng):
                node, pro = deq.popleft()
                count = 0
                for val in dic[node]:
                    if val not in set1:
                        count += 1
                for val in dic[node]:
                    if val in set1:
                        continue
                    if val == target and (cnt == t - 1 or len(dic[val]) == 1):
                        return pro / count
                    deq.append((val, pro / count))
                    set1.add(val)
            cnt += 1
        return 0
