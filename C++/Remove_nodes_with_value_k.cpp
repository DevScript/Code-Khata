Node *removeNodes(Node *head, int k) {
    // Write your code here.
    while(head ->next !=NULL)
        if(k ==head->data)
            head = head->next;
    else break;
    if(head->data==k)
        return NULL;

    Node *temp = head->next, *prev = head;
    while(temp !=NULL){
        if(temp ->data==k){
            prev->next = temp->next;
            temp = temp->next;
        }
    else
    {
        prev = temp;
        temp = temp->next;
    }
}
    return head;
}
