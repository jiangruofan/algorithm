class Solution:
    def isTransformable(self, s: str, t: str) -> bool:
        if Counter(s) != Counter(t):
            return False
        n = len(s)
        next1 = [float('inf') for _ in range(10)]
        for i in range(n):
            if next1[int(s[i])] == float('inf'):
                next1[int(s[i])] = i
        for i in range(n):
            val = int(t[i])
            for j in range(val):
                if next1[j] < next1[val]:
                    return False
            for j in range(next1[val] + 1, n):
                if int(s[j]) == val:
                    next1[val] = j
                    break
                if j == n - 1:
                    next1[val] = float('inf')
        return True
