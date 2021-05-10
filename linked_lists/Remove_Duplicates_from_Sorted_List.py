'''
Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

Problem Constraints
0 <= length of linked list <= 106

Example Input
Input 1:

 1->1->2
Input 2:

 1->1->2->3->3


Example Output
Output 1:

 1->2
Output 2:

 1->2->3
'''
# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

# keep a curr and a prev pointer
# iterate curr to a node where prev.val != curr.val and do prev.next = curr
class Solution:
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        p = head
        while p:
            prev = p
            p = p.next
            while p and p.val == prev.val:
                p = p.next
            prev.next = p
        return head
# TC O(n)
# SC O(1)

