'''
Postorder Traversal

Given a binary tree, return the Postorder traversal of its nodes values.
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

 [3, 2, 1]
Output 2:

 [6, 3, 2, 1]
'''
from collections import deque

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# add all the left elements in stack until curr reaches null
# if the curr is null and root of curr has no remaining right children then we keep popping and 
# adding stack[-1] to our res array
# But if the curr is null and its root does have a right child then set curr = stack[-1].right
class Solution:
    def postorderTraversal(self, root):
        curr = root
        stack = deque()
        res = []
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                temp = stack[-1].right
                if not temp:
                    temp = stack.pop()
                    res.append(temp.val)
                    while stack and temp == stack[-1].right:
                        temp = stack.pop()
                        res.append(temp.val)
                else:
                    curr = temp
        return res
# TC O(n)
# SC O(n)

