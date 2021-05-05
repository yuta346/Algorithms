# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        curr = head
        dummy = ListNode(-1)
        dummy.next = curr
        first = dummy
        while curr:
            if curr.val == val:
                dummy.next = curr.next
            else:
                dummy = dummy.next
            curr = curr.next
        return first.next
        
        
        