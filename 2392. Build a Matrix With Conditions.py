class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        res = [[0 for _ in range(k)] for _ in range(k)]
        indegree = [0 for _ in range(k + 1)]
        children = defaultdict(list)
        for x, y in rowConditions:
            children[x].append(y)
            indegree[y] += 1
        index = 0
        level = [-1 for _ in range(k + 1)]
        deq = deque([i for i in range(1, k + 1) if indegree[i] == 0])
        while deq:
            for _ in range(len(deq)):
                x = deq.popleft()
                level[x] = index
                for node in children[x]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        deq.append(node)
            index += 1
        for x in indegree:
            if x != 0:
                return []

        index1 = [0 for _ in range(k + 1)]
        indegree = [0 for _ in range(k + 1)]
        children = defaultdict(list)
        for x, y in colConditions:
            children[x].append(y)
            indegree[y] += 1
        deq = deque([i for i in range(1, k + 1) if indegree[i] == 0])
        max1 = 0
        while deq:
            for _ in range(len(deq)):
                x = deq.popleft()
                res[level[x]][index1[level[x]]] = x
                index1[level[x]] += 1
                max1 = max(max1, index1[level[x]])
                for node in children[x]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        deq.append(node)
            index1 = [max1 for _ in range(k + 1)]
        for x in indegree:
            if x != 0:
                return []
        return res


