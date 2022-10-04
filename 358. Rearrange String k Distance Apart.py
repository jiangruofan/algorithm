class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k == 0:
            return s
        cnt = Counter(s)
        res = ""
        heap = []
        for key, val in cnt.items():
            heappush(heap, (-val, key))
        while heap:
            if len(heap) < k and -heap[0][0] > 1:
                return ""
            leng = min(len(heap), k)
            save = []
            for _ in range(leng):
                num, val = heappop(heap)
                res += val
                num += 1
                if num != 0:
                    save.append((num, val))
            while save:
                heappush(heap, save.pop())
        return res
