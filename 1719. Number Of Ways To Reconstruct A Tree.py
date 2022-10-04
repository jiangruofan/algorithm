class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        dic = defaultdict(list)
        for i, j in pairs:
            dic[i].append(j)
            dic[j].append(i)
        root = next((key for key, val in dic.items() if len(val) == len(dic) - 1), -1 )
        if root == -1:
            return 0
        res = 1
        for key, val in dic.items():
            if key == root:
                continue
            cur_entry = len(val)
            parent_entry = float('inf')
            parent = -1
            for i in val:
                if cur_entry <= len(dic[i]) and len(dic[i]) < parent_entry:
                    parent_entry = len(dic[i])
                    parent = i
            if parent == -1 or any(i != parent and i not in dic[parent] for i in val):
                return 0
            if cur_entry == parent_entry:
                res = 2
        return res