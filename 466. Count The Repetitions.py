class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        leng1, leng2 = len(s1), len(s2)
        index = 0
        cnt1 = 0
        cnt2 = 0
        dic = {}
        res = 0
        for num in range(leng2 + 1):
            if num == n1:
                return cnt2 // n2
            cnt1 += 1
            for i in range(leng1):
                if s1[i] == s2[index]:
                    index += 1
                if index == leng2:
                    index = 0
                    cnt2 += 1
            if index in dic:
                res += dic[index][1]
                res += (n1 - dic[index][0]) // (cnt1 - dic[index][0]) * (cnt2 - dic[index][1])
                left = (n1 - dic[index][0]) % (cnt1 - dic[index][0])
                break
            else:
                dic[index] = (cnt1, cnt2)

        for _ in range(left):
            for i in range(leng1):
                if s1[i] == s2[index]:
                    index += 1
                if index == leng2:
                    index = 0
                    res += 1

        return res // n2
