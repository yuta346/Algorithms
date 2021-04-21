# Write a function that reverses a string. The input string is given as an array of characters s.
# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i],s[-i-1] = s[-i-1],s[i]
        return s

sol = Solution()
s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]
print(sol.reverseString(s))