// Creating a node
class Node {
  constructor(name, length, path) {
    this.musicNode = {
      name: name,
      length: length,
      path: path,
    };
    this.prev = null;
    this.next = null;
  }
}

// creating double liked list obj and pointer
class DoubllyLinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.length = 0;
    this.tempPos = null;
  }

  // add node to DLL
  add(name, length, path) {
    const newNode = new Node(name, length, path);
    if (this.length === 0) {
      this.head = newNode;
      this.tail = newNode;
    } else {
      this.tail.next = newNode;
      newNode.prev = this.tail;
      this.tail = newNode;
    }
    this.length++;
  }
  remove(name) {
    if (this.length === 0) {
       return;
    }
    let currNode = this.head;
    if (this.head.name == name){
       this.head = this.head.next;
       this.head.prev = null;
       this.length--;
   
      }
    else if (this.tail.name == name) {
       this.tail = this.tail.prev;
       this.tail.next = null;
       this.length--;
   
    }
    else {
      /* while (currNode.next.name != name || currNode.next != null) {
          currNode = currNode.next;
       } */
       currNode.next = currNode.next.next;
       currNode.next.prev = currNode;
    }
    return currNode;
 }
  // set position of current node
  // default is pointer of head node
  setDefaulltPointer() {
    this.tempPos = this.head;
  }

  // traverse DLL and return music obj
  traverse(direction) {
    // forward direction
    if (direction === 1 && this.tempPos.next != null) {
      this.tempPos = this.tempPos.next;
      return this.tempPos.musicNode;
    } else if (direction === -1 && this.tempPos.prev != null) {
      //backward direction
      this.tempPos = this.tempPos.prev;
      return this.tempPos.musicNode;
    } else {
      return 0;
    }
  }

  // check for position of node
  nodePosition() {
    if (this.tempPos.next == null) {
      return -1; // last pos
    } else if (this.tempPos.prev == null) {
      return 1; // first pos
    } else {
      return 0; // middle pos
    }
  }
}

// inserting music in double linked list
const dll = new DoubllyLinkedList();
dll.add(
  "Karam Mangta Hon",
  1,
  "js\\1.mp3"
);
dll.add(
  "Confirm Jannati Hai",
  2,
  "js\\2.mp3"
);
dll.add(
  "Ya Rasool Allah",
  3,
  "js\\3.mpeg"
);
dll.add(
  "Mustafa Jane Rehmat Pe Lakhon Salam",
  4,
  "js\\4.mpeg"
);
dll.add(
  "Ali Ali  Dam Ali ALi",
  5,
  "js\\5.mpeg"
);
dll.add(
  "Mere Huzoor Per Salam",
  6,
  "js\\6.mpeg"
);
//dll.remove("Confirm Jannati Hai");
dll.setDefaulltPointer();
