class Solution:
    # 100 150 200 250
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        mod = 10 ** 9 + 7
        set_x = set()
        set_y = set()
        for x, y, x1, y1 in rectangles:
            set_x.add(x)
            set_x.add(x1)
            set_y.add(y)
            set_y.add(y1)
        list_x = sorted(list(set_x))
        list_y = sorted(list(set_y))
        m, n = len(list_x), len(list_y)
        dic_x = {}
        dic_y = {}
        for i, val in enumerate(list_x):
            dic_x[val] = i
        for i, val in enumerate(list_y):
            dic_y[val] = i

        diff = [[0 for _ in range(n)] for _ in range(m)]
        for x, y, x1, y1 in rectangles:
            diff[dic_x[x]][dic_y[y]] += 1
            diff[dic_x[x1]][dic_y[y1]] += 1
            diff[dic_x[x]][dic_y[y1]] -= 1
            diff[dic_x[x1]][dic_y[y]] -= 1

        res = 0
        for i in range(m - 1):
            for j in range(n - 1):
                diff[i][j] += (diff[i - 1][j] if i > 0 else 0) + (diff[i][j - 1] if j > 0 else 0) - (
                    diff[i - 1][j - 1] if i > 0 and j > 0 else 0)
                if diff[i][j] > 0:
                    res += (list_x[i + 1] - list_x[i]) * (list_y[j + 1] - list_y[j]) % mod
                    res %= mod

        return res