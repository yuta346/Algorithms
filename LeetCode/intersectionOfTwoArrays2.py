# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        arr = []
        i=j=0
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]==nums2[j]:
                arr.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
        return arr

sol = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
# nums1 = [3,1,2]
# nums2 = [1,1]
print(sol.intersect(nums1,nums2))