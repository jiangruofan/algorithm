class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        leng = len(edges)
        res = 0
        distance = [float('inf') for _ in range(n)]
        dic = defaultdict(list)
        for x, y, dis in edges:
            dic[x].append((y, dis + 1))
            dic[y].append((x, dis + 1))

        heap = [(0, 0)]
        while heap:
            dis, node = heappop(heap)
            if dis >= distance[node]:
                continue
            if dis <= maxMoves:
                res += 1
            distance[node] = dis
            for val, dis1 in dic[node]:
                if dis + dis1 < distance[val]:
                    heappush(heap, (dis + dis1, val))

        for x, y, num in edges:
            num1 = max(0, maxMoves - distance[x])
            num2 = max(0, maxMoves - distance[y])
            res += min(num1 + num2, num)
        return res