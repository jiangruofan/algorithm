class LFUCache:

    def __init__(self, capacity: int):
        self.min1 = 1
        self.dic = {}
        self.dic_fre = defaultdict(lambda: Node())
        self.capacity = capacity

    def increment(self, key):
        node = self.dic[key]
        node.l.r = node.r
        if node.r:
            node.r.l = node.l
        else:
            if node.l.val == -1:
                node.l.l = None
                if self.min1 == node.fre:
                    self.min1 += 1
            else:
                self.dic_fre[node.fre].l = node.l
        node.fre += 1
        head = self.dic_fre[node.fre]
        if not head.r:
            head.r = node
            head.l = node
            node.l = head
        else:
            node.l = head.l
            head.l.r = node
            head.l = node
        node.r = None

    def get(self, key: int) -> int:
        if key in self.dic:
            self.increment(key)
            return self.dic[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.dic:
            self.dic[key].val = value
            self.increment(key)
            return
        if len(self.dic) == self.capacity:
            head = self.dic_fre[self.min1]
            del self.dic[head.r.key]
            if not head.r.r:
                head.l = head.r = None
            else:
                head.r.r.l = head
                head.r = head.r.r

        node = Node(key, value, 1)
        self.dic[key] = node
        head = self.dic_fre[1]
        if not head.r:
            head.r = node
            head.l = node
            node.l = head
        else:
            node.l = head.l
            head.l.r = node
            head.l = node
        node.r = None
        self.min1 = 1


class Node:
    def __init__(self, key=-1, val=-1, fre=-1, l=None, r=None):
        self.key = key
        self.val = val
        self.fre = fre
        self.l = l
        self.r = r

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)