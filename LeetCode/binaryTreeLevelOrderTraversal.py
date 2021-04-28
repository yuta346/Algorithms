# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """ 
        if root is None:
            return 
        quque = []
        quque.append(root)
        while queue:
            current = queue.pop()
            print(current.val)
            if current.left is not None:
                queue.push(current.left)
            if current.right is not None:
                queue.push(current.right)
            queue.pop()