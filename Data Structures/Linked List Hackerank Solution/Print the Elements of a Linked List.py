"""
Hackerrank solution for Print the elements of a linked list
"""
def printLinkedList(head):
    while head is not None:
        print(head.data)
        head = head.next
