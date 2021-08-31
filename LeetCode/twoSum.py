# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]


#Time complexity:O(n^2)
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j

#Time complexity:O(n)
    def twoSum2(self, nums, target):
        complement_dict={}
        for index,num in enumerate(nums):
            print(complement_dict)
            if num in list(complement_dict.keys()):
                return [complement_dict[num],index]
            else:
                complement_dict[target-num]=index
            


sol = Solution()
#print(sol.twoSum([3,2,4],6))
print(sol.twoSum2([3,2,4],6))
# print(sol.twoSum([3,3],6))
# print(sol.twoSum([2,5,5,11],10))
# print(sol.twoSum([1,1,3,3,3],6))