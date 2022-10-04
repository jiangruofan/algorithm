class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        if len(nums) < 7:
            return False
        prefix = [0]
        for val in nums:
            prefix.append(prefix[-1] + val)

        n = len(nums)
        for mid in range(3, n - 3):
            seen = set()
            for l in range(1, mid - 1):
                if prefix[l] - prefix[0] == prefix[mid] - prefix[l + 1]:
                    seen.add(prefix[l] - prefix[0])
            for r in range(mid + 2, n - 1):
                if prefix[r] - prefix[mid + 1] == prefix[n] - prefix[r + 1]:
                    if prefix[r] - prefix[mid + 1] in seen:
                        return True

        return False