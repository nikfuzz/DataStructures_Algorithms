'''
Enumerating GCD

You are given a number A and a number B. 
Greatest Common Divisor (GCD) of all numbers between A and B inclusive is taken (GCD(A, A+1, A+2 ... B)).
As this problem looks a bit easy, it is given that numbers A and B can be in the range of 10100.
You have to return the value of GCD found.
Greatest common divisor of 2 numbers A and B is the largest number D that divides both A and B perfectly.

Constraints:
1 <= A <= B <= 10100

input:
A = "1"
B = "3"

output: 1
'''

class Solution:
    # gcd from a to b is 1 or the iteration from a to b
    # if a == b then gcd is the number itself
    def solve(self, a, b):
        if a == b:
            return a
        
        return "1"