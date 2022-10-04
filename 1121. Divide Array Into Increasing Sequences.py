class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], k: int) -> bool:
        cnt = Counter(nums)
        n = cnt.most_common(1)[0][1]
        return len(nums) >= k * n