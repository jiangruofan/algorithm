class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        l, r = 0, m * 5000

        def check(target): # <= target
            res = 1
            sum1 = 0
            for i in range(m):
                sum1 += mat[i][0]
            if sum1 > target:
                return False
            def dfs(index, total):
                nonlocal res
                if res >= k:
                    return
                if index == m:
                    return
                for i in range(n):
                    if total + mat[index][i] - mat[index][0] > target:
                        break
                    if i > 0:
                        res += 1
                    dfs(index+1, total + mat[index][i] -mat[index][0])
            dfs(0, sum1)
            return res >= k

        while l < r:
            mid = (l + r) // 2
            if check(mid): # return >= k
                r = mid
            else: # return < k
                l = mid + 1
        return l