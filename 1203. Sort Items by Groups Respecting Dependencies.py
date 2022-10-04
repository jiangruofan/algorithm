class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        dic = defaultdict(list)

        cnt = m
        for i, val in enumerate(group):
            if val == -1:
                group[i] = cnt
                cnt += 1

        for i in range(len(group)):
            dic[group[i]].append(i)

        dic1 = defaultdict(list)
        entry = Counter()
        for i, list1 in enumerate(beforeItems):
            for val in list1:
                if group[val] == group[i]:
                    dic1[val].append(i)
                    entry[i] += 1

        def cal(list1, dic, entry):
            deq = deque([val for val in list1 if entry[val] == 0])
            res = []
            while deq:
                x = deq.popleft()
                res.append(x)
                for val in dic[x]:
                    entry[val] -= 1
                    if entry[val] == 0:
                        deq.append(val)
            return res

        dic2 = defaultdict(list)
        for key, list1 in dic.items():
            dic2[key] = cal(list1, dic1, entry)
            if len(dic2[key]) != len(list1):
                return []

        dic3 = defaultdict(set)
        entry = Counter()
        for i, list1 in enumerate(beforeItems):
            for val in list1:
                if group[val] != group[i] and group[i] not in dic3[group[val]]:
                    dic3[group[val]].add(group[i])
                    entry[group[i]] += 1

        group1 = cal(dic.keys(), dic3, entry)
        if len(group1) != len(dic):
            return []

        ans = []
        for val in group1:
            ans += dic2[val]
        return ans