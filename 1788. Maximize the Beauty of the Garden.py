class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        presum = [0]
        for val in flowers:
            presum.append(presum[-1] + val if val > 0 else presum[-1])

        dic = defaultdict(list)
        for i, val in enumerate(flowers):
            if len(dic[val]) < 2:
                dic[val].append(i)
            else:
                dic[val][1] = i

        res = -float('inf')
        for val, list1 in dic.items():
            if len(list1) == 1:
                continue
            res = max(res, 2 * val + presum[list1[1]] - presum[list1[0] + 1])

        return res
