package LinkedList;

public class DoublyLinkedList {
    Node head;
    Node tail;
    int size;

    static class Node {
        int data;
        Node previous;
        Node next;

        Node(int data) {
            this.data = data;
            previous = next = null;
        }
    }

    private void traverse() {
        if(head == null) {
            System.out.println("Linked List is empty");
        }
        else {
            Node temp = head;
            while(temp != null) {
                System.out.print(temp.data + " ");
                temp = temp.next;
            }
            System.out.println();
        }
    }

    private void deleteStart() {
        if(head == null) {
            System.out.println("Can't delete, as Linked List is empty");
        }
        else if(head.next == null) {
            head = null;
            tail = null;

            size--;
        }
        else {
            Node temp = head;
            head = temp.next;
            temp.next = null;
            head.previous = null;

            size--;
        }
    }

    private void deleteAtPosition(int position) {
        if(position < 1 || position > size) {
            System.out.println("Invalid position: " + position);
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
                delete.next.previous = temp;
                delete.previous = null;
                delete.next = null;

                size--;
            }
        }
    }

    private void deleteEnd() {
        if(head == null) {
            System.out.println("Can't delete, as Linked List is empty");
        }
        else if(head.next == null) {
            head = null;
            tail = null;

            size--;
        }
        else {
            Node temp = tail.previous;
            temp.next = null;
            tail.previous = null;
            tail = temp;

            size--;
        }
    }

    private void insertAtStart(int data) {
        Node newNode = new Node(data);

        if(head == null) {
            tail = newNode;
        }
        else {
            newNode.next = head;
            head.previous = newNode;
        }
        head = newNode;

        size++;
    }

    private void insertAtPosition(int position, int data) {
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
                    currentPosition++;
                    temp = temp.next;
                }

                Node newNode = new Node(data);
                newNode.next = temp.next;
                newNode.previous = temp;
                temp.next = newNode;
                newNode.next.previous = newNode;

                size++;
            }
        }
    }

    private void insertAtEnd(int data) {
        Node newNode = new Node(data);

        if(head == null) {
            head = newNode;
        }
        else {
            tail.next = newNode;
            newNode.previous = tail;
        }
        tail = newNode;

        size++;
    }

    public static void main(String[] args) {
        DoublyLinkedList doublyLinkedList= new DoublyLinkedList();
// Example
        doublyLinkedList.insertAtStart(0);
        doublyLinkedList.insertAtStart(-1);
        doublyLinkedList.insertAtEnd(1);
        doublyLinkedList.insertAtEnd(2);
        doublyLinkedList.insertAtPosition(1, -2);
        doublyLinkedList.traverse();
        doublyLinkedList.deleteAtPosition(10);
        doublyLinkedList.traverse();
    }
}