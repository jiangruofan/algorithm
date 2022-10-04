class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3

        second = nums[-n:]
        heapify(second)
        total = sum(second)
        list1 = [0 for _ in range(len(nums))]
        list1[2 * n] = total
        for i in range(2 * n - 1, n - 1, -1):
            heappush(second, nums[i])
            total -= second[0]
            heappop(second)
            total += nums[i]
            list1[i] = total

        first = [-nums[i] for i in range(n)]
        heapify(first)
        total = sum(first) * -1
        res = total - list1[n]

        for i in range(n, 2 * n):
            total += nums[i]
            heappush(first, -nums[i])
            total -= -first[0]
            heappop(first)
            res = min(res, total - list1[i + 1])
        return res