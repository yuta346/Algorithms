class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return i,j

sol = Solution()
print(sol.twoSum([3,2,4],6))
print(sol.twoSum([3,3],6))
print(sol.twoSum([2,5,5,11],10))
print(sol.twoSum([1,1,3,3,3],6))