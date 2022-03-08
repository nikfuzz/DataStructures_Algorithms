'''
Maximum Sum BST in Binary Tree

Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

Assume a BST is defined as follows:

1. The left subtree of a node contains only nodes with keys less than the node's key.
2. The right subtree of a node contains only nodes with keys greater than the node's key.
3. Both the left and right subtrees must also be binary search trees.

Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
Output: 20
Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3

Input: root = [4,3,null,1,2]
Output: 2
Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

Input: root = [-4,-2,-5]
Output: 0
Explanation: All values are negatives. Return an empty BST.

Constraints:

1. The number of nodes in the tree is in the range [1, 4 * 104].
2. -4 * 104 <= Node.val <= 4 * 104
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxSumBST(self, root) -> int:
        self.max = 0
        
        def getMaxSumBst(root):
            
            if not root:
                return (-float('inf'), float('inf'), 0, True)
            
            l_max, l_min, l_sum, l_bst = getMaxSumBst(root.left)
            r_max, r_min, r_sum, r_bst = getMaxSumBst(root.right)
            
            is_bst = l_bst and r_bst and (root.val > l_max and root.val < r_min)
            
            sub_sum = root.val
            
            if is_bst:
                sub_sum = l_sum + r_sum + root.val
                self.max = max(self.max, sub_sum)
                
            return (max(l_max, r_max, root.val), min(l_min, r_min, root.val), sub_sum, is_bst)
        
        getMaxSumBst(root)
        
        return self.max

# TC O(n), n = number of nodes
# SC O(n), n = number of nodes
            
        
        
        