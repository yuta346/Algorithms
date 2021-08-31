# Given two non-negative integers, num1 and num2 represented as string, 
# return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for 
# handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.


class Solution(object):
    def addStrings(self, num1, num2):
        result = []
        p1 = len(num1)-1
        p2 = len(num2)-1
        carry = 0

        while p1 >= 0 or p2 >= 0:
            sum = carry
            if p1>=0 :
                sum += int(num1[p1])
            if p2>=0 :
                sum += int(num2[p2])
            result.append(str(sum%10))
            carry = sum//10
            p1-=1
            p2-=1
        if carry > 0 :
            print(carry)
            result.append(str(carry))
        
        print(result)
        result.reverse()
        return ''.join(result)

sol = Solution()
print(sol.addStrings("456", "777"))
# sol.addStrings("101", "9")