"""
Hackerrank solution for Reverse a doubly linked list
"""
def reverse(head):

    while head.next != None:
        head.prev,head.next,head = head.next,head.prev,head.next
    head.next,head.prev = head.prev,None
    
    return head
