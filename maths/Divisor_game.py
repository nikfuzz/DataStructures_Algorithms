'''
Divisor game

Scooby has 3 three integers A, B and C.
Scooby calls a positive integer special if it is divisible by B and it is divisible by C. 
You need to tell number of special integers less than or equal to A.

Constraints:
1 <= A, B, C <= 109

input:
 A = 12
 B = 3
 C = 2

output: 2

input: 
 A = 6
 B = 1
 C = 4

output: 1
'''

class Solution:
    def gcd(self,a,b):
        if a == 0:
            return b
        else:
            return self.gcd(b%a, a)
    
    def solve(self, a, b, c):
        # lcm(a,b) = (a*b)/gcd(a,b)
        # return count of multiples of lcm from 1 to a
        lcm = (b * c)//self.gcd(b,c)
        
        return (a//lcm)