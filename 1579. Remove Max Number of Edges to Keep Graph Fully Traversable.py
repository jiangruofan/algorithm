class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        list1 = [i for i in range(n + 1)]
        list1[0] = -1

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

        cnt = 0
        for sign, x, y in edges:
            if sign == 3:
                if find(x) != find(y):
                    union(x, y)
                    cnt += 1

        list2 = list1[::]
        for sign, x, y in edges:
            if sign == 1:
                if find(x) != find(y):
                    union(x, y)
                    cnt += 1

        if cnt != n - 1:
            return -1

        list1 = list2
        for sign, x, y in edges:
            if sign == 2:
                if find(x) != find(y):
                    union(x, y)
                    cnt += 1

        for i in range(1, len(list1)):
            if find(i) != list1[1]:
                return -1

        return len(edges) - cnt
