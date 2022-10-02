package Stack;

import java.util.Stack;

public class StackImplementationUsingStackClass {
    static void pushInStack(Stack<Integer> stack) {
        for(int i = 0; i < 5; i++) {
            stack.push(i);
        }

        stack.push(100);
        stack.push(123);
    }

    static void popFromStack(Stack<Integer> stack) {
        for(int i = 0; i < 5; i++) {
            Integer poppedValue = stack.pop();
            System.out.print(poppedValue + " ");
        }
    }

    static void peekInStack(Stack<Integer> stack) {
        for(int i = 0; i < 3; i++) {
            Integer peekedValue = stack.peek();
            System.out.print(peekedValue + " ");
        }
    }

    static void checkIfStackIsExpty(Stack<Integer> stack) {
        boolean isStackEmpty = stack.isEmpty();
        System.out.println("Is Stack empty?: " + isStackEmpty);
    }

    static void searchInStack(Stack<Integer> stack, Integer element) {
        int indexOfSearchedElement = stack.search(element);
        System.out.println("Element " + element + " is present in index: " + indexOfSearchedElement);
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<Integer>();

        System.out.println("Pushing in stack");
        pushInStack(stack);
        System.out.println("Current stack: ");
        System.out.println(stack);

        System.out.println("Popping from stack: ");
        popFromStack(stack);
        System.out.println();
        System.out.println("Current stack: ");
        System.out.println(stack);

        System.out.println("Peeking in stack: ");
        peekInStack(stack);
        System.out.println();
        System.out.println("Current stack: ");
        System.out.println(stack);

        checkIfStackIsExpty(stack);

        searchInStack(stack, 0);
        searchInStack(stack, 1);
        searchInStack(stack, 2);

        stack.pop();
        System.out.println("Current stack: ");
        System.out.println(stack);
        checkIfStackIsExpty(stack);
        stack.pop();
        System.out.println("Current stack: ");
        System.out.println(stack);
        checkIfStackIsExpty(stack);

        stack.add(8);
        stack.add(80);
        stack.add(18);
        stack.add(38);
        System.out.println("Current stack: ");
        System.out.println(stack);
        stack.add(1, 30);
        System.out.println("Current stack: ");
        System.out.println(stack);
        stack.add(3, 30);
        System.out.println("Current stack: ");
        System.out.println(stack);
    }
}
