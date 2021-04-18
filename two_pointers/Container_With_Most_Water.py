'''
Container With Most Water

Given n non-negative integers A[0], A[1], ..., A[n-1] , where each represents a point at coordinate (i, A[i]).
N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.
Note: You may not slant the container.

Problem Constraints
0 <= N <= 105
1 <= A[i] <= 105

Example Input
Input 1:
A = [1, 5, 4, 3]

Input 2:
A = [1]


Example Output
Output 1:
 6
Output 2:
 0
'''
class Solution:
	def maxArea(self, a):
        # safety case
	    if len(a)<2:
	        return 0
	    
	    area = 0
	    i = 0
	    j = len(a)-1
        # we need to inc the quatity of the water so we need to max the min(a[i],a[j])
        # if a[i] is min then inc i+=1
        # else dec j
	    while i<j:
	        area = max(area,(min(a[i],a[j])*(j-i)))
	        if a[i] < a[j]:
	            i += 1
	        else:
	            j -= 1
	    return area

# time complexity will be O(n^2)