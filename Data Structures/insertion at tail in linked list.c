SinglyLinkedListNode* insertNodeAtTail(SinglyLinkedListNode* head, int data) {
    SinglyLinkedListNode* temp;
    SinglyLinkedListNode* new=(SinglyLinkedListNode*)malloc(sizeof(SinglyLinkedListNode));
    new->data=data;
    new->next=NULL;
    temp=head;
    if(temp==NULL)
    {
        head=new;
    }
    else
    while(temp!=NULL)
    {
        
        if(temp->next==NULL)
        {
           temp->next=new;
           break;
        }
        else 
           temp=temp->next;
    }
return head;
}   
