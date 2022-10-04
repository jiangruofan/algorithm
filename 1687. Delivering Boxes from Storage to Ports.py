class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        begin = 0
        weight = boxes[0][1]
        index = 0
        numsPort = 1
        leng = len(boxes)
        dp = [float('inf') for _ in range(leng)]
        dp[0] = 2
        for i in range(1, leng):
            if boxes[i][0] != boxes[i-1][0]:
                numsPort += 1
            weight += boxes[i][1]
            while i - begin + 1 > maxBoxes or weight > maxWeight:
                weight -= boxes[begin][1]
                if boxes[begin+1][0] != boxes[begin][0]:
                    numsPort -= 1
                begin += 1
            while index <= begin or (index < leng and boxes[index][0] == boxes[index-1][0]):
                index += 1
            x = dp[begin-1] if begin > 0 else 0
            y = dp[index-1] if index > 0 else 0
            dp[i] = min(x + numsPort + 1, y + numsPort if index <= i else float('inf'))
        return dp[-1]

