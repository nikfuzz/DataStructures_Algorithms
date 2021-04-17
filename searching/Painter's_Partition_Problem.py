'''
Painter's Partition Problem
Given 2 integers A and B and an array of integers C of size N. Element C[i] represents length of ith board.
You have to paint all N boards [C0, C1, C2, C3 … CN-1]. There are A painters available and each of them takes B units of time to paint 1 unit of board.

Calculate and return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board.
NOTE:
1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. Which means a configuration where painter 1 paints board 1 and 3 but not 2 is invalid.

Return the ans % 10000003.

Problem Constraints
1 <= A <= 1000
1 <= B <= 106
1 <= N <= 105
1 <= C[i] <= 106

Example Input
Input 1:
 A = 2
 B = 5
 C = [1, 10]

Input 2:
 A = 10
 B = 1
 C = [1, 8, 11, 3]


Example Output
Output 1:
 50

Output 2:
 11
'''

class Solution:
# check function to check if the current m is valid or not
    def check(self,a,b,c,m):
        sum = 0
        n = 1
        for i in range(len(c)):
            sum += (c[i]*b)
            if sum > m:
                n += 1
                if n > a:
                    return False
                sum = c[i] * b
        return True
            

# 	max boards
    def paint(self, a, b, c):
        # we need to select such a number which gives us min time to paint all boards
        # in the given number of painters
        l = max(c) * b
        r = sum(c) * b
        
        ans = r
        
        while l <= r:
            m = (l+r)//2
            
            if self.check(a,b,c,m):
                ans = min(ans,m)
                r = m-1
            else:
                l = m+1
                
        return ans % 10000003
