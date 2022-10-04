class Solution:
    def minInteger(self, num: str, k: int) -> str:
        n = len(num)
        next1 = [-1 for _ in range(10)]
        offset = [0 for _ in range(10)]
        rearranged = [False for _ in range(n)]

        for i, s in enumerate(num):
            if next1[int(s)] == -1:
                next1[int(s)] = i

        res = ""
        for i in range(n):
            r = -1
            val = -1
            for j in range(10):
                if next1[j] == -1:
                    continue
                if next1[j] - i + offset[j] <= k:
                    r = next1[j]
                    val = j
                    k -= next1[j] - i + offset[j]
                    res += str(j)
                    break

            if r == -1:
                break

            for j in range(10):
                if next1[j] < r:
                    offset[j] += 1

            for j in range(r + 1, n + 1):
                if j == n:
                    next1[val] = -1
                    continue

                if rearranged[j]:
                    offset[val] -= 1

                if num[j] == str(val):
                    next1[val] = j
                    break

            rearranged[r] = True

        for i in range(n):
            if not rearranged[i]:
                res += num[i]

        return res
