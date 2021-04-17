'''
Ath Magical Number

Given three positive integers A, B and C.
Any positive integer is magical if it is divisible by either B or C.
Return the Ath magical number. Since the answer may be very large, return it modulo 109 + 7.

Problem Constraints
1 <= A <= 109
2 <= B, C <= 40000

Example Input
Input 1:
 A = 1
 B = 2
 C = 3

Input 2:
 A = 4
 B = 2
 C = 3


Example Output
Output 1:
 2

Output 2:
 6
'''

class Solution:
    def gcd(self,a,b):
        if a == 0:
            return b
        else:
            return self.gcd(b%a,a)
    
    def solve(self, a, b, c):
        # formula for lcm
        lcm = (b*c) // self.gcd(b,c)
        
        l = 0
        r = a*(max(b,c))
        
        ans = 0
        
        while l<=r:
            m = (l+r)//2
            
            # numbers divded by b and c minus common - for a mid value
            count = ((m//b) + (m//c) - (m//lcm))
            
            if count >= a:
                ans = m
                r = m-1
            
            else:
                l = m+1
        
        return (ans%((10**9) + 7)) 
        
