class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        if coins[-1] == -1:
            return []
        leng = len(coins)
        deq = deque([(leng-1, coins[-1])])
        path = Counter()
        for i in range(leng-2, -1, -1):
            if deq[-1][0] - i > maxJump:
                deq.pop()
            if not deq:
                return []
            if coins[i] != -1:
                path[i] = deq[-1][0]
                while deq and deq[0][1] >= coins[i] + deq[-1][1]:
                    deq.popleft()
                deq.appendleft((i, coins[i] + (deq[-1][1] if deq else 0)))
        res = [1]
        x = 0
        while x < leng - 1:
            x = path[x]
            res.append(x+1)
        return res
