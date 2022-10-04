class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)
        n1 = n // 2

        def cal(list1):
            res = []
            leng = len(list1)
            for i in range(1 << leng):
                cnt = 0
                x = i
                index = 0
                while x:
                    if x & 1:
                        cnt += list1[index]
                    index += 1
                    x >>= 1
                res.append(cnt)
            return res

        list1 = cal(nums[:n1])
        list2 = cal(nums[n1:])
        list1.sort()
        list2.sort()

        ans = float('inf')
        l, r = 0, len(list2) - 1
        while l < len(list1) and r >= 0:
            if list1[l] + list2[r] == goal:
                return 0
            ans = min(ans, abs(goal - list1[l] - list2[r]))
            if list1[l] + list2[r] < goal:
                l += 1
            else:
                r -= 1
        return ans