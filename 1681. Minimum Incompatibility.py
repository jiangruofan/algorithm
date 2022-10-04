class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = Counter(nums)
        if max(cnt.values()) > k:
            return -1
        leng = len(nums)

        res = float('inf')
        seen = [0 for _ in range(leng)]
        seen[0] = 1

        def dfs(cur, total, max1, min1, addedincompatibility):
            nonlocal res
            if addedincompatibility > res:
                return
            if total == leng // k:
                index = 0
                while index < leng and seen[index]:
                    index += 1
                if index == leng:
                    res = min(res, addedincompatibility + max1 - min1)
                else:
                    seen[index] = 1
                    dfs(index, 1, nums[index], nums[index], addedincompatibility + max1 - min1)
                    seen[index] = 0
            else:
                for i in range(cur + 1, leng):
                    if seen[i]:
                        continue
                    if nums[i] == nums[cur]:
                        continue
                    if nums[i] == nums[i - 1] and not seen[i - 1]:
                        continue
                    seen[i] = 1
                    dfs(i, total + 1, nums[i], min1, addedincompatibility)
                    seen[i] = 0

        dfs(0, 1, nums[0], nums[0], 0)
        return res