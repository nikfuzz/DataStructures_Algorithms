'''
Add Two Numbers

You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Constraints:
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # put the lists in str. add the numbers. Put it in a list and reverse it. Create a linkedlist and return
    def addTwoNumbers(self, l1, l2):
        ptr = l1
        s1 = ''
        s2 = ''
        while ptr != None:
            s1 += str(ptr.val)
            ptr = ptr.next
        ptr = l2
        while ptr != None:
            s2 += str(ptr.val)
            ptr = ptr.next
        s1 = s1[::-1]
        s2 = s2[::-1]
        
        ans = int(s1) + int(s2)
        
        res = [int(x) for x in str(ans)]
        res.reverse()
        
        ans_list = ListNode(res[0])
        
        ptr = ans_list
        for i in range(1, len(res)):
            node = ListNode(res[i])
            ptr.next = node
            ptr = ptr.next
        
        return ans_list