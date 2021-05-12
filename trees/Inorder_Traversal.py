'''
Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes values.
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

 [1, 3, 2]
Output 2:

 [6, 1, 3, 2]
'''

from collections import deque

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# Since we cant use recursion we will take what part of the recursive approach offers - stack
# append all curr nodes in a stack and move to curr.left until curr is null
# if curr is null but the stack is not empty then pop and push the top element in the res array
# do this until curr and stack both reach null
class Solution:
    def inorderTraversal(self, root):
        st = deque()
        curr = root
        res = []
        while curr or st:
            if curr is not None:
                st.append(curr)
                curr = curr.left
            elif st:
                curr = st.pop()
                res.append(curr.val)
                curr = curr.right
        return res
# TC O(n)
# SC O(n)
                
                
                
