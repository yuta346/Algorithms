# Assume we are dealing with an environment which could only store 
# integers within the 32-bit signed integer 
# range: [−2**31,  2**31 − 1]. For the purpose of this problem, 
# assume that your function returns 0 when the reversed integer overflows.



class Solution(object):
    def reverse(self, x):
        if x < -2**31 or x > 2**31-1: return 0
        else:
            strx = str(x)
            if x >0:
                revst =  strx[::-1]
            else:
                temp = strx[1:] 
                print(temp)
                temp2 = temp[::-1] 
                print(temp2)
                revst = "-" + temp2
        
            if int(revst) <-2**31 or int(revst) > 2**31-1: return 0
            else: return int(revst)



rev = Solution()
print(rev.reverse(-120))


























# class Solution(object):
#     def reverse(self, x):
#        if x >= 2**31-1 or x <= -2**31: return 0
#        else:
#             strg = str(x)
#             if x >= 0 :
#                 revst = strg[::-1]
#             else:
#                 temp = strg[1:] 
#                 temp2 = temp[::-1] 
#                 revst = "-" + temp2
#             if int(revst) >= 2**31-1 or int(revst) <= -2**31: return 0
#             else: return int(revst) 
        

# rev = Solution()
# print(rev.reverse(123456))
        