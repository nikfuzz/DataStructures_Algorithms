'''
Count Rectangles

Given two arrays of integers A and B of size N each, where each pair (A[i], B[i]) for 0 <= i < N represents a unique point (x, y) in 2-D Cartesian plane.
Find and return the number of unordered quadruplet (i, j, k, l) such that (A[i], B[i]), (A[j], B[j]), (A[k], B[k]) and (A[l], B[l]) form a rectangle with the rectangle having all the sides parallel to either x-axis or y-axis.

Problem Constraints
1 <= N <= 2000
0 <= A[i], B[i] <= 10

Example Input
Input 1:
 A = [1, 1, 2, 2]
 B = [1, 2, 1, 2]

Input 1:
 A = [1, 1, 2, 2, 3, 3]
 B = [1, 2, 1, 2, 1, 2]


Example Output
Output 1:
 1

Output 2:
 3
'''
# we need to find the non-overlapping diagonal of the rectangles
# if x1,y2 and x2,y1 are given points then that rectangle is valid
class Solution:
    def solve(self, a, b):
        sett = set()
        for i in range(len(a)):
            temp = tuple([a[i],b[i]])
            sett.add(temp)
        count = 0
        for i in range(len(a)):
            for j in range(i+1,len(b)):
                if a[i] != a[j] and b[i] != b[j]:
                    if tuple([a[i],b[j]]) in sett and tuple([a[j],b[i]]) in sett:
                        count += 1
        # divide by two for same diagonals counted twice
        return count // 2

# TC O(n^2)
# SC O(n)
