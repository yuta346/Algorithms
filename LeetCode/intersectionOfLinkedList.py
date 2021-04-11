# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if(headA is None or headB is None):
            return "No intersection"
        pointerA = headA
        pointerB = headB
        while(pointerA is not pointerB):
            pointerA = pointerA.next
            pointerB = pointerB.next
            if(pointerA is pointerB):
                return pointerA
            if(pointerA is None):
                pointerA = headB
            elif(pointerB is None):
                pointerB = headA
        return pointerA
