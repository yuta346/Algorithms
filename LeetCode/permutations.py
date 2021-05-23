# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.
# Example 1:

# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Example 2:

# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
# Example 3:

# Input: nums = [1]
# Output: [[1]]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print(nums)
        result = []
        if len(nums) == 1:
            print('nums',nums)
            return [nums[:]]

        for i in range(len(nums)):
            print('first for loop',nums)
            n = nums.pop(0)
            print('n: ',n)
            perms = self.permute(nums)
            
            print('before 2nd for loop', perms)
            for perm in perms:
                print('second for loop perm',perm)
                perm.append(n)
                print('perm after append',perm)
            result.extend(perms)
            print('result',result)
            nums.append(n)
            print('end',nums)
        return result

nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))