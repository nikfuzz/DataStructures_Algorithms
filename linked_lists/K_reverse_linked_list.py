'''
K reverse linked list

Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return modified linked list.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5, 6]
 B = 2

Input 2:
 A = [1, 2, 3, 4, 5, 6]
 B = 3


Example Output
Output 1:
 [2, 1, 4, 3, 6, 5]

Output 2:
 [3, 2, 1, 6, 5, 4]
'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

# reverse the nodes until count of nodes becomes b
# then append it to recursively called next set of nodes
class Solution:
    def reverse(self,head,b):
        count = 0
        curr = head
        next = None
        prev = None
        # reverse b nodes
        while curr and count < b:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1
        # point head.next to the next window of elements that we need to reverse
        if next:
            head.next = self.reverse(next,b)
        return prev
# tc O(n)
# SC O(n), recursive stack


    def reverseList(self, head, b):
        return self.reverse(head,b)

