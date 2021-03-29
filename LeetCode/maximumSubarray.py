class Solution(object):
    def maxSubArray(self, nums):
        if len(nums)==1:
            return nums[0]
        currentValue = nums[0]
        globalValue = nums[0]
        for i in range(1, len(nums)):
            currentValue = max(nums[i]+currentValue, nums[i])
            if currentValue>globalValue:
                globalValue = currentValue
        return globalValue       
                


s = Solution()
#nums = [5,4,-1,7,8]
nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums=[-2,1]
print(s.maxSubArray(nums))