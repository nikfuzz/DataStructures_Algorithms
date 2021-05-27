'''
Kth Smallest Element in a Sorted Matrix

Given a sorted matrix of integers A of size N x M and an integer B.
Each of the rows and columns of matrix A are sorted in ascending order, find the Bth smallest element in the matrix.
NOTE: Return The Bth smallest element in the sorted order, not the Bth distinct element.

Problem Constraints
1 <= N, M <= 500
1 <= A[i] <= 10**9
1 <= B <= N * M

Example Input
Input 1:

 A = [ [9, 11, 15],
       [10, 15, 17] ] 
 B = 6
Input 2:

 A = [  [5, 9, 11],
        [9, 11, 13],
        [10, 12, 15],
        [13, 14, 16],
        [16, 20, 21] ]
 B = 12


Example Output
Output 1:

 17
Output 2:

 16
'''
# add all the elements of arr in a min heap
# pop b-1 elements
# return root of the heap
import heapq as heap
class Solution:
    def solve(self, a, b):
        h = []
        for i in range(len(a)):
            for j in range(len(a[i])):
                h.append(a[i][j])
        heap.heapify(h)
        for i in range(b-1):
            heap.heappop(h)
        return h[0]
# TC O(n*m + b*log n), where n is the number of rows and m is the number of cols
# SC O(n*m), where n is the number of rows and m is the number of cols
