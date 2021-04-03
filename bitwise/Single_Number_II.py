'''
Single Number II

Given an array of integers, every element appears thrice except for one which occurs once.
Find that element which does not appear thrice.
NOTE: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Problem Constraints:
2 <= A <= 5*106
0 <= A <= INTMAX

Input 1:
 A = [1, 2, 4, 3, 3, 2, 2, 3, 1, 1]

Input 2:
 A = [0, 0, 0, 1]

Output 1:
 4
Output 2:
 1
'''

class Solution:
    # verically add all the bits in each number
	def singleNumber(self, a):
	    res = 0
	    for i in range(32):
	        par = 0
	        cmp = (1<<i)
	        for j in range(len(a)):
	            if cmp & a[j]:
	                par += 1
            # if a bit pos %3 == 0 then the number occ twice
	        if par%3 != 0:
	            res = res | cmp
	    return res
	        