import random

class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        leng = len(blacklist)
        self.dic = {}
        self.end = n - leng - 1
        index = n - leng
        blacklist = set(blacklist)
        for val in blacklist:
            if val < n - leng:
                while index in blacklist:
                    index += 1
                self.dic[val] = index
                index += 1


    def pick(self) -> int:
        x = random.randint(0, self.end)
        if x not in self.dic:
            return x
        else:
            return self.dic[x]



# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()