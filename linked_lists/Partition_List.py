'''
Partition List

Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or equal to B.
You should preserve the original relative order of the nodes in each of the two partitions.

Problem Constraints
1 <= |A| <= 106
1 <= A[i], B <= 109

Example Input
Input 1:

A = [1, 4, 3, 2, 5, 2]
B = 3
Input 2:

A = [1, 2, 3, 1, 3]
B = 2


Example Output
Output 1:

[1, 2, 2, 4, 3, 5]
Output 2:

[1, 1, 2, 3, 3]
'''

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # find the first node which has val less than b
    # traverse the list with two pointers
    # p1 will inc when there's a val less than b else p2
    # finally the last p1 will point to the beginning of p2 and last p2 will point to null
    def partition(self, head, b):
        if not head or not head.next:
            return head
        head1 = None
        ptr = head
        while ptr and (not head1):
            if ptr.val<	b and not head1:
                head1 = ptr
            ptr = ptr.next
        # return head if there is no node.val < b
        if not head1:
            return head
        dummy = head1
        dummy2 = ListNode(-2)
        ptr1 = dummy
        ptr2 = dummy2
        curr = head
        while curr:
            if curr.val < b and head1 != curr:
                ptr1.next =  curr
                ptr1 = curr
            elif curr.val >= b:
                ptr2.next = curr
                ptr2 = curr
            curr = curr.next
        ptr2.next = None
        ptr1.next = dummy2.next
        return dummy
# TC O(n)
# SC O(1)

