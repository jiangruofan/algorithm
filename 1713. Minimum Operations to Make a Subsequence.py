class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        dic = {}
        for i, val in enumerate(target):
            dic[val] = i

        list1 = []
        for val in arr:
            if val in dic:
                list1.append(dic[val])

        x = []
        for val in list1:
            if not x:
                x.append(val)
                continue
            index = bisect_left(x, val)
            if index == len(x):
                x.append(val)
            else:
                x[index] = val

        return len(target) - len(x)