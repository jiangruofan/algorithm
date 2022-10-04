class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        dic1 = defaultdict(lambda: defaultdict(lambda: float('inf')))
        dic2 = defaultdict(lambda: defaultdict(lambda: float('inf')))
        for start, end, dis in edges:
            dic1[start][end] = min(dis, dic1[start][end])
            dic2[end][start] = min(dis, dic2[end][start])
        def dijk(dic, start):
            res = [float('inf') for _ in range(n)]
            res[start] = 0
            heap = [(0, start)]
            while heap:
                dis, node = heappop(heap)
                for key, val in dic[node].items():
                    if dis + val < res[key]:
                        res[key] = dis + val
                        heappush(heap, (res[key], key))
            return res
        list1 = dijk(dic1, src1)
        list2 = dijk(dic1, src2)
        list3 = dijk(dic2, dest)
        res = float('inf')
        for i in range(n):
            res = min(res, list1[i] + list2[i] + list3[i])
        return res if res != float('inf') else -1