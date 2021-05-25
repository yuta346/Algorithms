# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        path  = ""
        result = []

        def dfs(result,root,path):
            if root is None:
                return 
            path += str(root.val)
            print(path)
            dfs(result, root.left, path+"->")
            dfs(result, root.right, path+"->")
            if root.left is None and root.right is None:
                result.append(path)

        dfs(result, root, path)
        print(result)




tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.right = TreeNode(5)
sol = Solution()
sol.binaryTreePaths(tree)
