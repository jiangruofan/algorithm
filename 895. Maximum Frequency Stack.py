class FreqStack:

    def __init__(self):
        self.dic = Counter()
        self.dic1 = defaultdict(list)
        self.maxfre = -1


    def push(self, val: int) -> None:
        self.dic[val] += 1
        self.dic1[self.dic[val]].append(val)
        if self.dic[val] > self.maxfre:
            self.maxfre = self.dic[val]


    def pop(self) -> int:
        res = self.dic1[self.maxfre].pop()
        self.dic[res] -= 1
        if not self.dic1[self.maxfre]:
            self.maxfre -= 1
        return res
