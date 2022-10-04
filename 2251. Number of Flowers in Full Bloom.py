class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        diff = Counter()
        for x, y in flowers:
            diff[x] += 1
            diff[y + 1] -= 1

        list1 = sorted(diff.keys())
        for i in range(1, len(list1)):
            diff[list1[i]] += diff[list1[i - 1]]

        res = []
        for val in persons:
            index = bisect_right(list1, val)
            res.append(diff[list1[index - 1]])
        return res