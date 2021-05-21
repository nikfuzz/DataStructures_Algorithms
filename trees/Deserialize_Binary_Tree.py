'''
Deserialize Binary Tree

Given an integer array A denoting the Level Order Traversal of the Binary Tree.
You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.
NOTE:
In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.

Problem Constraints
1 <= number of nodes <= 105
-1 <= A[i] <= 105

Example Input
Input 1:

 A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
Input 2:

 A = [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]


Example Output
Output 1:

           1
         /   \
        2     3
       / \
      4   5
Output 2:

            1
          /   \
         2     3
        / \     \
       4   5     6
'''

from collections import deque
import sys
sys.setrecursionlimit(10**6)
# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# The array will be in the level order form
# The first element is the root and next one is left child and the one after that is the right child
# we need to pop an element from queue as the root node and assign i as its left and i+1 as its right child
# if the root is none we move to the next element in the list
# if left or right val is -1 then assign null to that child of the root
class Solution:
    def solve(self, a):
        root = TreeNode(a[0])
        q = deque()
        q.append(root)
        i = 1
        while q and i<len(a):
            curr = q.popleft()
            if not curr:
                continue
            left = a[i]
            right = a[i+1]
            i += 2
            if left == -1:
                curr.left = None
            else:
                curr.left = TreeNode(left)
            if right == -1:
                curr.right = None
            else:
                curr.right = TreeNode(right)
            q.append(curr.left)
            q.append(curr.right)
        return root
# TC O(n)
# SC O(n)
