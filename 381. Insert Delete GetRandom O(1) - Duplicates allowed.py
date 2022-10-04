class RandomizedCollection:

    def __init__(self):
        self.dic = defaultdict(set)
        self.nums = []


    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.dic[val].add(len(self.nums)-1)
        return True if len(self.dic[val]) == 1 else False


    def remove(self, val: int) -> bool:
        if not self.dic[val]:
            return False
        if self.nums[-1] == val:
            self.dic[val].remove(len(self.nums)-1)
            self.nums.pop()
            return True
        x = self.dic[val].pop()
        end = self.nums[-1]
        self.dic[end].remove(len(self.nums)-1)
        self.dic[end].add(x)
        self.nums.pop()
        self.nums[x] = end
        return True


    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()