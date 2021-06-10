'''
Length of LIS

You are given an array A. You need to find the length of the Longest Increasing Subsequence in the array.
In other words, you need to find a subsequence of array A in which the elements are in sorted order, 
(strictly increasing) and as long as possible.

Problem Constraints
1 ≤ length(A), A[i] ≤ 10^5

Example Input
Input 1:

A: [2, 1, 4, 3]
Input 2:

A: [5, 6, 3, 7, 9]


Example Output
Output 1:

2
Output 2:

4
'''
# Create a temp array which will store the longest inc substring till i, and a lis var to store the length
# We keep adding a[i] to the temp
# if temp[-1] < a[i] then we can just append a[i] and inc lis
# else we need to find the right position in the temp for a[i] using binary search and replace temp[pos] with a[i]
class Solution:
    def binS(self, temp, k):
        l = 0
        r = len(temp)
        ans = 0
        while l<r:
            m = (l+r)//2
            if temp[m] < k:
                l = m+1
            else:
                ans = m
                r = m
        return ans
    
    def findLIS(self, a):
        temp = []
        lis = 0
        for i in range(0,len(a)):
            if not temp:
                temp.append(a[i])
                lis += 1
            elif temp[-1] < a[i]:
                temp.append(a[i])
                lis += 1
            elif temp[-1] >= a[i]:
                pos = self.binS(temp, a[i])
                temp[pos] = a[i]
        return lis
# TC O(n*log n)
# SC O(n)