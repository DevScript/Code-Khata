interface LinkedListQueue{
    public void addlast(Object obj);
  //  public void addFront(Object obj);
    public Object first();
    public Object remove();
    public Object removeLast();
    public int size();
    
}

public class Deque implements LinkedListQueue{
    Node head=new Node();
    int size;

    public class Node {
        Object data;
        Node next;
        Node prev;

        Node(){} 
        Node(Object data){
            this.data=data;
        }
        Node(Object data,Node next,Node prev){
           this.data=data;
           this.next=next;
           this.prev=prev;
        }
   }
    

@Override           
public void addlast(Object data) {
 if (this.head.next==null) {
   head.next=new Node(data);
   head.prev=head.next;
   ++size;  
     System.out.println(data+" added");
 }
 else{
     head.prev=head.prev.next=new Node(data,head,head.prev);
     ++size;
     System.out.println(data+" added");
 }
}


@Override
public Object first() {
  if (head.next==null) {
      throw new IllegalStateException("Queue is empty");
  } else {
      return head.next.data;

  }  
}
@Override
public Object remove() {
    if (head.next==null) {
        throw new IllegalStateException("Queue is empty");
    } else {
        head.next=head.next.next;
        --size;
    }  
    return head.next.data;
  }
  @Override
  public Object removeLast() {
    if (head.next==null) {
        throw new IllegalStateException("Queue is empty");
    } else {
        head.prev=head.prev.prev;
        --size;
    }  
    return head.next.data;
  }
  @Override
  public int size() {
    if (head.next==null) {
        throw new IllegalStateException("Queue is empty");
    } else {
        return size;
    }  
  }
  
  public String toString() {
      String str="";
    if (head.next==null) 
        throw new IllegalStateException("Queue is empty");
        
    
    else{
          //String str="";
    for (Node i = head.next; i != head.prev.next; i=i.next) {
       str+=i.data+", ";
    }
    }
    return str;
}
public boolean search(Object obj) {
    if (head.next==null) 
        {
            throw new IllegalStateException("Queue is empty");
            
        }
    else{
         
    for (Node i = head.next; i != head.prev.next; i=i.next) {
        if (obj==i.data) {
           return true;
        }
    }
    return false;
    }
}
public Queue reverse() {
    Queue q2=new Queue();
    for (Node i =head.prev; i!=head.next; i=i.prev) {
        q2.add(i.data);
    }
    return q2;
}
public Queue merge(Queue q1,Queue q2) {
    q1.head.prev.next=q2.head.next;
    q2.head.prev=q1.head.prev;
    q1.head.prev=q2.head.prev;

    return q1;
    
}
public boolean isEquals(Deque q2) {
   Node i=this.head;
   Node j=q2.head;
    while (this.head.prev!=null) {
       if (i.next.data!=j.next.data) {
           return false;
       }
       i=i.next;
       j=j.next;

   }
   return true;
}
public void removeBottom(){
    // for (Node i = this.head; i.prev.next !=null; i=i.next) {
        
    // }
        this.head.prev=head.prev.prev;
}
  public static void main(String[] args) {
      Queue que=new Queue();
      System.out.println();
      que.add(2);
      que.add(3);
      que.add(4);
      que.add(5);
    
    //   Queue que2=new Queue();
    //   System.out.println();
    //   que2.add(2);
    //   que2.add(3);
    //   que2.add(4);
    //   que2.add(5);
     }
}
