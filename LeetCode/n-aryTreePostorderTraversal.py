"""
# Definition for a Node.
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return root
        result = []
        stack = [root]
        while stack:
            current = stack.pop()
            result.insert(0,current.val)
            for neighbor in current.children:
                stack.append(neighbor)
        return result