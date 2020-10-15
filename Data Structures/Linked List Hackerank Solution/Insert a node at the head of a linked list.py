"""
hackerrank function for inserting a node at the head of linked list
"""
def insertNodeAtHead(llist, data):
    # Write your code here
    node = SinglyLinkedListNode(data)
    node.data = data
    node.next = llist
    return node
