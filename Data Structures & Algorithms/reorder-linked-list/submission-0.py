# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # first node of second list
        second = slow.next # because slow is the last node of the first list
        
        # split two lists by making the first list end is none
        prev = slow.next = None
        
        # reversing the second list
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next

        # because after reversing the list second is none
        second = prev 
        first = head

        # reording the list
        while second:
            temp1 , temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            second = temp2
            first = temp1
            
