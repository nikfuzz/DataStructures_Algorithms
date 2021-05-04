'''
Sort stack using another stack

Given a stack of integers A, sort it using another stack.
Return the array of integers after sorting the stack using another stack.

Problem Constraints
1 <= |A| <= 5000
0 <= A[i] <= 1000000000

Example Input
Input 1:
 A = [5, 4, 3, 2, 1]

Input 2:
 A = [5, 17, 100, 11]


Example Output
Output 1:
 [1, 2, 3, 4, 5]

Output 2:
 [5, 11, 17, 100]
'''

# one stack will be the input stack and another will be a temp/aux stack
# we only add an element in our temp stack if temp[-1] > x or when the stack is empty
# the temp stack will finally have sorted elements
from collections import deque

class Solution:
    def solve(self, a):
        inp = deque()
        temp = deque()
        for i in range(len(a)):
            inp.append(a[i])
        while inp:
            x = inp.pop()
            # pop all elements that are greater than incoming element in the temp stack
            while temp and temp[-1] > x:
                inp.append(temp.pop())
            
            temp.append(x)
        return temp
# TC O(n^2)
# SC O(n)