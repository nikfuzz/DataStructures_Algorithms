'''
Colorful Number

For Given Number A find if its COLORFUL number or not.
If number A is a COLORFUL number return 1 else return 0.
What is a COLORFUL Number:
A number can be broken into different contiguous sub-subsequence parts. 
Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.

Problem Constraints
1 <= A <= 2 * 109

Example Input
Input 1:
 A = 23

Input 2:
 A = 236


Example Output
Output 1:
 1

Output 2:
 0
'''

class Solution:
    # make a digits arr
    # find product from i to n and put it in a set
    # if the val already exists in the set return 0
	def colorful(self, a):
	    digits = [int(x) for x in str(a)]
	    
	    sett = set()
	    
	    for i in range(0,len(digits)):
	        product = 1
	        for j in range(i,len(digits)):
	            product *= digits[j]
	            if product in sett:
	                return 0
	            else:
	                sett.add(product)
	    return 1
# TC O(n^2)
# SC O(n)