class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        m, n = len(image), len(image[0])
        def get(l, r, x, sign):
            while l < r:
                mid = (l + r) // 2
                judge = False
                for i in range(x):
                    if sign and image[i][mid] == '1':
                        judge = True
                        break
                    if not sign and image[mid][i] == '1':
                        judge = True
                        break
                if judge:
                    r = mid
                else:
                    l = mid + 1
            return l

        def get2(l, r, x, sign):
            while l < r:
                mid = (l + r) // 2 + 1
                judge = False
                for i in range(x):
                    if sign and image[i][mid] == '1':
                        judge = True
                        break
                    if not sign and image[mid][i] == '1':
                        judge = True
                        break
                if judge:
                    l = mid
                else:
                    r = mid - 1
            return l
        left = get(0, y, m, True)
        right = get2(y, n-1, m, True)
        top = get(0, x, n, False)
        bottom = get2(x, m - 1, n, False)
        return (right - left + 1) * (bottom - top + 1)