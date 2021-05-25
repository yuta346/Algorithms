
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.



class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums_dict = {}
        # for i in nums:
        #     nums_dict[i] = nums_dict.get(i,0)+1
        #     if nums_dict[i] > 1:
        #         return i
        
        # nums_list = [0]*len(nums)
        # for i in nums:
        #     nums_list[i]+=1
        #     if nums_list[i] > 1:
        #         return i
    
        nums_set = set()
        for i in nums:
            if i in nums_set:
                return i
            nums_set.add(i)
            










sol = Solution()
print(sol.findDuplicate([1,3,4,2,2]))