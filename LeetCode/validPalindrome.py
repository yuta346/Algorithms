import re

class Solution(object):
    def isPalindrome(self, s):
        if s is " ":
           return " "
        else:
            s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]

sol = Solution()
s = "A man, a plan, a canal: Panama"
#s = "race a car"
print(sol.isPalindrome(s))