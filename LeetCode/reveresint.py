# Assume we are dealing with an environment which could only store 
# integers within the 32-bit signed integer 
# range: [−2**31,  2**31 − 1]. For the purpose of this problem, 
# assume that your function returns 0 when the reversed integer overflows.


#Solution1
class Solution1(object):
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
rev = Solution1()
print(rev.reverse(-120))

#Solution2
class Solution2(object):
    def reverse(self, x):
        if x >= 2**31-1 or x <= -2**31: return 0
        else:
            list_x = list(str(x))
            if  x>0:
                list_x = list_x[::-1]
                list_x_int = int("".join(list_x))
            else:
                sign = list_x.pop(0)
                list_x = list_x[::-1]
                list_x.insert(0,sign)
                list_x_int = int("".join(list_x))
            if list_x_int >=(2**31)-1 or list_x_int <=(-2**31):
                return 0
            else: return list_x_int
            
            
sol = Solution2()
print(sol.reverse(-123))
print(sol.reverse(123))
print(sol.reverse(-1534236469))
