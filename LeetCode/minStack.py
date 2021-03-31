#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
# MinStack() initializes the stack object.
# void push(val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.

#####################
#getMin: O(1) 
#####################
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
                
    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            if self.stack[-1]==self.minStack[-1]:
                self.stack.pop()
                self.minStack.pop()
            else: self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
minS = MinStack()
print(minS.push(-2))
print(minS.push(0))
print(minS.push(-3))
print(minS.getMin())
print(minS.pop())
print(minS.top())
print(minS.getMin())


###########
#getMin O(n)
###########
# class MinStack(object):

#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
        
#     def push(self, val):
#         """
#         :type val: int
#         :rtype: None
#         """
#         self.stack.append(val)
        
#     def pop(self):
#         """
#         :rtype: None
#         """
#         if self.stack:
#             self.stack.pop()
        
#     def top(self):
#         """
#         :rtype: int
#         """
#         if self.stack:
#             return self.stack[-1]
        
#     def getMin(self):
#         """
#         :rtype: int
#         """
#         if self.stack:
#             return min(self.stack)
        