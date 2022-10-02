package LinkedList;

public class CircularLinkedList {
    Node head;
    Node tail;
    int size;

    static class Node {
        int data;
        Node next;

        Node(int data) {
            this.data = data;
            next = null;
        }
    }

    private void traverse() {
        if(head == null) {
            System.out.println("Empty List");
        }
        else {
            Node temp = head;
            do {
                System.out.print(temp.data + " ");
                temp = temp.next;
            }
            while(temp != head);
            System.out.println();
        }
    }

    private void deleteStart() {
        if(head == null) {
            System.out.println("Empty List");
        }
        else if(head == tail) {
            tail.next = null;
            head = tail = null;

            size--;
        }
        else {
            Node temp = head;
            head = head.next;
            temp.next = null;
            tail.next = head;

            size--;
        }
    }

    private void deleteAtPosition(int position) {
        if(position < 1 || position > (size + 1)) {
            System.out.println("Invalid position");
        }
        else {
            if(position == 1) {
                deleteStart();
            }
            else if(position == size) {
                deleteEnd();
            }
            else {
                Node temp = head;
                int currentPosition = 1;

                while(currentPosition != (position - 1)) {
                    temp = temp.next;
                    currentPosition++;
                }

                Node delete = temp.next;
                temp.next = delete.next;
                delete.next = null;

                size--;
            }
        }
    }

    private void deleteEnd() {
        if(head == null) {
            System.out.println("Empty List");
        }
        else if(head == tail) {
            tail.next = null;
            head = tail = null;

            size--;
        }
        else {
            Node temp = head;
            int currentPosition = 1;

            while(currentPosition != (size - 1)) {
                temp = temp.next;
                currentPosition++;
            }
            temp.next = head;
            tail.next = null;
            tail = temp;

            size--;
        }
    }

    private void insertAtStart(int data) {
        Node newNode = new Node(data);

        if(head == null) {
            head = newNode;
            head.next = head;
            tail = head;
        }
        else {
            newNode.next = head;
            head = newNode;
            tail.next = head;
        }

        size++;
    }

    private void insertAtPosition(int data, int position) {
        if(position < 1 || position > (size + 1)) {
            System.out.println("Invalid position");
        }
        else {
            if(position == 1) {
                insertAtStart(data);
            }
            else if(position == (size + 1)) {
                insertAtEnd(data);
            }
            else {
                Node temp = head;
                int currentPosition = 1;

                while(currentPosition != (position - 1)) {
                    temp = temp.next;
                    currentPosition++;
                }

                Node newNode = new Node(data);
                newNode.next = temp.next;
                temp.next = newNode;

                size++;
            }
        }
    }

    private void insertAtEnd(int data) {
        Node newNode = new Node(data);

        if(head == null) {
            head = newNode;
            tail = newNode;
            head.next = head;
        }
        else {
            tail.next = newNode;
            tail = newNode;
            tail.next = head;
        }

        size++;
    }

    public static void main(String[] args) {
        CircularLinkedList circularLinkedList= new CircularLinkedList();
// Example
        circularLinkedList.insertAtEnd(1);
        circularLinkedList.insertAtEnd(2);
        circularLinkedList.insertAtEnd(3);
        circularLinkedList.traverse();
        circularLinkedList.insertAtStart(4);
        circularLinkedList.traverse();

        circularLinkedList.insertAtPosition(8, 3);
        circularLinkedList.traverse();

        circularLinkedList.deleteStart();
        circularLinkedList.deleteEnd();
        circularLinkedList.deleteStart();
        circularLinkedList.deleteEnd();
        circularLinkedList.deleteAtPosition(2);
        circularLinkedList.deleteAtPosition(4);
        circularLinkedList.traverse();

    }
}