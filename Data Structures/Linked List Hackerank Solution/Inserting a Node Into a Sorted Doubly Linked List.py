"""
Hackerrank solution for Inserting a Node Into a Sorted Doubly Linked List
"""
def sortedInsert(head, data):
    #create new node
    node = DoublyLinkedListNode(data)

    if head is None:
        head = node
    #insert before head
    elif data<head.data:
        node.next = head
        head.prev = node
        head = node
    #case 3 insert at specific position
    else:
        cur = head
        # traverse to the specific position
        while cur.next is not None and cur.data<data:
            cur = cur.next
        #insert at the end
        if cur.next == None and cur.data < data:
            cur.next = node
            node.prev = cur
        #insert at specific position
        else:
            previous = cur.prev
            #make changes for previous node
            previous.next = node
            node.prev = previous
            #make changes for current node
            node.next = cur
            cur.prev = node

    return head
