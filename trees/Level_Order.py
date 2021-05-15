'''
Level Order

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

Problem Constraints
1 <= number of nodes <= 105

Example Input
Input 1:

    3
   / \
  9  20
    /  \
   15   7
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [
   [3],
   [9, 20],
   [15, 7]
 ]
Output 2:

 [ 
   [1]
   [6, 2]
   [3]
 ]
'''
from collections import deque
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# add root in queue
# save the size of the queue, s
# when you pop an element from the queue, add its left and right children in the queue 
# and push the popped element in the temp list
# once you iterate through s values append the temp list to the res list and start another temp list
# Keep repeating until q is not null
class Solution:
    def levelOrder(self, root):
        q = deque()
        res = []
        q.append(root)
        while q:
            s = len(q)
            lvl = []
            for i in range(s):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                lvl.append(node.val)
            res.append(lvl)
        return res
# TC O(n)
# SC O(n)