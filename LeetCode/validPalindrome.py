import re

class Solution(object):
    def isPalindrome(self, s):
        if s is " ":
           return " "
        else:
            s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if s == s[::-1]:
            return True
        return False

sol = Solution()
s = "A man, a plan, a canal: Panama"
s = "race a car"
#s = " "
print(sol.isPalindrome(s))