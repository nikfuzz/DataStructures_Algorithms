'''
Divide Integers

Divide two integers without using multiplication, division and mod operator.
Return the floor of the result of the division.
Also, consider if there can be overflow cases i.e output is greater than INT_MAX, return INT_MAX.
NOTE: INT_MAX = 2^31 - 1

Problem Constraints:
-231 <= A, B <= 231-1
B!= 0

Input 1:
 A = 5
 B = 2

Input 2:
 A = 7
 B = 1

Output 1:
 2
Output 2:
 7
'''

class Solution:
	def divide(self, a, b):
	    int_max = 2**31 - 1
        # if one of a or b is neg then the ans is neg
	    sign = 1
	    if (a < 0) ^ (b < 0):
	        sign = -1
	    a = abs(a)
	    b = abs(b)
	    t = 0
	    q = 0
        # we find the highest pow of 2 when multiplied with b is just smaller or equal to a
        # we keep adding the prev result to t which has to be added for next highest pow multiplication
	    for i in range(31,-1,-1):
	        if t+(b<<i) <= a:
	            t += (b<<i)
	            q = q | (1<<i)
	    
	    q = sign*q
	    
	    if int_max<q:
	        return int_max
	    else:
	        return q
	        