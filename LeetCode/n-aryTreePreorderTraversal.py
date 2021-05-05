"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
#iterative solution
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        stack = []
        result = []
        if root is None:return 
        stack.append(root)
        while stack:
            current = stack.pop()
            result.append(current.val)
            for neighbor in reversed(current.children):
                stack.append(neighbor)
        return result