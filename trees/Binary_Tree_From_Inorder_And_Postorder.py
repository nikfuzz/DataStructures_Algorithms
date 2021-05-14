'''
Binary Tree From Inorder And Postorder

Given inorder and postorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.

Problem Constraints
1 <= number of nodes <= 105

Example Input
Input 1:

 A = [2, 1, 3]
 B = [2, 3, 1]
Input 2:

 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]


Example Output
Output 1:

   1
  / \
 2   3
Output 2:

   1  
  / \
 6   2
    /
   3
'''

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# first make a map of all inorder elements with their indexes
# We know that last element of post order will give us the curr root
# all the elements to the left of root in inorder will give us left subtree and right side will give us right subtree
# LEFT SUBTREE IN POSTORDER --- to get all the left sub tree elements in postorder we range from starting index of postorder to 
# starting + the number of elements - 1 left of root in inorder
# RIGHT SUBTREE IN POSTORDER --- to get right subtree in post we start from starting + the number of elements to end -1
# for inorder take all the elements to the left and right as left subtree and right subtree respectively
class Solution:
    map = {}
    def createTree(self,inor, s1, e1, postor, s2, e2):
        if s1 > e1 or s2 > e2:
            return
        root = TreeNode(postor[e2])
        if not root:
            return
        pos = self.map[postor[e2]]
        noe = pos - s1
        root.left = self.createTree(inor, s1, pos-1, postor, s2, s2+noe-1)
        root.right = self.createTree(inor, pos+1, e1, postor, s2+noe, e2-1)
        return root

    def buildTree(self, inor, postor):
        self.map = {}
        for i in range(len(inor)):
            self.map[inor[i]] = i
        return self.createTree(inor,0,len(inor)-1,postor,0,len(postor)-1)
# TC O(n)
# SC O(n)
        
