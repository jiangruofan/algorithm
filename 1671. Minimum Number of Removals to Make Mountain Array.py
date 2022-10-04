class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')

        def cal(list1):
            leng = len(list1)
            x = []
            for i in range(leng - 1):
                if list1[i] >= list1[-1]:
                    continue
                if not x:
                    x.append(list1[i])
                    continue
                index = bisect_left(x, list1[i])
                if index == len(x):
                    x.append(list1[i])
                else:
                    x[index] = list1[i]
            return leng - 1 - len(x)

        for i in range(1, len(nums) - 1):
            x = cal(nums[:i + 1])
            y = cal(nums[i:][::-1])
            if x == i or y == len(nums) - i - 1 == y:
                continue
            res = min(res, x + y)
        return res