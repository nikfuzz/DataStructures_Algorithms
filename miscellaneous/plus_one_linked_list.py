# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

class LinkedNode():
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
        

def printList(head):
    ptr = head
    while ptr:
        print(ptr.val)
        ptr = ptr.next
        
def addNode(val, head=None):
    if not head:
        head = LinkedNode(val)
        return head
        
    ptr = head
    
    while ptr.next:
        ptr = ptr.next
        
    ptr.next = LinkedNode(val)
    
    return head
    
def rotateList(head):
    preptr, ptr = None, head
    
    while ptr:
        next = ptr.next
        ptr.next = preptr
        preptr = ptr
        ptr = next
    
    head = preptr
        
    return head
    
def addOne(head):
    ptr = head
    carry = 0
    tail = None
    ptr.val += 1
    carry = ptr.val // 10
    ptr.val = ptr.val % 10
    ptr = ptr.next
    
    while carry and ptr:
        ptr.val += (carry)
        carry = ptr.val // 10
        ptr.val %= 10
        tail = ptr
        ptr = ptr.next
        
    if tail and tail.next == None and carry:
        tail.next = LinkedNode(carry) 
    
    
    return head
    
    
arr = [1,9,1,9]

head = None

for num in arr:
    head = addNode(num, head)
    
head = rotateList(head)
head = addOne(head)
head = rotateList(head)
    
printList(head)

