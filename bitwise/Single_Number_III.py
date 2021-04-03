'''
Single Number III

Given an array of numbers A , in which exactly two elements appear only once and all the other elements appear exactly twice. 
Find the two elements that appear only once.
Note: Output array must be sorted.

Input 1:
A = [1, 2, 3, 1, 2, 4]

Input 2:
A = [1, 2]

Output 1:
[3, 4]

Output 2:
[1, 2]
'''

class Solution:
    # we need to divide the arr into two parts
    # 1 numbers which have 1 in msb of xor of arr and 2 which have 0s
    def solve(self, a):
        xor = 0
        for i in range(len(a)):
            xor = xor ^ a[i]
        
        xor2 = xor1 = 0
        # msb of xor
        filter = (xor & (xor-1)) ^ xor
        # one of the numbers will be in xor1 and another in xor2
        for i in range(len(a)):
            if filter & a[i]:
                xor1 = xor1^a[i]
            else:
                xor2 = xor2^a[i]
        if xor1 < xor2:
            return [xor1,xor2]
        return[xor2,xor1]
