'''
Count Right Triangles

Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2D Cartesian plane.
Find and return the number of unordered triplets (i, j, k) such that (A[i], B[i]), (A[j], B[j]) and (A[k], B[k]) form a right angled triangle with the triangle having one side parallel to the x-axis and one side parallel to the y-axis.
NOTE: The answer may be large so return the answer modulo (109 + 7).

Problem Constraints
1 <= N <= 105
0 <= A[i], B[i] <= 109

Example Input
Input 1:
 A = [1, 1, 2]
 B = [1, 2, 1]

Input 2:
 A = [1, 1, 2, 3, 3]
 B = [1, 2, 1, 2, 1]


Example Output
Output 1:
 1

Output 2:
 6
'''

class Solution:
    # from a pivot point, same x points and y points will give us the other two points to form the triangle
    # which is parallel to the axis
    # all the same x points - (pivot point, 1) * all the same y points - (pivot point, 1) will give us all triangles
    # for one pivot point
    def solve(self, a, b):
        ans = 0
        mx = {}
        my = {}
        
        for i in range(len(a)):
            if a[i] in mx:
                mx[a[i]] += 1
            else:
                mx[a[i]] = 1
            
            if b[i] in my:
                my[b[i]] += 1
            else:
                my[b[i]] = 1
        
        for i in range(len(a)):
            ans += (((mx[a[i]]-1)*(my[b[i]]-1)) % (10**9+7))
        
        return ans % (10**9+7)
# TC O(n)
# SC O(n+n) => O(n)
