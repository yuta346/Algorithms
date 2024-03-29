# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1]
        if n==0:
            return dp[0]
        if n==1:
            return dp[1]
        else:
            for i in range(2, n+1):
                dp.append(dp[i-1]+dp[i-2])
        return dp[-1]


#Recursive
#Time Limit Exceeded
class Solution(object):
    def climbStairs(self, n):
        if n==0:
            return 1
        if n==1:
            return 1
        return self.climbStairs(n-1)+self.climbStairs(n-2)



sol = Solution()
# print(sol.climbStairs(2))
print(sol.climbStairs(3))
print(sol.climbStairs(4))
