'''
Good Graph

Given a directed graph of N nodes where each node is pointing to exactly one of the N nodes (can possibly point to itself). Ishu, the coder, is bored and he has discovered a problem out of it to keep himself busy. Problem is as follows:

A node is 'good' if it satisfies one of the following:
1. It is the special node (marked as node 1)
2. It is pointing to the special node (node 1)
3. It is pointing to a good node.
Ishu is going to change pointers of some nodes to make them all 'good'. You have to find the minimum number of pointers to change in order to make all the nodes good (Thus, a Good Graph).
NOTE: Resultant Graph should hold the property that all nodes are good and each node must point to exactly one node.

Problem Constraints
1 <= N <= 10^5

Example Input
Input 1:

 [1, 2, 1, 2]
Input 2:

 [3, 1, 3, 1]


Example Output
Output 1:

 1
Output 2:

 1
'''
# Assign color to the connected components
# Run a while loop to assign the current color until we reach a visited node
# After we reach a visited node we need to check if the next node is of the same color
# If next is colored with the current color and it is not a good node that is not index 0 then we can count it in our answer
class Solution:
    def solve(self, a):
        ans = 0
        vis = set()
        color = [-1]*len(a)
        c = 0
        for i in range(len(a)):
            if i not in vis:
                curr = i
                vis.add(i)
                next = a[curr]-1
                color[curr] = c
                while next not in vis:
                    vis.add(next)
                    color[next] = c
                    curr = next
                    next = a[curr]-1
                if color[next] == c and next != 0:
                    ans += 1
                c += 1
        return ans
# TC O(V + E)
# SC O(V)