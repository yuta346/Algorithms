# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.inorder_helper(root, [])
        
    def inorder_helper(self,root,result):
        if root is None:
            return []
        else:
            self.inorder_helper(root.left,result)
            result.append(root.val)
            self.inorder_helper(root.right,result)
        return result