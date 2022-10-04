class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def get(m, nums):
            k = len(nums) - m
            stack = []
            for i in range(len(nums)):
                while stack and stack[-1] < nums[i] and k > 0:
                    stack.pop()
                    k -= 1
                stack.append(nums[i])
            return stack[:-k] if k > 0 else stack
        def merge(list1, list2):
            list1 = deque(list1)
            list2 = deque(list2)
            ans = []
            while list1 or list2:
                x = list1 if list1 > list2 else list2
                ans.append(x.popleft())
            return ans
        res = []
        for i in range(k+1):
            if i <= len(nums1) and k - i <= len(nums2):
                res = max(res, merge(get(i, nums1), get(k-i, nums2)))
        return res
