"""
Hackkerrank Solution for Insertion of node at the tail of Linked List
"""
def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)

    if (head == None):
        head = node
    else:
        current = head
        while (current.next != None):
            current = current.next
        current.next = node
    return head
