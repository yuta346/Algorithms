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
        queue = [root]
        result = []
        while queue:
            queue_length = len(queue)
            current_level = []
            for i in range(queue_length):
                current = queue.pop()
                current_level.append(current.val)
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            result.append(current_level)
        return result