# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
# The digits are stored such that the most significant digit is at the head of the list, 
# and each element in the array contains a single digit.
# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

# Example 2:
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Example 3:

# Input: digits = [0]
# Output: [1]

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """ 
        for i in range(len(digits)-1,-1,-1):
            if digits[i] != 9:
                digits[i]+=1
                return digits
            else: 
                digits[i]=0
        digits.insert(0,1)
        return digits


sol = Solution()
# digits = [1,2,3]
# digits = [4,3,2,1]
# digits = [9,9,9,9]
# digits= [9,9]
digits=[1,2,9]
digits = [9,9,9]
print(sol.plusOne(digits))
        