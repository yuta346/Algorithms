class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        test_num=0
        while(n>0):
            remainder = n % 10
            test_num = (test_num * 10) + remainder
            n = n//10   
sol = Solution()
sol.reverseBits(123)