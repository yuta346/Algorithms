#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.
#An input string is valid if:
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.

class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i in ['(','[','{']:
                stack.append(i)
            else:
                #check if stack is empty
                if not stack:
                    return False
                #pop the top element in the stack
                stack_top = stack.pop()
                if stack_top == '(':
                    if i !=')':
                        return False
                elif stack_top == '[':
                     if i !=']':
                        return False
                elif stack_top == '{':
                     if i !='}':
                        return False
        #check if stack is empty
        if stack:
            return False
        else:
            return True
        
sol = Solution()
print(sol.isValid("()"))
print(sol.isValid("()[]{}"))
print(sol.isValid( "(]"))
print(sol.isValid("([)]"))
print(sol.isValid("{[]}"))
print(sol.isValid("(){}}{"))
