'''
Compute nCr % p

Given three integers A, B and C, where A represents n, B represents r and C represents p and p is a prime number greater than equal to n, find and return the value of nCr % p where nCr % p = (n! / ((n-r)! * r!)) % p.
x! means factorial of x i.e. x! = 1 * 2 * 3... * x.
NOTE: For this problem, we are considering 1 as a prime.

Problem Constraints
1 <= A <= 106
1 <= B <= A
A <= C <= 109+7

Input 1:
 A = 5
 B = 2
 C = 13

Input 2:
 A = 6
 B = 2
 C = 13

Output 1:
 10
Output 2:
 2
'''

import sys

sys.setrecursionlimit(10**6)

class Solution:
    # binary exponentiation
    def binExp(self,a,b,m):
        if b == 0:
            return 1
        
        if b & 1 == 0:
            return self.binExp(a*a%m,b//2,m)
        else:
            return a*self.binExp(a*a%m,b//2,m)
    
    def solve(self, n, r, m):
        # case of nCn
        if n==r:
            return 1%m
        
        # we need to find fact(n) % mod
        # the denominator will be given by the modular inverse of the actual denominator
        r = min(n, n - r)
        facn = deno = 1
        
        for i in range(r):
            facn = (facn * (n-i))%m
            deno = (deno * (i+1))%m
        
        if m > 2:
            return (facn * self.binExp(deno,m-2,m))%m
        elif deno:
            return (facn/deno) % m
        else:
            return 1
            