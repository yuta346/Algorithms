class Solution(object):
     def maxProfit(self, prices):
        min = prices[0]
        maxVal = 0
        for i in range(len(prices)):
            if prices[i]<min:
                min = prices[i]
            else:
                maxVal = max(maxVal, prices[i]-min)
        return maxVal


s = Solution()
#prices = [7,1,5,3,6,4]
#prices = [7,6,4,3,1]
prices = [1,3,7,6,4,3,99,100]
print(s.maxProfit(prices))