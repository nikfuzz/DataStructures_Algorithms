'''
Closest pair from sorted arrays

Given two sorted arrays of distinct integers, A and B, and an integer C, find and return the pair whose sum is closest to C and the pair has one element from each array.
More formally, find A[i] and B[j] such that abs((A[i] + B[j]) - C) has minimum value.
If there are multiple solutions find the one with minimum i and even if there are multiple values of j for the same i then return the one with minimum j.
Return an array with two elements {A[i], B[j]}.

Problem Constraints
1 <= length of both the arrays <= 100000
1 <= A[i], B[i] <= 109
1 <= C <= 109

Example Input
Input 1:
 A = [1, 2, 3, 4, 5]
 B = [2, 4, 6, 8]
 C = 9
Input 2:
 A = [5, 10, 20]
 B = [1, 2, 30]
 C = 13


Example Output
Output 1:
 [1, 8]
Output 2:
 [10, 2]
'''

class Solution:
    def solve(self, a, b, c):
        diff = float('inf')
        
        l = 0
        r = len(b)-1

        # start l from 0->len(a)-1 and r from len(b)-1 -> 0
        # We will find min abs(a[l] + b[r] - c)
        while l<len(a) and r>=0:
            if abs(a[l] + b[r] - c) < diff:
                i = l
                j = r
                diff = abs(a[l] + b[r] - c)
            
            # for multiple answers we need to select an answer which has min l, if l is same then min r
            elif abs(a[l] + b[r] - c) == diff:
                if i>l or (i==l and j>r):
                    i = l
                    j = r
            
            if a[l] + b[r] >= c:
                r -= 1
            else:
                l += 1
        return [a[i],b[j]]
# TC O(n)
# SC O(1)