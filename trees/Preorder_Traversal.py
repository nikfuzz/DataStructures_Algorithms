'''
Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes values.
NOTE: Using recursion is not allowed.

Problem Constraints
1 <= number of nodes <= 105

Example Input
Input 1:

   1
    \
     2
    /
   3
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [1, 2, 3]
Output 2:

 [1, 6, 2, 3]
'''

from collections import deque

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
    # Since we cant use recursion we will take what part of the recursive approach offers - stack
    # if curr is not null append curr in res and stack and move to curr.left
    # if curr is null then we pop from stack and go to previous node's right sub tree
    def preorderTraversal(self, root):
        stack = deque()
        curr = root
        res = []
        while curr or stack:
            if curr:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
                
            elif stack:
                curr = stack.pop()
                curr = curr.right
        return res
# TC O(n)
# SC O(1) aux space, res space is O(n)

