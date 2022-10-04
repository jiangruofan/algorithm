class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n - 1
        restrictions.sort()
        restrictions = [[1, 0]] + restrictions + [[n, n - 1]]
        leng = len(restrictions)
        list1 = [0 for _ in range(leng)]
        for i in range(1, leng):
            list1[i] = min(restrictions[i][1], list1[i - 1] + restrictions[i][0] - restrictions[i - 1][0])

        for i in range(leng - 2, 0, -1):
            list1[i] = min(list1[i], list1[i + 1] + restrictions[i + 1][0] - restrictions[i][0])

        res = 0
        for i in range(1, leng):
            add1 = (list1[i] - list1[i - 1] + restrictions[i][0] - restrictions[i - 1][0]) // 2
            res = max(res, list1[i - 1] + add1)

        return res