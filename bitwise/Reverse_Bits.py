'''
Reverse Bits

Reverse the bits of an 32 bit unsigned integer A.

Problem Constraints
0 <= A <= 232

Input 1:
 0
Input 2:
 3

Output 1:
 0
Output 2:
 3221225472
'''

class Solution:
    # reverse the string and append missing 0s to make it 32bit
    def reverse(self, a):
        s = bin(a).replace("0b", "")
        s = s[::-1]
        i = 0
        while i < (32-len(s)):
            s += '0'
            i += 1
        return int(s,2)
