class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        res = 0
        root = node()
        root.add(nums[0])

        def cal(num, limit):
            total = 0
            list1 = []
            while limit:
                list1.append(1 if limit & 1 else 0)
                limit >>= 1
            list1 = list1[::-1]
            list2 = []
            while num:
                list2.append(1 if num & 1 else 0)
                num >>= 1
            list2 = list2[::-1]
            m, n = len(list1), len(list2)
            list1 = [0 for _ in range(32 - m)] + list1
            list2 = [0 for _ in range(32 - n)] + list2

            cur = root
            for i in range(len(list1)):
                if not cur:
                    break
                if list1[i] == 0:
                    cur = cur.children[1] if list2[i] == 1 else cur.children[0]
                else:
                    total += cur.children[0 if list2[i] == 0 else 1].cnt
                    cur = cur.children[0 if list2[i] == 1 else 1]
            return total

        for i in range(1, len(nums)):
            res += cal(nums[i], high + 1) - cal(nums[i], low)
            root.add(nums[i])
        return res


class node:
    def __init__(self):
        self.children = defaultdict(node)
        self.cnt = 0

    def add(self, num):
        list1 = []
        while num:
            list1.append(1 if num & 1 else 0)
            num >>= 1
        list1 = list1[::-1]
        leng = len(list1)
        list1 = [0 for _ in range(32 - leng)] + list1
        cur = self
        for i in range(len(list1)):
            cur.cnt += 1
            cur = cur.children[0] if list1[i] == 0 else cur.children[1]
        cur.cnt += 1