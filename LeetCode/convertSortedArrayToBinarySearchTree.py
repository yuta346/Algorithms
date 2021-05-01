#Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.bst_recursive(nums,0,len(nums)-1)
        
    def bst_recursive(self,nums,low, high):
        mid = (low+high)//2
        
        if low > high:
            return None
        
        root = TreeNode(val=nums[mid])
        root.left = self.bst_recursive(nums,low, mid-1)
        root.right = self.bst_recursive(nums,mid+1, high)
        return root