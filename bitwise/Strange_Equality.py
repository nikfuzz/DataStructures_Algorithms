'''
Strange Equality

Given an integer A.
Two numbers X and Y are defined as follows:
X is the greatest number smaller than A such that XOR sum of X and A is the same as the sum of X and A.
Y is the smallest number greater than A such that XOR sum of Y and A is the same as the sum of Y and A.
Find and return the XOR of X and Y.
NOTE 1: XOR of X and Y is defined as X ^ Y where '^' is the BITWISE XOR operator.
NOTE 2: Your code will be run against a maximum of 100000 Test Cases.

Problem Constraints
1 <= A <= 109

Example Input
A = 5

Example Output
10
'''

import math

class Solution:
    # a + b = a^b + 2*(a&b)
    def solve(self, n):
        bits = int(math.log(n,2)) + 1
        # x is 2 pow just greater than n
        x = 1<<bits
        
        y = 0
        y = n
        # y is bit-inverse of n
        for i in range(bits):
            y = y ^ (1<<i) 
            
        
        return x^y