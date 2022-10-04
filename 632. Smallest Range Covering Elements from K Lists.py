class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        res = [-float('inf'), float('inf')]
        n = len(nums)
        index = [0 for _ in range(n)]
        max1 = 0
        heap = []
        for i in range(n):
            heappush(heap, (nums[i][0], i))
            max1 = max(max1, nums[i][0])
        while True:
            if max1 - heap[0][0] < res[1] - res[0]:
                res = [heap[0][0], max1]
            num, index1 = heappop(heap)
            if index[index1] == len(nums[index1]) - 1:
                break
            index[index1] += 1
            heappush(heap, (nums[index1][index[index1]], index1))
            max1 = max(max1, nums[index1][index[index1]])
        return res

