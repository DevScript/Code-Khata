#updated Queues implimentation using Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class queue_SL:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
   
    def Pop(self):
        if self.head == None:
            print("---------Nothing left to remove---------")
        else:
            if self.head.next == None:
                del self.head
                self.head = None
            else:
                current_node = self.head
                self.head = current_node.next
                del current_node
                

    def Display(self):
        if self.head == None:
            print("---------Nothing to be displayed---------")
        else:
            temp = self.head
            print("Elements are:", end = " ")
            while temp.next != None:
                print(temp.data, end = " ")
                temp = temp.next
            print(temp.data) #since while loop termminates and it wont print the data in last node
                

lnk_lst = queue_SL()
cnd = True

while cnd:
    print("Menu\n1. Push\n2. Pop\n3. Display\n4. Quit")
    query = int(input("Enter selected option: "))
    if query == 1:
        lnk_lst.push(int(input("Enter data: ")))
    elif query == 2:
        lnk_lst.Pop()
    elif query == 3:
        lnk_lst.Display()
    elif query == 4:
        print("Quitting...")
        cnd = False
    else:
        print("Select a valid option from menu")
