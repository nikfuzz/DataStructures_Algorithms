'''
Longest Increasing Subsequence

Find the longest increasing subsequence of a given array of integers, A.
In other words, find a subsequence of array in which the subsequence's elements are in strictly increasing order, 
and in which the subsequence is as long as possible.
In this case, return the length of the longest increasing subsequence.

Problem Constraints
0 <= length(A) <= 2500
1 <= A[i] <= 2500

Example Input
Input 1:

 A = [1, 2, 1, 5]
Input 2:

 A = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]


Example Output
Output 1:

 3
Output 2:

 6
'''
# for choosing ith element you have to find the max lis from 0 to i-1 where a[i]>a[j]
# if we choose the ith element we take max(lis[i], lis[j]+1)
class Solution:
    def lis(self, a):
        lis = [1]*len(a)
        for i in range(1, len(a)):
            for j in range(i):
                if a[i] > a[j]:
                    lis[i] = max(lis[i], lis[j]+1)
        return max(lis)
# TC O(n^2)
# SC O(n)
