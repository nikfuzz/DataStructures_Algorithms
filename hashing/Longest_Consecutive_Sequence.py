'''
Longest Consecutive Sequence

Given an unsorted integer array A of size N.
Find the length of the longest set of consecutive elements from the array A.

Problem Constraints
1 <= N <= 106
-106 <= A[i] <= 106

Example Input
Input 1:
A = [100, 4, 200, 1, 3, 2]
Input 2:
A = [2, 1]


Example Output
Output 1:
 4
Output 2:
 2
'''
class Solution:
    # store all the numbers in a hashmap
    # first find the starting of the set of consecutive elements
    # count the numbers which you find by inc 1
	def longestConsecutive(self, a):
	    sett = set()
	    for i in range(len(a)):
	        sett.add(a[i])
	    ans = float('-inf') 
	    for i in range(len(a)):
	        if a[i]-1 not in sett:
	            count = 1
	            curr_subset = a[i]
	            while curr_subset + 1 in sett:
	                count += 1
	                curr_subset += 1
	            ans = max(count, ans)
	    return ans
# tc O(n)
# sc O(n)