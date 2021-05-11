'''
Add Two Numbers as Lists

You are given two linked lists, A and B representing two non-negative numbers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

Problem Constraints
1 <= |A|, |B| <= 105

Example Input
Input 1:
 A = [2, 4, 3]
 B = [5, 6, 4]

Input 2:
 A = [9, 9]
 B = [1]


Example Output
Output 1:
 [7, 0, 8]

Output 2:
 [0, 0, 1]
'''

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

# start p1 from list 1 and p2 from list 2
# add p1.val + p2.val + carry and store it in a new node
# if p1 or p2 becomes null then keep adding 0 for that list's element until both of them become null
# then keep adding digits from remaining carry to the new list
class Solution:
    def addTwoNumbers(self, head1, head2):
        p1 = head1
        p2 = head2
        
        carry = 0
        dummy = ListNode(-1)
        prev = dummy
        while p1 or p2:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            
            x = x + y + carry
            new_node = ListNode(x%10)
            prev.next = new_node
            prev = new_node
            carry = x//10
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
        while carry:
            new_node = ListNode(carry%10)
            prev.next = new_node
            prev = new_node
            carry = carry//10
        return dummy.next
# TC O(n) n is max(len(list1),len(list2))
# SC O(n), but O(1) aux space
