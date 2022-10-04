# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        res = []
        leng = len(lists)
        heap = []
        for i in range(leng):
            if lists[i]:
                heappush(heap, (lists[i].val, lists[i]))
        res = ListNode(-1)
        cur = res
        while heap:
            cur.next = ListNode(heap[0][0])
            cur = cur.next
            x = heappop(heap)
            if x[1].next:
                heappush(heap, (x[1].next.val, x[1].next))
        return res.next