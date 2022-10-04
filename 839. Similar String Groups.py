class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        list1 = [i for i in range(n)]

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

        def check(s1, s2):
            s11 = s1
            s22 = s2
            s1 = list(s1)
            s2 = list(s2)
            if len(s1) != len(s2):
                return False

            preindex = -1
            for i in range(len(s1)):
                if s1[i] == s2[i]:
                    continue
                if preindex != -1:
                    return s1[preindex] == s2[i] and s2[preindex] == s1[i] and s11[i + 1:] == s22[i + 1:]
                preindex = i
            return True

        for i in range(n):
            for j in range(i + 1, n):
                if find(i) == find(j):
                    continue
                if check(strs[i], strs[j]):
                    union(i, j)

        for i in range(n):
            list1[i] = find(i)

        return len(set(list1))