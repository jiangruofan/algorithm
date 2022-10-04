class SORTracker:

    def __init__(self):
        self.heap1 = []
        self.heap2 = []

    def add(self, name: str, score: int) -> None:
        heappush(self.heap1, minNonde(score, name))
        node = heappop(self.heap1)
        heappush(self.heap2, maxNonde(node.score, node.name))

    def get(self) -> str:
        res = self.heap2[0].name
        node = heappop(self.heap2)
        heappush(self.heap1, minNonde(node.score, node.name))
        return res


class minNonde:

    def __init__(self, score, name):
        self.score = score
        self.name = name

    def __lt__(self, other):
        if self.score == other.score:
            return self.name > other.name
        return self.score < other.score


class maxNonde:

    def __init__(self, score, name):
        self.score = score
        self.name = name

    def __lt__(self, other):
        if self.score == other.score:
            return self.name < other.name
        return self.score > other.score

# Your SORTracker object will be instantiated and called as such:
# obj = SORTracker()
# obj.add(name,score)
# param_2 = obj.get()