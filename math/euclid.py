import math

#time complexity O(n^3)
def euclid(a,b):
    if b == 0:
        return a
    return euclid(b, a%b)
print(euclid(1035,759))

#extended euclid
#Input: Two positive integers a and b with a>=b>=0
#Output: Integers x,y,d such that d = gcd(a,b) and ax+by=d
def extended_euclid(a,b):
    if b==0:return (1,0,a)
    (x,y,d) = extended_euclid(b, a%b)
    return (y,x-math.floor(a/b)*y,d)
print(extended_euclid(1035,759))

#to find the multiplicative inverse, input a and b(here b is mod)
# a and mod are relatively prime
#example: 2x is congruent to 1 mod 9
#2 is a and 9 is b here so input 
#the output x is the inverse of a
print(extended_euclid(2,9)) 
print(extended_euclid(11,25)) 
print(extended_euclid(2,6)) 




