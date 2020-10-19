"""
Hackerrank Solution for Find Merge Point of Two Lists
"""
def findMergeNode(head1, head2):
    def getcount(head):
        count = 0
        while head.next != None:
            head = head.next
            count+=1
        return count
    c1 = getcount(head1)
    c2 = getcount(head2)
    def getmerge(d,head1,head2):
        for i in range(d):
            head1 = head1.next

        while head1 and head2:
            if head1 == head2:
                return head1.data
            else:
                head1 = head1.next
                head2 = head2.next
    
    if c1>c2:
        return getmerge(c1-c2,head1,head2)
    else:
        return getmerge(c2-c1,head2,head1)
    
