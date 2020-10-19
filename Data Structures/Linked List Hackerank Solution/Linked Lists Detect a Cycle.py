"""
Hackerank solution for Linked Lists: Detect a Cycle
"""
def has_cycle(head):
    c = []
    while head!=None:
        if head.data in c:
            return 1
        else:
            c.append(head.data)
            head = head.next
    return 0
