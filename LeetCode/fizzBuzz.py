
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        i = 1
        while i < n+1:
            if i%3 == 0 and i%5 ==0:
                result.append("FizzBuzz")
            elif i%5 == 0:
                result.append("Buzz")
            elif i%3 ==0:
                result.append("Fizz")
            else:
                result.append(str(i))
            i+=1
        return result



sol = Solution()
sol.fizzBuzz(15)