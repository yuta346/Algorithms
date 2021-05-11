# Given two strings s and t, check if s is a subsequence of t.

# A subsequence of a string is a new string that is formed from the original string 
# by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false


class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==0:
            return True
        p1 = 0
        p2 = 0
        while p1<len(s) and p2<len(t):
            if s[p1]==t[p2]:
                p1+=1
                p2+=1
            else: p2+=1
        if p1==len(s):
            return True
        return False
            
            
            