class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        right = destination[1]
        down = destination[0]
        res = ""
        factorial = [1]
        for i in range(1, right + down + 1):
            factorial.append(factorial[-1] * i)

        while right + down:
            nums = factorial[right + down - 1] // factorial[right - 1] // factorial[down]
            if nums >= k:
                res += "H"
                right -= 1
            else:
                res += "V"
                down -= 1
                k -= nums
        return res
