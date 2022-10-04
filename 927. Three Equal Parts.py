class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        cnt = Counter(arr)
        if cnt[1] % 3 != 0:
            return [-1, -1]

        if cnt[1] == 0:
            return [0, len(arr) - 1]

        total = cnt[1] // 3
        index = len(arr)
        while total:
            index -= 1
            if arr[index] == 1:
                total -= 1

        res = []
        begin = 0
        while arr[begin] == 0:
            begin += 1

        r = index
        while r < len(arr) and arr[begin] == arr[r]:
            begin += 1
            r += 1

        if r != len(arr):
            return [-1, -1]

        res.append(begin - 1)

        while arr[begin] == 0:
            begin += 1

        r = index
        while r < len(arr) and arr[begin] == arr[r]:
            begin += 1
            r += 1

        if r != len(arr):
            return [-1, -1]

        res.append(begin)
        return res