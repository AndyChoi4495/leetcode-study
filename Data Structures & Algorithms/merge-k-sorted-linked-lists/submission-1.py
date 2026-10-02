# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for li in lists:
            while li:
                heapq.heappush(minHeap, li.val)
                li = li.next
        
        dummy = cur = ListNode(0,None)

        while minHeap:
            val = heapq.heappop(minHeap)
            cur.next = ListNode(val)
            cur = cur.next
        
        return dummy.next

        