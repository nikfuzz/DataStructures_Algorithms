'''
Delete one

Given an integer array A of size N. 
You have to delete one element such that the GCD(Greatest common divisor) of the remaining array is maximum.
Find the maximum value of GCD.

Constraints:
2 <= N <= 105
1 <= A[i] <= 109

input: [12, 15, 18]
output: 6

input: [5, 15, 30]
output: 15
'''

class Solution:
    def gcd(self,a,b):
        if a == 0:
            return b
        else:
            return self.gcd(b%a, a)
    
    # calculate prefix gcd arr and suffix gcd arr
    # gcd of pref[i-1] and suff[i+1] will give gcd of arr without (i)
    def solve(self, a):
        pref = [0]*len(a)
        suff = [0]*len(a)
        
        ma = float('-inf')
        g = 0
        for i in range(len(a)):
            g = self.gcd(g,a[i])
            pref[i] = g
        
        g = 0
        for i in range(len(a)-1, -1, -1):
            g = self.gcd(g,a[i])
            suff[i] = g
        
        g_l = 0
        g_r = 0
        for i in range(len(a)):
            if i == 0:
                g_l = 0
                g_r = suff[i+1]
            elif i == len(a)-1:
                g_r = 0
                g_l = pref[i-1]
            else:
                g_l = pref[i-1]
                g_r = suff[i+1]
            ma = max(ma,self.gcd(g_l,g_r))
        return ma