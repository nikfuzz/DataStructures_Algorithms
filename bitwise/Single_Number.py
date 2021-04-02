'''
Single Number

Given an array of integers A, every element appears twice except for one. Find that single one.
NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?


Problem Constraints:
2 <= |A| <= 2000000
0 <= A[i] <= INTMAX

Input 1:
 A = [1, 2, 2, 3, 1]

Output 1:
 3

Input 2:
 A = [1, 2, 2]

Output 2:
 1
'''

class Solution:
    # a^a = 0
	def singleNumber(self, a):
	    res = 0
	    for i in range(len(a)):
            res = res ^ a[i]
        return res