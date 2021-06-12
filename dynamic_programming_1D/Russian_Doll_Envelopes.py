'''
Russian Doll Envelopes

Given a matrix of integers A of size N x 2 describing dimensions of N envelopes, 
where A[i][0] denotes the height of the ith envelope and A[i][1] denotes the width of the ith envelope.
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and 
height of the other envelope. Find the maximum number of envelopes you can put one inside other.

Problem Constraints
1 <= N <= 1000
1 <= A[i][0], A[i][1] <= 10^9

Example Input
Input 1:

 A = [ 
         [5, 4]
         [6, 4]
         [6, 7]
         [2, 3]  
     ]
Input 2:

 A = [     '
         [8, 9]
         [8, 18]    
     ]


Example Output
Output 1:

 3
Output 2:

 1
'''
# sort arr on the basis of height in asc order, if heights are same then
# sort them on the basis of width in desc order
# Then calculate longest increasing subsequence on the basis of width in the sorted arr
class Solution:
    def customSort(self, a):
        for i in range(len(a)):
            for j in range(len(a)-i-1):
                if a[j][0] > a[j+1][0]:
                    a[j], a[j+1] = a[j+1], a[j]
                elif a[j][0] == a[j+1][0] and a[j+1][1]>a[j][1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a
    
    def solve(self, a):
        a = self.customSort(a)
        a = [a[i][1] for i in range(len(a))]
        lis = [1]*len(a)
        for i in range(len(a)):
            for j in range(i):
                if a[i]>a[j]:
                    lis[i] = max(lis[i], 1+lis[j])
        return max(lis)
# TC O(n^2)
# SC O(n)