'''
Longest Palindromic List

Given a linked list of integers. Find and return the length of the longest palindrome list that exists in that linked list.
A palindrome list is a list that reads the same backward and forward.
Expected memory complexity : O(1)

Problem Constraints
1 <= length of the linked list <= 2000
1 <= Node value <= 100

Example Input
Input 1:

 2 -> 3 -> 3 -> 3
Input 2:

 2 -> 1 -> 2 -> 1 ->  2 -> 2 -> 1 -> 3 -> 2 -> 2


Example Output
Output 1:

 3
Output 2:

 5
'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

# revesre the curr element
# from that element check all the nodes to the left and all the nodes that are on the right side
# do this until pointer reaches null or the palindrome is broken
class Solution:
    # Helper function to compare node vals
    # gives the length of the longest palindrome from a node or a split
    def findPali(self,left,right):
        count = 0
        while left and right:
            if left.val == right.val:
                count += 1
            else:
                return count
            left = left.next
            right = right.next
        return count
    
    def solve(self, head):
        if not head.next:
            return 1
        prev = None
        curr = head
        res = 0 
        while curr:
            next = curr.next
            curr.next = prev
            # for odd
            # plus 1 because we count the curr node too
            res = max(res,2*self.findPali(prev,next)+1)
            # for even
            res = max(res,2*self.findPali(curr,next))
            prev = curr
            curr = next
        return res
# TC O(n^2)
# SC O(1)
            
            
            
