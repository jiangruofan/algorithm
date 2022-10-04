class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        leng = len(arr)
        odd, even = [-1] * leng, [-1] * leng
        list1 = sorted(range(leng) ,key = lambda x : arr[x])
        stack = []
        for i in list1:
            while stack and i > stack[-1]:
                x = stack.pop()
                odd[x] = i
            stack.append(i)
        stack = []
        list1.sort(key = lambda x : -arr[x])
        for i in list1:
            while stack and i > stack[-1]:
                x = stack.pop()
                even[x] = i
            stack.append(i)
        res = 1
        dp = [[False] * 2 for _ in range(leng)]
        dp[-1][0] = dp[-1][1] = True
        for i in range(leng-2, -1, -1):
            dp[i][0] = dp[odd[i]][1] if odd[i] != -1 else False
            dp[i][1] = dp[even[i]][0] if even[i] != -1 else False
            res += 1 if dp[i][0] else 0
        return res