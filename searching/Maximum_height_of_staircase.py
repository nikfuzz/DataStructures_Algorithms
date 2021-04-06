'''
Maximum height of staircase

Given an integer A representing the number of square blocks. The height of each square block is 1. The task is to create a staircase of max height using these blocks.
The first stair would require only one block, the second stair would require two blocks and so on.
Find and return the maximum height of the staircase.

Problem Constraints
0 <= A <= 109

Input 1:
 A = 10
Input 2:
 20


Example Output
Output 1:
 4
Output 2:
 5
'''

class Solution:
    # keep iterating i by 1 to inc the steps and check if we have enough n to subtract i
    def solve(self, n):
        if n == 0:
            return 0
        i = 1
        while n>0:
            n -= i
            if i + 1>n:
                return i
            i += 1
        return i