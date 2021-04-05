'''
Trailing Zeros in Factorial

Given an integer A, return the number of trailing zeroes in A! i.e. factorial of A.
Note: Your solution should run in logarithmic time complexity.

Problem Constraints:
1 <= A <= 109

Input 1
 A = 5
Input 2:
 A = 6

Output 1:
 1
Output 2:
 1
'''

class Solution:
# we count all 5s in the factors of a!
    def trailingZeroes(self, a):
        count = 0
        while a>=5:
            a = a//5
            count += a
        return count
