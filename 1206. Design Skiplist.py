import random


class Skiplist:

    def __init__(self):
        self.node = Node()

    def search(self, target: int) -> bool:
        cur = self.node
        while cur:
            while cur.right and cur.right.val <= target:
                cur = cur.right
            if cur.val == target:
                return True
            cur = cur.down
        return False

    def add(self, num: int) -> None:
        list1 = []
        cur = self.node
        while cur:
            while cur.right and cur.right.val < num:
                cur = cur.right
            list1.append(cur)
            cur = cur.down
        judge = 1
        down = None
        while judge and list1:
            x = list1.pop()
            x.right = Node(num, x.right, down)
            down = x.right
            judge = random.randint(0, 1)
        if not list1:
            self.node = Node(down=self.node)

    def erase(self, num: int) -> bool:
        judge = False
        cur = self.node
        while cur:
            while cur.right and cur.right.val < num:
                cur = cur.right
            if cur.right and cur.right.val == num:
                judge = True
                cur.right = cur.right.right
            cur = cur.down
        return judge


class Node:

    def __init__(self, val=-1, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)