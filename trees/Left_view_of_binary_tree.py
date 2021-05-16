'''
Left view of binary tree

Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree.
Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side
NOTE: The value comes first in the array which have lower level.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 109

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

 [1, 2, 4, 8]
Output 2:

 [1, 2, 4, 5]
'''

from collections import deque

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# do a level order traversal and append only the first element of the q for each level
class Solution:
    def solve(self, root):
        res = []
        q = deque()
        q.append(root)
        while q:
            s = len(q)
            for i in range(s):
                node = q.popleft()
                if i == 0:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                
        return res
# TC O(n)
# SC O(n)
