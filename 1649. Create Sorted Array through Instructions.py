class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        mod = 10 ** 9 + 7
        dic = {}
        index = 1
        x = sorted(instructions)
        for i, val in enumerate(x):
            if i > 0 and val == x[i - 1]:
                continue
            dic[val] = index
            index += 1

        bit = [0 for _ in range(index)]

        def update(loc, val):
            while loc < index:
                bit[loc] += val
                loc += loc & (-loc)

        def query(loc):
            ret = 0
            while loc > 0:
                ret += bit[loc]
                loc -= loc & (-loc)
            return ret

        res = 0
        for val in instructions:
            res += min(query(dic[val] - 1), query(index - 1) - query(dic[val]))
            res %= mod
            update(dic[val], 1)
        return res