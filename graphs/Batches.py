'''
Batches

A students applied for admission in IB Academy. An array of integers B is given representing the strengths of A people i.e. B[i] represents the strength of ith student.
Among the A students some of them knew each other. A matrix C of size M x 2 is given which represents relations where ith relations depicts that C[i][0] and C[i][1] knew each other.
All students who know each other are placed in one batch.
Strength of a batch is equal to sum of the strength of all the students in it.
Now the number of batches are formed are very much, it is impossible for IB to handle them. So IB set criteria for selection: All those batches having strength at least D are selected.
Find the number of batches selected.
NOTE: If student x and student y know each other, student y and z know each other then student x and student z will also know each other.

Problem Constraints
1 <= A <= 10^5
1 <= M <= 2*10^5
1 <= B[i] <= 10^4
1 <= C[i][0], C[i][1] <= A
1 <= D <= 10^9

Example Input
Input 1:

 A = 7
 B = [1, 6, 7, 2, 9, 4, 5]
 C = [  [1, 2]
        [2, 3] 
       `[5, 6]
        [5, 7]  ]
 D = 12
Input 2:

 A = 5
 B = [1, 2, 3, 4, 5]
 C = [  [1, 5]
        [2, 3]  ]
 D = 6

Example Output
Output 1:

 2
Output 2:

 1
'''
# Create a Disjoint Set Union for the nodes and the edges mentioned in the arr c
# Also keep updating the new strength of the aggregated nodes in a different arr
# Assign this sum to the parent of every set
# When calculating sum of each set take sum of only unvisited root parent into consideration
import sys
sys.setrecursionlimit(10**6)

class DSU:
    def __init__(self, n, b):
        self.parent = [i for i in range(n+1)]
        self.size = [1 for i in range(n+1)]
        self.vis = set()
        self.str = b
        self.str.insert(0,0)
        
    def findSet(self, v):
        if v == self.parent[v]:
            return v
        self.parent[v] = self.findSet(self.parent[v])
        return self.parent[v]
        
    def unionSet(self, u, v):
        v = self.findSet(v)
        u = self.findSet(u)
        if v != u:
            if self.size[v] < self.size[u]:
                v, u = u, v
            self.parent[u] = v
            self.size[v] += self.size[u]
            self.str[v] += self.str[u]
            self.str[u] = 0
            
    def findSum(self, v):
        parent = self.findSet(v)
        if parent in self.vis:
            return 0
        self.vis.add(parent)
        return self.str[parent]
        

class Solution:
    def solve(self, a, b, c, d):
        dsu = DSU(a,b)
        for i in range(len(c)):
            dsu.unionSet(c[i][0],c[i][1])
        batches = 0
        for i in range(1,a+1):
            batchSum = dsu.findSum(i)
            if batchSum >= d:
                batches += 1
        return batches
# TC: Amortised O(1) for all DSU functions and O(n) for traversing all nodes => O(n)
# SC O(n)
