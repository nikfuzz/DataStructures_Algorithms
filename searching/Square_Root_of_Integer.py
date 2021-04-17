'''
Square Root of Integer

Given an integer A.
Compute and return the square root of A.
If A is not a perfect square, return floor(sqrt(A)).
DO NOT USE SQRT FUNCTION FROM STANDARD LIBRARY.
NOTE: Do not use sort function from standard library. Users are expected to solve this in O(log(A)) time.

Problem Constraints
0 <= A <= 10^10

Example Input
Input 1:
 11
Input 2:
 9

Example Output
Output 1:
 3
Output 2:
 3
'''

class Solution:
    def sqrt(self, n):
        
        if n == 1:
            return 1
        # use binary search to find a number (m*m) closest or exactly equal to the input
        l = 0
        r = n//2
        ans = 0
        
        while l<=r:
            m = (l+r)//2
            
            if m*m <= n:
                ans = m
                l = m+1
            
            else:
                r = m-1
        return ans
