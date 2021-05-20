# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        list_node = self.preOrder(root)
        result =  list_node.count(list_node[0]) == len(list_node)
        return result
        
    def preOrder(self, root):
        if root is None:
            return []
        else:
            return [root.val] + self.preOrder(root.left) + self.preOrder(root.right)
        