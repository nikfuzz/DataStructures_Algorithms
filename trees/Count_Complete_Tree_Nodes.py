'''
Count Complete Tree Nodes

Given a complete binary tree, A, find the total number of nodes in the tree.

Input 1:

        1
       / \
      2   3

Output 1:
    3

Input 2:

        1
       / \
      2   3
     / \
    4   5

Output 2:
    5
'''

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# a complete tree has all its node with 2 children except for the level just above leaf
# The last level is filled from left to right
# Until we find the last leaf node we can just get the number of nodes with 2**height-1
# To confirm the current sub tree is completely filled we check left and right height, if they are same return 2**height-1
# If they are not same simply count the nodes by adding 1 and calling the function recursively
class Solution:
    def rightHeight(self, root):
        count = 0
        while root:
            count += 1
            root = root.right
        return count
        
    def leftHeight(self, root):
        count = 0
        while root:
            count += 1
            root = root.left
        return count
        
    def solve(self, root):
        if not root: return 0
        l = self.leftHeight(root)
        r = self.rightHeight(root)
        if l == r:
            return ((2**l) -1)
        return 1 + self.solve(root.left) + self.solve(root.right)
# TC O(logn * logn)
# SC O(h)
        