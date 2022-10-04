class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        entry = [0 for _ in range(n)]
        dic = defaultdict(list)
        for x, y in edges:
            dic[x].append(y)
            dic[y].append(x)
            entry[x] += 1
            entry[y] += 1
        deq = deque([i for i in range(n) if entry[i] == 1])
        seen = set(deq)
        while deq:
            x = deq.popleft()
            for node in dic[x]:
                if node in seen:
                    continue
                entry[node] -= 1
                if entry[node] == 1:
                    deq.append(node)
                    seen.add(node)

        ans = [0 for _ in range(n)]
        deq = deque([i for i in range(n) if entry[i] != 1])
        seen = set(deq)
        total = 1
        while deq:
            leng = len(deq)
            for _ in range(leng):
                x = deq.popleft()
                for node in dic[x]:
                    if node in seen:
                        continue
                    deq.append(node)
                    ans[node] = total
                    seen.add(node)
            total += 1
        return ans