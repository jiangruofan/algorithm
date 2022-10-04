class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        list1 = []
        for i, val in enumerate(nums):
            if val:
                list1.append(i)

        if k % 2 == 0:
            # 1 2 3 4
            # 1 0 1 2
            constant = (1 + k // 2) * (k // 2) - k // 2
        else:
            # 1 2 3
            # 1 0 1
            constant = (1 + k // 2) * (k // 2)

        res = 0
        mid = k // 2
        for i in range(k):
            res += abs(list1[i] - list1[mid])
        sum1 = res
        for i in range(k, len(list1)):
            sum1 -= abs(list1[i - k] - list1[mid])
            sum1 += abs(list1[i] - list1[mid + 1])
            sum1 += k // 2 * abs(list1[mid + 1] - list1[mid])
            sum1 -= (k - 1) // 2 * abs(list1[mid + 1] - list1[mid])
            mid += 1
            res = min(res, sum1)

        return res - constant


'''
odd:
x x o x x
  x x o x x
even:
x x o x
  x x o x
'''
