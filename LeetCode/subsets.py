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
        result = [[]]
        for num in nums:
            for i in range(len(result)):
                print(i)
                result.append([num] + result[i])
        print(result)
        return result

sol = Solution()
# nums = [1,2,3]
# nums = [1,2]
nums = [3,2,4,1]
sol.subsets(nums)