'''
Serialize Binary Tree

Given the root node of a Binary Tree denoted by A. You have to Serialize the given Binary Tree in the described format.
Serialize means encode it into a integer array denoting the Level Order Traversal of the given Binary Tree.

NOTE:
In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.

Problem Constraints
1 <= number of nodes <= 105

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

 [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
Output 2:

 [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]
'''

from collections import deque

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# Do a level order traversal
# if left child or right child is none add -1 to the queue
class Solution:
    def solve(self, root):
        q = deque()
        res = []
        q.append(root)
        while q:
            s = len(q)
            for i in range(s):
                node = q.popleft()
                # if val == -1 then we just add it into the res and we know there is no right or left subtree so
                # continue after that
                if node.val == -1:
                    res.append(node.val)
                    continue
                if node.left:
                    q.append(node.left)
                else:
                    q.append(TreeNode(-1))
                if node.right:
                    q.append(node.right)
                else:
                    q.append(TreeNode(-1))
                res.append(node.val)
        return res
# TC O(n)
# SC O(n)
            
