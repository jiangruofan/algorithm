class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        leng = len(requests)
        res = 0
        for i in range(1 << leng):
            list1 = [0 for _ in range(n)]
            x = i
            index = 0
            cnt = 0
            while x:
                if x & 1:
                    cnt += 1
                    request = requests[index]
                    list1[request[0]] -= 1
                    list1[request[1]] += 1
                x >>= 1
                index += 1
            judge = True
            for val in list1:
                if val != 0:
                    judge = False
                    break
            if judge:
                res = max(res, cnt)
        return res