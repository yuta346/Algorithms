# Given an integer array nums of unique elements, return all possible subsets (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

# Example 1:

# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Example 2:

# Input: nums = [0]
# Output: [[],[0]]



class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List
        [List[int]]
        """
        result = [[], nums]
        for i in range(len(nums)):
            if [nums[i]] not in result:
                result.append([nums[i]])
            for j in range(len(nums)):
                if [nums[j]] not in result and i !=j and [nums[i],nums[j]] not in result: 
                    result.append([nums[i],nums[j]])
        print(result)
        return result

sol = Solution()
nums = [1,2,3]
# nums = [1,2]
nums = [3,2,4,1]
sol.subsets(nums)