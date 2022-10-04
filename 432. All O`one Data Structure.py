class AllOne:

    def __init__(self):
        self.dic = Counter()
        self.max1 = []
        self.min1 = []

    def inc(self, key: str) -> None:
        self.dic[key] += 1
        heappush(self.max1, (-self.dic[key], key))
        heappush(self.min1, (self.dic[key], key))

    def dec(self, key: str) -> None:
        self.dic[key] -= 1
        if self.dic[key] == 0:
            del self.dic[key]
            return
        heappush(self.min1, (self.dic[key], key))
        heappush(self.max1, (-self.dic[key], key))


    def getMaxKey(self) -> str:
        while self.max1 and self.dic[self.max1[0][1]] != -self.max1[0][0]:
            heappop(self.max1)
        return self.max1[0][1] if self.max1 else ""


    def getMinKey(self) -> str:
        while self.min1 and self.dic[self.min1[0][1]] != self.min1[0][0]:
            heappop(self.min1)
        return self.min1[0][1] if self.min1 else ""