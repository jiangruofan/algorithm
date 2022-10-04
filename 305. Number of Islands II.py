class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        list1 = [-1 for i in range(m * n)]
        res = 0
        ans = []

        def find(x):
            if list1[x] == x:
                return x
            list1[x] = find(list1[x])
            return list1[x]

        def union(x, y):
            fa1 = find(x)
            fa2 = find(y)
            if fa1 != fa2:
                list1[fa1] = fa2

        for x, y in positions:
            pos = x * n + y
            if list1[pos] != -1:
                ans.append(res)
                continue
            surround = {}
            for i, j in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                pos1 = i * n + j
                if i < 0 or i == m or j < 0 or j == n or list1[pos1] == -1:
                    continue
                if find(pos1) not in surround:
                    surround[list1[pos1]] = pos1
            list1[pos] = pos
            if surround:
                for key, val in surround.items():
                    union(val, pos)

                res -= len(surround) - 1
            else:
                res += 1
            ans.append(res)
        return ans
