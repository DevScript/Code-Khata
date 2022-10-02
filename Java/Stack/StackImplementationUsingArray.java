package Stack;
/*A Stack is a linear data structure that follows the LIFO (Last-In-First-Out) principle.*/
public class StackImplementationUsingArray {
    private int maxSize;
    private int stackArray[];
    private int top;

    StackImplementationUsingArray(int size) {
        maxSize = size;
        stackArray = new int[maxSize];
        top = -1;
    }

    public boolean isFull() {
        return (top == maxSize - 1);
    }

    public boolean isEmpty() {
        return (top == -1);
    }

    public void push(int element) {
        if(isFull()) {
            System.out.println("Stack is already full");
        }
        else {
            stackArray[++top] = element;
            //top = top + 1;
            //stackArray[top] = element;
        }
    }

    public int pop() {
        if(isEmpty()) {
            return top;
        }
        else {
            return stackArray[top--];
        }
    }

    public int peek() {
        if(isEmpty()) {
            return top;
        }
        else {
            return stackArray[top];
        }
    }

    public static void main(String[] args) {
        StackImplementationUsingArray s = new StackImplementationUsingArray(10);
        int poppedElement, peekedElement;

        s.push(10);
        s.push(20);
        s.push(30);
        s.push(-10);
        s.push(150);
        s.push(-920);
        s.push(10);

        poppedElement = s.pop();
        System.out.println("Popped Element: " + poppedElement);

        poppedElement = s.pop();
        System.out.println("Popped Element: " + poppedElement);

        poppedElement = s.pop();
        System.out.println("Popped Element: " + poppedElement);

        peekedElement = s.peek();
        System.out.println("Peeked Element: " + peekedElement);

        peekedElement = s.peek();
        System.out.println("Peeked Element: " + peekedElement);

        peekedElement = s.peek();
        System.out.println("Peeked Element: " + peekedElement);

        for(int i = 0; i < 7; i++) {
            s.push(i);
        }

        while(!s.isEmpty()) {
            poppedElement = s.pop();
            System.out.println("Popped Element: " + poppedElement);
        }

        poppedElement = s.pop();
        if(poppedElement == -1) {
            System.out.println("Stack is empty");
        }
        else {
            System.out.println("Popped Element: " + poppedElement);
        }
    }
}
