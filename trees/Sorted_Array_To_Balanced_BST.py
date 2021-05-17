'''
Sorted Array To Balanced BST

Given an array where elements are sorted in ascending order, convert it to a height Balanced Binary Search Tree (BBST).
Balanced tree : a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node 
never differ by more than 1.

Problem Constraints
1 <= length of array <= 100000

Example Input
Input 1:

 A : [1, 2, 3]
Input 2:

 A : [1, 2, 3, 5, 10]


Example Output
Output 1:

      2
    /   \
   1     3
Output 2:

      3
    /   \
   2     5
  /       \
 1         10
'''

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# the mid of the array will divide the array into 2 parts of the balanced bst
# recursively send limits(start and end) of the arr to calculate mid for each subtree
# the mid becomes the root and m-1 will be the new end point for left subtree
# m+1 becomes the new start point for the right sub tree
# preorder traversal
class Solution:
    def makeBST(self,a,s,e):
        # break when start > end
        if s > e:
            return
        m = (s + e)//2
        new_node = TreeNode(a[m])
        new_node.left = self.makeBST(a,s,m-1)
        new_node.right = self.makeBST(a,m+1,e)
        
        return new_node
        
        
    def sortedArrayToBST(self, a):
        return self.makeBST(a,0,len(a)-1)
# TC O(n)
# SC O(log(n)), the recursive stack space for a balanced tree is log n
