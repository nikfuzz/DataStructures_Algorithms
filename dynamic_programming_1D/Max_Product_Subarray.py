'''
Max Product Subarray

Given an integer array A of size N. Find the contiguous subarray within the given array (containing at least one number) which has the largest product.
Return an integer corresponding to the maximum product possible.
NOTE: Answer will fit in 32-bit integer value.

Problem Constraints
1 <= N <= 5 * 10^5
-100 <= A[i] <= 100

Example Input
Input 1:

 A = [4, 2, -5, 1]
Input 2:

 A = [-3, 0, -5, 0]


Example Output
Output 1:

 8
Output 2:

 0
'''
# we need to maitain two dp arr. One will have max values uptil ith ind and the other one will have min val
# We need the min arr as well because we have negative numbers in an input so a number which is much bigger but negative 
# can give a max value when multiplied by another negative number
class Solution:
    def maxProduct(self, a):
        dp1 = [None]*(len(a))
        dp2 = [None]*(len(a))
        dp1[0] = a[0]
        dp2[0] = a[0]
        for i in range(1,len(a)):
            dp1[i] = min(a[i], a[i]*dp1[i-1], a[i]*dp2[i-1])
            dp2[i] = max(a[i], a[i]*dp1[i-1], a[i]*dp2[i-1])
        return max(max(dp1), max(dp2))
# TC O(n)
# SC O(n)
            
