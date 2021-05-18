'''
Floor and Ceil in BST

Given a Binary Search Tree rooted at A.
Given an integer array B of size N. Find the floor and ceil of every element of the array B.
Floor(X) is the highest element in the tree <= X, while the ceil(X) is the lowest element in the tree >= X.
NOTE: If floor or ceil of any element of B doesn't exists, output -1 for the value which doesn't exists.

Problem Constraints
0 <= Number of nodes in the tree <= 1000000
0 <= node values <= 109
0 <= N <= 100000
0 <= B[i] <= 109

Example Input
Input 1:

Given Tree A:
           10
         /    \
        4      15
       / \
      1   8
B = [4, 19]
Input 2:

Given Tree A:
            8
          /   \
         5     19
        / \     \
       4   7     100
B = [1, 11]       


Example Output
Output 1:

[
    [4, 4]
    [15, -1]
]
Output 2:

[
    [-1, 4]
    [8, 19]
]
'''

# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

# to find floor we need to store ans every time we find a root.val<num and move to root.right or we will directly 
# return num if num == root.val
# For ceil we follow opp. logic. We store the ans for root.val>num and move to root.left or we directly return root.val...
# if root.val == num
class Solution:
    def findFloor(self, root, num, ans):
        if not root: return ans
        if root.val == num:
            return root.val
        elif root.val < num:
            ans = root.val
            return self.findFloor(root.right, num, ans)
        else:
            return self.findFloor(root.left, num, ans)
    
    def findCeil(self, root, num, ans):
        if not root: return ans
        if root.val == num:
            return root.val
        elif root.val > num:
            ans = root.val
            return self.findCeil(root.left, num, ans)
        else:
            return self.findCeil(root.right, num, ans)
    
    
    def solve(self, root, b):
        res = []
        for i in range(len(b)):
            floor = self.findFloor(root, b[i], -1)
            ceil = self.findCeil(root, b[i], -1)
            res.append(list([floor,ceil]))
        return res
# TC O(n)
# SC O(h), h = height of the tree
