class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        heapl = []
        heapr = []
        dicl = Counter()
        dicr = Counter()
        left = right = 0
        res = []
        def adjust():
            nonlocal left, right
            sign = 1 if k % 2 == 1 else 0
            while len(heapl) - left < len(heapr) - right + sign:
                x = heappop(heapr)
                if x in dicr:
                    dicr[x] -= 1
                    if dicr[x] == 0:
                        del dicr[x]
                    right -= 1
                else:
                    heappush(heapl, -x)
            while len(heapl) - left > len(heapr) - right + sign :
                x = -heappop(heapl)
                if x in dicl:
                    dicl[x] -= 1
                    if dicl[x] == 0:
                        del dicl[x]
                    left -= 1
                else:
                    heappush(heapr, x)
            while heapl and -heapl[0] in dicl:
                x = -heappop(heapl)
                dicl[x] -= 1
                if dicl[x] == 0:
                    del dicl[x]
                left -= 1
            while heapr and heapr[0] in dicr:
                x = heappop(heapr)
                dicr[x] -= 1
                if dicr[x] == 0:
                    del dicr[x]
                right -= 1

        for i, val in enumerate(nums):
            if heapr and heapr[0] <= val:
                heappush(heapr, val)
            else:
                heappush(heapl, -val)
            adjust()
            if i >= k-1:
                res.append(-heapl[0] if k % 2 == 1 else (-heapl[0] + heapr[0]) / 2)
                if nums[i-k+1] <= -heapl[0]:
                    dicl[nums[i-k+1]] += 1
                    left += 1
                else:
                    dicr[nums[i-k+1]] += 1
                    right += 1
        return res

