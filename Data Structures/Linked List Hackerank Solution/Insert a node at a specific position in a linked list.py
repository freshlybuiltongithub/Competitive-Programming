"""
Hackerrank Solution for Insert a node at a specific position in a linked list
"""
def insertNodeAtPosition(head, data, position):
    #create new node
    node = SinglyLinkedListNode(data)

    if head is None:
        head = node
    else:
        temp = head 
        count = 1
        while temp is not None and count<position:
            temp = temp.next
            count += 1

    node.next = temp.next
    temp.next = node

    return head
