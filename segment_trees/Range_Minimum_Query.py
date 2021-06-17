'''
Range Minimum Query

Given an integer array A of size N.
You have to perform two types of query, in each query you are given three integers x,y,z.
If x = 0, then update A[y] = z.
If x = 1, then output the minimum element in the array A between index y and z inclusive.
Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.

Problem Constraints
1 <= N, M <= 10^5
1 <= A[i] <= 10^9
If x = 0, 1<= y <= N and 1 <= z <= 10^9
If x = 1, 1<= y <= z <= N

Example Input
Input 1:

 A = [1, 4, 1]
 B = [ 
        [1, 1, 3]
        [0, 1, 5]
        [1, 1, 2] 
     ]
Input 2:

 A = [5, 4, 5, 7]
 B = [ 
        [1, 2, 4]
        [0, 1, 2]
        [1, 1, 4]
     ]


Example Output
Output 1:

 [1, 4]
Output 2:

 [4, 2]
'''
from math import ceil, log2

class SegmentTree:
    def __init__(self, a):
        x = (int)(ceil(log2(len(a))))
        self.tree = [10**9+1]* (2 * (int)(2**x) - 1)
        self.buildTree(a,0,0,len(a)-1)
        
    def buildTree(self, a, ind, st, end):
        if st == end:
            self.tree[ind] = a[st]
            return
        m = (st + end)//2
        self.buildTree(a, 2*ind+1, st, m)
        self.buildTree(a, 2*ind+2, m+1, end)
        self.tree[ind] = min(self.tree[2*ind+1], self.tree[2*ind+2])
        
    def updateTree(self, id, ind, st, end, val):
        if st == end:
            self.tree[ind] = val
            return
        m = (st+end)//2
        if id<=m:
            self.updateTree(id,2*ind+1,st,m,val)
        else:
            self.updateTree(id,2*ind+2,m+1,end,val)
        self.tree[ind] = min(self.tree[2*ind+1], self.tree[2*ind+2])
        
    def queries(self, ind, st, end, l, r):
        if r<st or l>end:
            return float('inf')
        if l<=st and r>=end:
            return self.tree[ind]
        m = (st+end)//2
        left = self.queries(2*ind+1, st, m, l, r)
        right = self.queries(2*ind+2, m+1, end, l, r)
        return min(left, right)
        
# create a segment tree for min nodes from range st to end
# for queries we need to find a rande of st and end for which l and r (ans range) are l<=st and r>=end.
# if r<st or l>end then we return int_max since we are looking at the wrong range
# if our searching range is smaller then the given range then include the ans for curr searching range and look in the 
# next subtree for remaining searching range
# for updating use binary search to find the given node, update the value, and then keep updating value for 
# all its parent nodes
class Solution:
    def solve(self, a, b):
        st = SegmentTree(a)
        res = []
        for i in range(len(b)):
            if b[i][0] == 1:
                ans = st.queries(0, 0, len(a)-1, b[i][1]-1, b[i][2]-1)
                res.append(ans)
            elif b[i][0] == 0:
                st.updateTree(b[i][1]-1, 0, 0, len(a)-1, b[i][2])
        return res

