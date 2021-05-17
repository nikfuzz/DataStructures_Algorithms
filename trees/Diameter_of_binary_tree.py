'''
Diameter of binary tree

Given a Binary Tree A consisting of N integer nodes, you need to find the diameter of the tree.
The diameter of a tree is the number of edges on the longest path between two nodes in the tree.

Problem Constraints
0 <= N <= 105

Example Input
Input 1:

           1
         /   \
        2     3
       / \
      4   5
Input 2:

            1
          /   \
         2     3
        / \     \
       4   5     6


Example Output
Output 1:

 3
Output 2:

 4
'''

import sys
sys.setrecursionlimit(10**6)
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# We make a new class to store height and diameter at each node
class NodeInfo:
    def __init__(self,h,dia):
        self.h = h
        self.dia = dia
# Post order
# Store height and diameter for every node
# diameter is max of l.height + r.height + 2(for the edges from node) or left diameter or right diameter 
class Solution:
    def calDia(self,root):
        if not root:
            return NodeInfo(-1,-1)
        
        l = (self.calDia(root.left))
        r = (self.calDia(root.right))
        
        height = 1 + max(l.h, r.h)
        dia = max(l.h + r.h + 2, l.dia, r.dia)
        return NodeInfo(height, dia)
    
    def solve(self, root):
        ans = self.calDia(root)
        return ans.dia
# TC O(n)
# SC O(n)
        