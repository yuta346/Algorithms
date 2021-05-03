#Solution 1
class Solution(object):
    def maxProfit(self, prices):
        minVal = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]<minVal:
                minVal = prices[i]
            else:
                profit += prices[i]-minVal
                minVal = prices[i] #shift minVal
        return profit


#Solution 2
class Solution(object):
    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit+=prices[i+1]-prices[i]
        return profit

s = Solution()
prices = [7,1,5,3,6,4]
# prices = [1,2,3,4,5]
print(s.maxProfit(prices))