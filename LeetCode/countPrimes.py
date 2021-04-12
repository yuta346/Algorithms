# Count the number of prime numbers less than a non-negative number, n.
# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# Example 2:
# Input: n = 0
# Output: 0

# Example 3:
# Input: n = 1
# Output: 0
import random
class Solution(object):
    def countPrimes(self, n):
        nums = [True for x in range(n)]
        prime_count = 0

        for i in range(2,n):
            if nums[i]==True:
                for j in range(i*i,n,i):
                    if nums[j]==True:
                        nums[j]=False
        
        for k in range(2,n):
            if nums[k]==True:
                prime_count+=1
        return prime_count

sol = Solution()
print(sol.countPrimes(10))
