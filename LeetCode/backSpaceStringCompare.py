class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_stack =[]
        t_stack =[]
        for i in s:
            if i=='#':
                if s_stack:
                    s_stack.pop()
                continue
            s_stack.append(i)
            
        for j in t:
            if j=='#':
                if t_stack:
                    t_stack.pop()
                continue
            t_stack.append(j)
        return s_stack == t_stack
        




sol = Solution()
# s = "ab#c"
# t = "ad#c"
# s = "a##c"
# t = "#a#c"
# s= "xywrrmp"
# t = "xywrrm#p"
s = "y#fo##f"
t = "y#f#o##f"
print(sol.backspaceCompare(s,t))