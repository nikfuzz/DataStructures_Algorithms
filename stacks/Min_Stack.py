'''
Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
NOTE:
All the operations have to be constant time operations.
getMin() should return -1 if the stack is empty.
pop() should return nothing if the stack is empty.
top() should return -1 if the stack is empty.

Problem Constraints
1 <= Number of Function calls <= 107

Example Input
Input 1:

push(1)
push(2)
push(-2)
getMin()
pop()
getMin()
top()

Input 2:
getMin()
pop()
top()


Example Output
Output 1:
 -2 1 2

Output 2:
 -1 -1
'''

# maintain two stacks
# one will push and pop as specified
# our second stack will be a min stack. We will push element into it only when its top is bigger than the element we need to push.
# pop when that element gets popped from the main stack
# when getmin is called return top of the min stack

from collections import deque

class MinStack:
    stack = deque()
    min_stack = deque()
    
    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if self.min_stack:
            if self.min_stack[-1] > x:
                self.min_stack.append(x)
        else:
            self.min_stack.append(x)
        return x
            

    # @return nothing
    def pop(self):
        if (self.stack and self.min_stack)and self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        if self.stack:
            self.stack.pop()
        

    # @return an integer
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1
        

    # @return an integer
    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return -1
# TC O(n)
# SC O(n)