'''
Binary updates

Given an integer A denoting the size of the array consisting all ones.

You are given Q queries, for each query there are two integer x and y:

If x is 0, then update the value of array at index y to 0.
If x is 1, then output the index of yth one in the array. If there is no such index then output -1.
NOTE 1: There will atleast 1 query where value of x is 1.

Problem Constraints
1 <= A, Q <= 105
0 <= x <= 1
1 <= y <= A

Example Input
Input 1:

 A = 4
 B = [ [1, 2],
       [0, 2],
       [1, 4] ]
Input 2:

 A = 5
 B = [ [0, 3],
       [1, 4],
       [0, 3],
       [1, 5] ] 


Example Output
Output 1:

 [2, -1]
Output 2:

 [5, -1]
'''

from math import ceil, log2
# segment free class
class SegmentTree:
    def __init__(self, a):
        x = (int)(ceil(log2(len(a))))
        self.tree = [0]* (2 * (int)(2**x) - 1)
        self.buildTree(a, 0, 0, len(a)-1)
        
    def buildTree(self, a, ind, st, end):
        if st == end:
            self.tree[ind] = a[st]
            return
        mid = (st + end)//2
        self.buildTree(a, 2*ind+1, st, mid)
        self.buildTree(a, 2*ind+2, mid+1, end)
        self.tree[ind] = self.tree[2*ind+1] + self.tree[2*ind+2]
        
    def updateTree(self, id, ind, st, end):
        if st == end:
            self.tree[ind] = 0
            return
        mid = (st + end)//2
        if st <= id and id<= mid:
            self.updateTree(id, 2*ind+1, st, mid)
        else:
            self.updateTree(id, 2*ind+2, mid+1, end)
        self.tree[ind] = self.tree[2*ind+1] + self.tree[2*ind+2]
        
    def queries(self, ind, st, end, y):
        if y>self.tree[ind]:
            return -1
        if st == end:
            return st
        mid = (st+end)//2
        l = self.tree[2*ind+1]
        if l >= y:
            return self.queries(2*ind+1, st, mid, y)
        else:
            return self.queries(2*ind+2, mid+1, end, y-l)

# We will store sum of 1s for a given range in a segment tree
# For updation follow a tree traversal. If id <= mid then look for id in the left subtree else look in the right sub tree
# For queries we first check the left child value. If the left child has a sum >= the yth one we are trying to find then 
# look for the answer in the left subtree else look for y-l in right sub tree
# We do the above two steps because we need to find the **first** yth 1
class Solution:
    def solve(self, a, b):
        a = list([1]*a)
        st = SegmentTree(a)
        res = []
        for i in range(len(b)):
            if b[i][0] == 0:
                st.updateTree(b[i][1]-1, 0, 0, len(a)-1)
            elif b[i][0] == 1:
                ans = st.queries(0, 0, len(a)-1, b[i][1])
                if ans == -1:
                    res.append(ans)
                else:
                    res.append(ans+1)
        return res
# TC O(n * log n)
# SC O(n)