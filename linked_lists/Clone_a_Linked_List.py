'''
Clone a Linked List

Given a doubly linked list of integers with one pointer of each node pointing to the next node (just like in a single link list) while the second pointer, however, can point to any node in the list and not just the previous node.
You have to create a copy of this list and return the head pointer of the duplicated list.

Problem Constraints
1 <= length of the list <= 100000
1 <= Value of node <= 100000

Example Input
Input 1:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1
Input 2:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1


Example Output
Output 1:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1
Output 2:

1 -> 2 -> 3 -> 4 -> 5
random pointer of each node 
1 -> 5 2 -> 4 3 -> 3 4 -> 2 5 -> 1
'''

# Make a clone of each node(with its random pointer) and place it right next to the original node
# now change random pointer of every alternate node from head.next (our new list) to curr.random.next
# also change the next pointers to point to alternate node
# this will give us two identical lists with different heads

class ListNode: 
    def __init__(self,x):
        self.val = x
        self.next = None
        self.random = None

def clonelist(head):
    if not head.next:
        return ListNode(head.val)
    curr = head
    while curr:
        new_node = ListNode(curr.val)
        new_node.next = curr.next
        new_node.random = curr.random
        curr.next = new_node
        curr = new_node.next
    new_head = head.next
    curr = new_head 
    prev = head
    while curr and prev:
        curr.random = curr.random.next
        prev.next = curr.next
        prev = prev.next
        if curr.next:
            curr = curr.next.next
    return new_head

# TC O(n)
# SC O(n), for the new list. But O(1) aux space

    