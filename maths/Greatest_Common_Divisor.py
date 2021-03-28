'''
Greatest Common Divisor

Given 2 non negative integers A and B, find gcd(A, B)
GCD of 2 integers A and B is defined as the greatest integer g such that g is a divisor of both A and B. 
Both A and B fit in a 32 bit signed integer.

constraints:
0 <= A, B <= 109

input:
A = 4
B = 6

output: 2

input: 
A = 6
B = 7

output: 1
'''
import sys

sys.setrecursionlimit(10**6)
class Solution:
    # a%g = 0 and b%g = 0
    # => (a-b) % g = 0 => (a-b) % g
    # % will give repeating minus => we can use a%b instead of a-b
	def gcd(self, a, b):
	    if a == 0:
	        return b
	    return self.gcd(b%a, a)