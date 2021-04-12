# Given a string s, return the first non-repeating character in it and return its index. 
# If it does not exist, return -1.
# Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:

# Input: s = "loveleetcode"
# Output: 2
# Example 3:

# Input: s = "aabb"
# Output: -1

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = list(s)
        char_dict  = {char:0 for char in s}
        for char in s:
            char_dict[char]+=1
        
        for char in s:
            if char_dict[char]==1:
                return s.index(char)
        return -1

sol = Solution()
s = "leetcode"
s = "loveleetcode"
s = "aabb"
print(sol.firstUniqChar(s))