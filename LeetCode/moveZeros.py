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
       
        # for num in nums:
        #     if num==0:
        #         nums.remove(num)
        #         nums.append(0)

        pointer = 0
        count_zeros = 0
        for n in nums:
            if n!=0:
                nums[pointer] = n
                pointer+=1
            else: count_zeros+=1
        for i in range(1,count_zeros+1):
           nums[-i] = 0
        return nums
sol = Solution()
nums = [0,1,0,3,12]
# nums = [0,0,1]
print(sol.moveZeroes(nums))