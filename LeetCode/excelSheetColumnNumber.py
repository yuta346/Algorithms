# Given a string columnTitle that represents the column title as appear in an Excel sheet, 
# return its corresponding column number.

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        result = 0
        factor = 1
        for char in columnTitle[::-1]:
            result+=(ord(char)-ord('A')+1)*factor #26^0, 26^1, 26^2...
            factor*=26
        return result


sol = Solution()
columnTitle = "FXSHRXW"
columnTitle = "AA"
print(sol.titleToNumber(columnTitle))
