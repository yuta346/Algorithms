# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.symmetric_helper(root,root)

    def symmetric_helper(root1,root2):
        
        if not root1  and not root2: return None
        
        

        self.symmetric_helper(root1.left, root2.right)
        self.symmetric_helper(root1.right,root2.left)
        