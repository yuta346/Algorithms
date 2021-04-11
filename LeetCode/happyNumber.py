# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        check_loop = []
        while(n!=1):
            num_arr = [int(d)**2 for d in str(n)]
            n =  sum(num_arr)
            if(n in check_loop):
                return False
            else:
                check_loop.append(n)
        return True
           

sol = Solution()
# print(sol.isHappy(19))
print(sol.isHappy(2))
print(sol.isHappy(7))