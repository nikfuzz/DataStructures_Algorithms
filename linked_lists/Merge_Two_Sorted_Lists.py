'''
Merge Two Sorted Lists

Merge two sorted linked lists A and B and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

Problem Constraints
0 <= |A|, |B| <= 105

Example Input
Input 1:

 A = 5 -> 8 -> 20
 B = 4 -> 11 -> 15
Input 2:

 A = 1 -> 2 -> 3
 B = Null


Example Output
Output 1:

 4 -> 5 -> 8 -> 11 -> 15 -> 20
Output 2:

 1 -> 2 -> 3
'''

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# similar to merge function in merge sort
# iterate p1 and p2 and compare val of nodes, put the suitable node as t.next
# if one of them becomes reaches null then iterate the other remaining list and add elements in order
class Solution:
    def mergeTwoLists(self, head1, head2):
        p1 = head1
        p2 = head2
        
        dummy = ListNode(0)
        t = dummy
        
        while p1 and p2:
            if p1.val < p2.val:
                t.next = p1
                p1 = p1.next
            else:
                t.next = p2
                p2 = p2.next
            t = t.next
        while p1:
            t.next = p1
            t = t.next
            p1 = p1.next
        while p2:
            t.next = p2
            t = t.next
            p2 = p2.next
        return dummy.next
# TC O(n)
# SC O(1)

