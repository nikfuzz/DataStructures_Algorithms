'''
Find nth Magic Number

Given an integer A, find and return the Ath magic number.
A magic number is defined as a number which can be expressed as a power of 5 or sum of unique powers of 5.
First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….

Problem Constraints
1 <= A <= 5000

Example Input 1:
 A = 3
Example Input 2:
 A = 10

Example Output 1:
 30
Example Output 2:
 650
'''

class Solution:
    def solve(self, n):
        ans = 0
        x = 1
        
        # need to add 5**i+1 for every set bit
        while n>0:
            x *= 5
            # checks if n is odd
            if n&1 == 1:
                ans += x
            n = n >> 1
        
        return ans