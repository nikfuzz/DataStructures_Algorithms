'''
Prime Modulo Inverse

Given two integers A and B. Find the value of A-1 mod B where B is a prime number and gcd(A, B) = 1.
A-1 mod B is also known as modular multiplicative inverse of A under modulo B.

Problem Constraints:
1 <= A <= 109
1<= B <= 109
B is a prime number

Input 1:
 A = 3
 B = 5

Output 1:
 2

Input 2:
 A = 6
 B = 23

Output 2:
 4
'''

class Solution:
    # binary exponentiation
    def powpow(self,a,b,m):
        if b == 0:
            return 1
        if b%2 == 0:
            return self.powpow(a*a%m, b//2,m)
        else:
            return a * self.powpow(a*a%m, b//2,m)
    
    # acc to fermat's theorm taking mod of a ^ mod-2 gives us the modulo inverse
    def solve(self, a, m):
        res = self.powpow(a,m-2,m)
        return res%m