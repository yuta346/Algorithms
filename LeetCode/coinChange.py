# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')for _ in range(amount+1)]
        dp[0]=0
        
        for i in range(len(dp)):
            for coin in coins:
                if i-coin>=0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return -1 if dp[-1]==float('inf') else dp[-1]

sol = Solution()
coins = [1,2,5]
amount = 11
print(sol.coinChange(coins, amount))