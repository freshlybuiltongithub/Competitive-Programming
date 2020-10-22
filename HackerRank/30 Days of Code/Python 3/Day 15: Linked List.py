"""
Hackerrank Solution for Day 15: Linked List
"""
    def insert(self,head,data): 
        #Complete this method
        
        new_node = Node(data)
        if head == None:
            return new_node
        else:
            current  = head
            while current.next != None:
                current = current.next
            current.next = new_node
            return head 

        


