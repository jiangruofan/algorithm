class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        dic1, dic2 = defaultdict(list), defaultdict(list)
        count = sum(nums)
        n = len(nums) // 2
        target = sum(nums) // 2
        list1 = nums[:n]
        list2 = nums[n:]
        for i in range(1 << n):
            cnt = 0
            total1 = total2 = 0
            for j in range(n):
                if (1 << j) & i != 0:
                    cnt += 1
                    total1 += list1[j]
                    total2 += list2[j]
            dic1[cnt].append(total1)
            dic2[cnt].append(total2)
        res = float('inf')
        for i in range(n+1):
            x1 = sorted(dic1[i])
            x2 = sorted(dic2[n-i])
            l, r = 0, len(x2) - 1
            while l <len(x1) and r >= 0:
                sum1 = x1[l] + x2[r]
                res = min(res, abs(count - 2 * sum1))
                if sum1 == target:
                    return abs(count - 2 * target)
                elif sum1 < target:
                    l += 1
                else:
                    r -= 1
        return res