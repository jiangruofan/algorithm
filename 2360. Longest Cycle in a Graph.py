class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        leng = len(edges)
        sons = [-1 for _ in range(leng)]
        indegree = [0 for _ in range(leng)]
        for i in range(leng):
            if edges[i] == -1:
                continue
            sons[i] = edges[i]
            indegree[edges[i]] += 1
        deq = deque([i for i in range(leng) if indegree[i] == 0])
        while deq:
            x = deq.popleft()
            if sons[x] != -1:
                indegree[sons[x]] -= 1
                if indegree[sons[x]] == 0:
                    deq.append(sons[x])
        res = -1
        left = set([i for i in range(leng) if indegree[i] == 1])
        while left:
            cnt = 1
            x = left.pop()
            while sons[x] in left:
                x = sons[x]
                left.remove(x)
                cnt += 1
            res = max(res, cnt)
        return res
