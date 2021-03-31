'''
Finding Position

Given an integer A which denotes the number of people standing in the queue.
A selection process follows a rule where people standing on even positions are selected. 
Of the selected people a queue is formed and again out of these only people on even position are selected.
This continues until we are left with one person. Find and return the position of that person in the original queue.

Problem Constraints
1 <= A <= 109

Input 1:
 A = 10

Output 1:
 8

Input 2:
 A = 5

Output 2:
 4
'''

# observation: the last standing element is always the highest pow of 2 <= a
import math

class Solution:
    def solve(self, a):
        p = int(math.log(a,2))
        return int((2**p))
