'''
BST nodes in a range

Given a binary search tree of integers. You are given a range B and C.
Return the count of the number of nodes that lies in the given range.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= B < = C <= 109

Example Input
Input 1:

            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 12
     C = 20
Input 2:

            8
           / \
          6  21
         / \
        1   4

     B = 2
     C = 20


Example Output
Output 1:

 5
Output 2:

 3
'''

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
# if node is in range then add 1 + result from left and right subtrees
# if the node is less than lower limit then dont count that node and move to the right child 
# else move to the left child
class Solution:
    def solve(self, root, b, c):
        if not root: return 0
        if root.val >= b and root.val <= c:
            return 1 + self.solve(root.left, b, c) + self.solve(root.right, b, c)
        elif root.val < b:
            return self.solve(root.right, b, c)
        else:
            return self.solve(root.left, b, c)
        return 0
# TC O(n)
# SC O(H), H is the height of the tree and can range between logn to n
