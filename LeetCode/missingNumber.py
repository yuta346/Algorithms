class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        for i in range(len(nums)+1):
            if i not in num_set:
                print(i)
                return i
            

sol = Solution()
sol.missingNumber([3,0,1])
sol.missingNumber([0,1])
sol.missingNumber([9,6,4,2,3,5,7,0,1])