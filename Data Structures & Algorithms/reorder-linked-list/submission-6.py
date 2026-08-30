# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        ''' 
        1 2 3 4 5 6
        s s s s
          f.  f.  f
         
         '''

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next

        prev = slow.next = None
        
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        list1 = head
        list2 = prev

        while list2:
            temp1 = list1.next
            temp2 = list2.next
            list1.next = list2
            list2.next = temp1
            list1 = temp1
            list2 = temp2


        
        