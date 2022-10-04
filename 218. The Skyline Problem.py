class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        list1 = []
        for l, r, h in buildings:
            list1.append((l, -h))
            list1.append((r, h))
        list1.sort()

        heap = [0]
        dic = Counter()
        res = []
        for x, h in list1:
            if h < 0:
                while -heap[0] in dic:
                    dic[-heap[0]] -= 1
                    if dic[-heap[0]] == 0:
                        del dic[-heap[0]]
                    heappop(heap)
                pre = heap[0]
                heappush(heap, h)
                if heap[0] < pre:
                    res.append([x, -h])
            else:
                dic[h] += 1
                pre = heap[0]
                while -heap[0] in dic:
                    dic[-heap[0]] -= 1
                    if dic[-heap[0]] == 0:
                        del dic[-heap[0]]
                    heappop(heap)
                if pre != heap[0]:
                    res.append([x, -heap[0]])
        return res