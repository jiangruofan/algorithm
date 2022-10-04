class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        packages.sort()
        mod = 10 ** 9 + 7
        presum = [0]
        for val in packages:
            presum.append(presum[-1] + val)

        res = float('inf')
        for list1 in boxes:
            list1.sort()
            if list1[-1] < packages[-1]:
                continue
            last = 0
            total = 0
            for val in list1:
                if val < packages[last]:
                    continue
                index = bisect_right(packages, val)
                num = index - last
                total += num * val - (presum[index] - presum[last])
                last = index
                if last == len(packages):
                    break
            res = min(res, total)

        return res % mod if res != float('inf') else -1
