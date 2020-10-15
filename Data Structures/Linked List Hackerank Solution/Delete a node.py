"""
Hackerrank solution for delete a node in python
"""
def deleteNode(head, position):
    if position==0:
        return head.next
    else:
        temp = head
        count = 1
        while temp.next != None:
            if count==position:
                temp.next=temp.next.next  
                break  
            temp = temp.next
            count+=1
    return head   
