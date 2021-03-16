# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.

# class Solution(object):
#     def romanToInt(self, s):
#         keys = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
#         prev = keys[s[0]]
#         total = prev 

#         for i in range(1, len(s)):
#             if keys[s[i]] > prev:
#                 total = total - (2*prev) + keys[s[i]]
#             else:
#                 total+= keys[s[i]] 
#             prev =keys[s[i]]
#         return total

# s = Solution()
# print(s.romanToInt("MCMXCIV"))



# class Solution(object):
#     def removeDuplicates(self, nums):
#         pointer1 = 0
#         for i in range(1, len(nums)):
#             if nums[pointer1] != nums[i]:
#                 pointer1+=1
#                 nums[pointer1]=nums[i]
#         return pointer1+1
            
            
# s = Solution()
# print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


# class Solution(object):
#     def removeElement(self, nums, val):

#         p1 = 0
#         for i in range(0, len(nums)):
#             if nums[i] != val:
#                 nums[p1]=nums[i]
#                 p1+=1
#         return p1
# s = Solution()
# print(s.removeElement([0,1,2,2,3,0,4,2], 2))


class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(0, len(nums)):
            if nums[i]>=target:
                return i
        return i+1
                
                

c = Solution()
print(c.searchInsert([1,3,5,6], 7))