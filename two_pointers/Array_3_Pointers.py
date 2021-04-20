'''
Array 3 Pointers

You are given 3 sorted arrays A, B and C.
Find i, j, k such that : max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])).

Problem Constraints
0 <= len(A), len(B), len(c) <= 106
0 <= A[i], B[i], C[i] <= 107

Example Input
Input 1:
 A = [1, 4, 10]
 B = [2, 15, 20]
 C = [10, 12]

Input 2:
 A = [3, 5, 6]
 B = [2]
 C = [3, 4]


Example Output
Output 1:
 5

Output 2:
 1
'''
class Solution:
    # put a pointer on each arr
    # our goal is to maximize the subtracting value or min the adding val
    # since the arr is sorted we can only max the subtracting value
	def minimize(self, a, b, c):
	    i = j = k = 0
	    mi = float('inf')
	    while i < len(a) and j < len(b) and k<len(c):
	        ma = max((abs(a[i]-b[j]),abs(b[j]-c[k]),abs(c[k]-a[i])))
	        mi = min(ma,mi)

            # increment the min value since we want to maximize the subtracting value
	        if a[i] <= b[j] and a[i] <= c[k]:
	            i += 1
	        elif b[j] <= a[i] and b[j] <= c[k]:
	            j += 1
	        else:
	            k += 1
	    return mi