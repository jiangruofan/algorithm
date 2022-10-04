class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        dic = defaultdict(lambda: [[float('inf'), float('inf')], [-float('inf'), -float('inf')]])
        m, n = len(targetGrid), len(targetGrid[0])
        seen = set()
        for i in range(m):
            for j in range(n):
                dic[targetGrid[i][j]][0][0] = min(dic[targetGrid[i][j]][0][0], i)
                dic[targetGrid[i][j]][0][1] = min(dic[targetGrid[i][j]][0][1], j)
                dic[targetGrid[i][j]][1][0] = max(dic[targetGrid[i][j]][1][0], i)
                dic[targetGrid[i][j]][1][1] = max(dic[targetGrid[i][j]][1][1], j)
                seen.add(targetGrid[i][j])

        graph = defaultdict(list)
        entry = Counter()
        for key, val in dic.items():
            for i in range(val[0][0], val[1][0] + 1):
                for j in range(val[0][1], val[1][1] + 1):
                    if key != targetGrid[i][j]:
                        graph[key].append(targetGrid[i][j])
                        entry[targetGrid[i][j]] += 1

        deq = deque([val for val in seen if entry[val] == 0])
        while deq:
            x = deq.popleft()
            for val in graph[x]:
                entry[val] -= 1
                if entry[val] == 0:
                    deq.append(val)

        return not any(val != 0 for val in entry.values())