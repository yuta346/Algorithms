# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

from collections import Counter

class Solution1(object):
    def majorityElement(self, nums):
        count_dict = {x:0 for x in nums}
        for num in nums:
            count_dict[num]+=1
        for key in count_dict.keys():
            if count_dict[key]>len(nums)//2:
                return key

class Solution2(object):
    def majorityElement(self, nums):
        count_dict = Counter(nums)
        for key in count_dict:
            if count_dict[key] >= len(nums)//2:
                return key


nums1 = [2,2,1,1,1,2,2]
nums2 = [3,2,3]
sol = Solution1()
print(sol.majorityElement(nums1))
print(sol.majorityElement(nums2))
