class Solution1(object):
    def strStr(self, haystack, needle):
        if len(needle)==0:
            return 0
        if needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)-len(needle)+1):
                flag=True
                for j in range(len(needle)):
                    if haystack[i+j]!=needle[j]:
                        flag=False
                        break
                if flag:
                    return i
                
class Solution2(object):
    def strStr(self, haystack, needle):
        if len(needle)==0:
            return 0
        if needle not in haystack:
            return -1
        return haystack.index(needle)


                         
s = Solution1()
haystack = "mississippi"
needle = "issip"
print(s.strStr(haystack,needle))