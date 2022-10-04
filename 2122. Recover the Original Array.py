class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        total = []
        for i in range(1, n // 2 + 1):
            if (nums[i] - nums[0]) % 2 == 0 and nums[i] != nums[0]:
                total.append(nums[i] - nums[0])
        for dif in total:
            cnt = Counter(nums)
            sum1 = n // 2
            res = []
            judge = True
            for val in nums:
                if cnt[val] == 0:
                    continue
                cnt[val] -= 1
                res.append(val + dif // 2)
                if val + dif in cnt:
                    if cnt[val + dif] == 0:
                        judge = False
                        break
                    cnt[val + dif] -= 1
                else:
                    judge = False
            if judge:
                return res


