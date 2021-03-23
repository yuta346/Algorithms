class Solution(object):

    def longestCommonPrefix(self, strs):
        if len(strs)==0: return ""
        prefix = strs[0]

        for string in strs[1:]:
            while prefix != string[0:len(prefix)]:
                print("prefix",prefix)
                print("prefix[0:(prefix_len-1)]",prefix[0:len(prefix)-1])
                prefix = prefix[0:len(prefix)-1]
        return prefix
s = Solution()
arr = ["flower","flow","flight"]
arr2 = ["dog","racecar","car"]
print(s.longestCommonPrefix(arr))

