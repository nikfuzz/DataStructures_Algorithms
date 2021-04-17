'''
Given two Integers A, B. You have to calculate (A ^ (B!)) % (1e9 + 7).
"^" means power ,
"%" means "mod", and
"!" means factorial.

Problem Constraints
1 <= A, B <= 5e5

Input 1:
A = 1
B = 1

Input 2:
A = 2
B = 2

Output 1:
1

Output 2:
4
'''

import math
import sys

sys.setrecursionlimit(10**6)

class Solution:
    m = (10**9 + 7)
            
    def powpow(self,a,b,m):
        if b == 0:
            return 1
        if b%2 == 0:
            return self.powpow(a*a%m, b//2,m) % m
        else:
            return a %m * self.powpow(a*a%m, b//2,m) % m

    
    
    def solve(self, a, b):
        # calculate factorial
        for i in range(1,b):
            b = (b * i) % (self.m-1)
        
        # using fermat's theorm we get the power value
        b = b % (self.m-1)
        # use binary exponentiation
        a = self.powpow(a,b,self.m) % self.m
        
        return a