'''
Smallest Good Base

Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1. 
Now given a string representing A, you should return the smallest good base of A in string format.

Constraints
3 <= A <= 10^18

Input 1:
    A = "13"
Output 1:
    "3"     (13 in base 3 is 111)

Input 2:
    A = "4681"
Output 2:
    "8"     (4681 in base 8 is 11111).
'''

import math
# we check from 64 1s to one 1
# the base for that set of 1s should give us the ip number
# n-1 will always be true but we need to find a number shorter than n-1
class Solution:
    def check(self,n,i):
        
        l = 2
        r = n-1
        
        while(l<=r):
            m = (l+r)//2
            
            sum = 0
            temp = 1
            for j in range(i):
                sum += temp
                temp *= m
                
            if sum == n:
                return m
            elif sum > n:
                r = m-1
            else:
                l = m+1
            
        return -1
        
        
    
    def solve(self, a):
    
        n = int(a)
        x = float('inf')
        for i in range(64,0,-1):
            if self.check(n,i) != -1:
                x = min(self.check(n,i),x)

        if x >= 2 and x != float('inf'):
            return str(x)
        return str(n-1)
            
            