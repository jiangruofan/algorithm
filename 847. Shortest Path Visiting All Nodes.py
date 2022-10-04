class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        leng = len(graph)
        n = (1 << leng) - 1
        deq = deque([(node, n & ~(1 << node)) for node in range(leng)])
        visited = set([(node, n & ~(1 << node)) for node in range(leng)])
        res = 0
        while deq:
            x = len(deq)
            for _ in range(x):
                node, seen = deq.popleft()
                for val in graph[node]:
                    new_seen = seen & ~(1 << val)
                    if new_seen == 0:
                        return res + 1
                    if (val, new_seen) not in visited:
                        deq.append((val, new_seen))
                        visited.add((val, new_seen))
            res += 1
        return 0
