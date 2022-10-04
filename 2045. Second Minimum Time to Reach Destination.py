class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        dic = defaultdict(list)
        for i, j in edges:
            dic[i].append(j)
            dic[j].append(i)
        seen = [[float('inf'), float('inf')] for _ in range(n+1)]
        seen[1][0] = 0
        deq = deque([(1, 0)])
        while seen[n][1] == float('inf'):
            index, dis = deq.popleft()
            for val in dic[index]:
                if seen[val][0] == float('inf'):
                    seen[val][0] = dis + 1
                    deq.append((val, dis + 1))
                elif dis + 1 > seen[val][0] and dis + 1 < seen[val][1]:
                    seen[val][1] = dis + 1
                    deq.append((val, dis+1))
        res = 0
        for _ in range(seen[n][1]):
            if (res // change) % 2 == 0:
                res += time
            else:
                res += time + change - res % change
        return res

