# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {x:0 for x in s}
        t_dict = {y:0 for y in t}
        for char in s:
            s_dict[char]+=1
        for char in t:
            t_dict[char]+=1
        if s_dict == t_dict:
            return True
        return False

sol  = Solution()
print(sol.isAnagram(s = "anagram", t = "nagaram"))
print(sol.isAnagram(s = "rat", t = "car"))
