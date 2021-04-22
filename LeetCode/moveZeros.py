# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            return nums
        else:
            for num in nums:
                if num==0:
                    nums.remove(num)
                    nums.append(0)
                    
sol = Solution()
nums = [0,1,0,3,12]
# nums = [0,0,1]
print(sol.moveZeroes(nums))