# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# The number of elements initialized in nums1 and nums2 are m and n respectively. 
# You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]

import copy
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        # del nums1[m:]
        # nums1.extend(nums2)
        # nums1.sort()
        
        temp = copy.deepcopy(nums1)
        i=j=k=0
        while m>i and n>j:
            if temp[i]<nums2[j]:
                nums1[k] = temp[i]
                i+=1
            else:
                nums1[k] = nums2[j]
                j+=1
            k+=1
        while i<m:
            nums1[k] = temp[i]
            i+=1
            k+=1
        while j<n:
            nums1[k] = nums2[j]
            j+=1
            k+=1
        return nums1


sol = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
print(sol.merge(nums1,m,nums2,n))