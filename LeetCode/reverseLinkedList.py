# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        return self.reverse(head, None)
    
    def reverse(self, head, newHead):
        if head is None:
            return newHead
        
        next = head.next
        head.next = newHead
        newHead = head
        head = next

        return self.reverse(head, newHead)
    
