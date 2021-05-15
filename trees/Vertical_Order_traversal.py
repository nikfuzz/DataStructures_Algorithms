'''
Vertical Order traversal

Given a binary tree, return a 2-D array with vertical order traversal of it.
NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.

Problem Constraints
0 <= number of nodes <= 105

Example Input
Input 1:

      6
    /   \
   3     7
  / \     \
 2   5     9
Input 2:

      1
    /   \
   3     7
  /       \
 2         9


Example Output
Output 1:

 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]
Output 2:

 [
    [2],
    [3],
    [1],
    [7],
    [9]
 ]
'''

# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

# We need to make a map => <distance_from_center,[(depth,root.val)]>
# first we sort based on distance from center
# then within that list we sort based on depth
class Solution:
    def sortDistanceWise(self,root,d,lvl,map):
        if not root: return
        if d not in map:
            map[d] = list([tuple([lvl,root.val])])
        else:
            map[d].append(tuple([lvl,root.val]))
        self.sortDistanceWise(root.left,d-1,lvl+1,map)
        self.sortDistanceWise(root.right,d+1,lvl+1,map)
        return
	
    def verticalOrderTraversal(self, root):
        map = {}
        self.sortDistanceWise(root,0,0,map)
        for i in map.values():
            i.sort(key=lambda x:x[0])
        if not map: return []
        mi = min(map)
        ma = max(map)
        res = []
        for i in range(mi,ma+1):
            j = map[i]
            lis = []
            for x in j:
                lis.append(x[1])
            res.append(lis)
        return res
# TC O(n)
# SC O(n)
