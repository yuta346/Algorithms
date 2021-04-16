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
        count_matrix = [[0]*(amount+1) for _ in coins]
        
        for i in range(len(coins)):
            for j in range(1, amount+1):
                without_this_coin = (count_matrix[i-1][j] if i>=0 else 0)
                with_this_coin = ( count_matrix[i][count_matrix[i-1][j]-coins[i]]+1  if j>=coins[i] else 0) 
                count_matrix[i][j] = min(without_this_coin , with_this_coin)

        print(count_matrix)
        return count_matrix[-1][-1]
        # if count_matrix[-1][-1] >0:
        #     return count_matrix[-1][-1]

        # else: return -1



sol = Solution()
coins = [1,2,5]
amount = 11
print(sol.coinChange(coins, amount))