'''
TOP VIEW

Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.
Right view of a Binary Tree is a set of nodes visible when the tree is visited from top.
Return the nodes in any order.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Example Input
Input 1:

 
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8 
Input 2:

 
            1
           /  \
          2    3
           \
            4
             \
              5


Example Output
Output 1:

 [1, 2, 4, 8, 3, 7]
Output 2:

 [1, 2, 3]
'''

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# we will need a map of [distance from center] -> list[tuple([level, node.val])]
# when we go left dist from center dec and when we go right dist from center inc, by 1
# as we go down the tree the lvl increases
# After we make the map, we need to sort each list in the map bases on the lvl
# we then append the res with the first element of every list across each distance
class Solution:
    def topView(self, root, d, lvl, map):
        if not root: return
        if d not in map:
            map[d] = list([tuple([lvl, root.val])])
        else:
            map[d].append(tuple([lvl,root.val]))
        self.topView(root.left, d-1, lvl+1, map)
        self.topView(root.right, d+1, lvl+1, map)
        return
    
    def solve(self, root):
        map = {}
        self.topView(root,0,0,map)
        if not map: return []
        for i in map.values():
            i.sort(key=lambda x: x[0])
        mi = min(map)
        ma = max(map)
        res = []
        for i in range(mi,ma+1):
            j = map[i]
            res.append(j[0][1])
        return res
# TC O(n)
# SC O(n)
            
