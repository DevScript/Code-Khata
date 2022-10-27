Node *removeDuplicates(Node *head)
{
   if (head== NULL)
   {
       return NULL;
   }
   Node* curr= head, *prev= NULL;
   map<int, bool>visited;
   while (curr!= NULL)
   {
       if (visited[curr->data]== true)
       {
           Node* target= curr;
           prev->next= curr->next;
           curr= curr->next;
           target->next= NULL;
           delete (target);
       }
       else
       {
       visited[curr->data]= true;
       prev= curr;
       curr= curr->next;
       }
   }
   return head;
}
