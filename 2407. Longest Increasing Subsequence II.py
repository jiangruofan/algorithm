class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        tree = Counter()
        x = max(nums)

        def update(begin, end, index, num, node):
            tree[node] = max(tree[node], num)
            mid = (begin + end) // 2
            if begin == end:
                return
            if index <= mid:
                update(begin, mid, index, num, node * 2)
            else:
                update(mid + 1, end, index, num, node * 2 + 1)

        def query(begin, end, l, r, node):
            if begin == l and end == r:
                return tree[node]

            mid = (begin + end) // 2
            if r <= mid:
                return query(begin, mid, l, r, node * 2)
            elif l > mid:
                return query(mid + 1, end, l, r, node * 2 + 1)
            else:
                return max(query(begin, mid, l, mid, node * 2), query(mid + 1, end, mid + 1, r, node * 2 + 1))

        for val in nums:
            l, r = max(0, val - k), val - 1
            max1 = query(0, x, l, r, 1)
            update(0, x, val, max1 + 1, 1)

        return tree[1]


