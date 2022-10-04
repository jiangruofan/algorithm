class Solution:
    def smallestMissingValueSubtree(self, parents: List[int], nums: List[int]) -> List[int]:
        leng = len(parents)
        res = [1 for _ in range(leng)]
        one = -1
        for i in range(leng):
            if nums[i] == 1:
                one = i
                break
        if one == -1:
            return res

        dic = defaultdict(list)
        for i in range(1, leng):
            dic[parents[i]].append(i)

        visited = Counter()

        def cal(node):
            visited[nums[node]] = 1
            for child in dic[node]:
                if visited[nums[child]]:
                    continue
                cal(child)

        index = 2
        while one != -1:
            cal(one)
            while visited[index]:
                index += 1
            res[one] = index
            one = parents[one]
        return res