'''
Bob and Queries

Bob has an array A of N integers. Initially, all the elements of the array are zero. Bob asks you to perform Q operations on this array.
You have to perform three types of query, in each query you are given three integers x, y and z.
if x = 1: Update the value of A[y] to 2 * A[y] + 1.
if x = 2: Update the value A[y] to ⌊A[y]/2⌋ , where ⌊⌋ is Greatest Integer Function.
if x = 3: Take all the A[i] such that y <= i <= z and convert them into their corresponding binary strings. Now concatenate all the binary strings and find the total no. of '1' in the resulting string.
Queries are denoted by a 2-D array B of size M x 3 where B[i][0] denotes x, B[i][1] denotes y, B[i][2] denotes z.

Problem Constraints
1 <= N, Q <= 100000
1 <= y, z <= N
1 <= x <= 3

Example Input
Input 1:

 A = 5
 B = [   
        [1, 1, -1]
        [1, 2, -1]
        [1, 3, -1]   
        [3, 1, 3] 
        [3, 2, 4]   
     ]
Input 2:

 A = 5
 B = [   
        [1, 1, -1]
        [1, 2, -1]
        [3, 1, 3]
        [2, 1, -1]
        [3, 1, 3]   
     ]

Example Output
Output 1:

 [3, 2]
Output 2:

 [2, 1]
'''
# Build a segment tree for sum of nums from start to end
# To update choose a mid of start and end and check if id<= mid: go the left sub tree, else right sub tree
# To query find the range that fits our match, if a part of it fits then search for the next part in the other sub tree
class Solution:
    def buildSegmentTree(self, a, tree, ind, st, end):
        if st == end:
            tree[ind] = a[st]
            return
        mid = (st+end)//2
        self.buildSegmentTree(a,tree,2*ind+1,st,mid)
        self.buildSegmentTree(a,tree,2*ind+2,mid+1,end)
        tree[ind] = tree[2*ind+1] + tree[2*ind+2]
    
    def updateTree(self, a, tree, ind, st, end, id, val):
        if st == end:
            tree[ind] = val
            return
        mid = (st + end)//2
        if id <= mid:
            self.updateTree(a, tree, 2*ind+1, st, mid, id, val)
        else:
            self.updateTree(a, tree, 2*ind+2, mid+1, end, id, val)
        tree[ind] = tree[2*ind+1] + tree[2*ind+2]
    
    def queries(self, tree, ind, st, end, l, r):
        if r<st or l>end:
            return 0
        if l<=st and r>=end:
            return tree[ind]
        mid = (st+end)//2
        left = self.queries(tree, 2*ind+1, st, mid, l, r)
        right = self.queries(tree, 2*ind+2, mid+1, end, l, r)
        return (left+right)
    
    def solve(self, a, b):
        tree = [0]*(4*a)
        a = list([0]*a)
        self.buildSegmentTree(a,tree,0,0,len(a)-1)
        res = []
        for i in range(len(b)):
            if b[i][0] == 1:
                a[b[i][1]-1] = 2*a[b[i][1]-1]+1
                val = bin(a[b[i][1]-1]).split('0b')[1]
                val = val.count('1')
                self.updateTree(a, tree, 0, 0, len(a)-1, b[i][1]-1, val)
            if b[i][0] == 2:
                a[b[i][1]-1] = a[b[i][1]-1]//2
                val = bin(a[b[i][1]-1]).split('0b')[1]
                val = val.count('1')
                self.updateTree(a, tree, 0, 0, len(a)-1, b[i][1]-1, val)
            if b[i][0] == 3:
                ones = self.queries(tree, 0, 0, len(a)-1, b[i][1]-1, b[i][2]-1)
                res.append(ones)
        return res
# TC O(N + Q*log n), Q is the number of queries
# SC O(N)