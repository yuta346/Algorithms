# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_dict = {x:0 for x in nums}
        for num in nums:
            count_dict[num]+=1
        for value in count_dict.values():
            if value >=2:
                return True
        return False



sol = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
# nums = [1,2,3,4]
print(sol.containsDuplicate(nums))
        