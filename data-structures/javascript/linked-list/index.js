class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  isEmpty() {
    return this.size === 0;
  }

  getSize() {
    return this.size;
  }

  // O(1) time
  prepend(value) {
    // add a node to the beginnig of the list
    const node = new Node(value);
    if (!this.isEmpty()) {
      node.next = this.head;
    }
    this.head = node;
    this.size++;
  }

  // O(n) time, where n is the size of the list
  append(value) {
    // add a node to the end of the list
    const node = new Node(value);
    if (this.isEmpty()) {
      this.head = node;
    } else {
      // find end
      let prev = this.head;
      while (prev.next) {
        prev = prev.next;
      }
      prev.next = node;
    }

    this.size++;
  }
  
  insert(value, index) {
    if (index < 0 || index > this.size) {
      console.log(`Provided index: ${index} is out of the list boundary;
        current size= ${this.size}`);
      return;
    }

    if (index === 0) {
      this.prepend(value);
      return;
    }

    let prevNode = this.head;
    let currIndex= 1;
    while (currIndex < index) {
      prevNode = prevNode.next;
      currIndex++;
    }
    const newNode = new Node(value);
    newNode.next = prevNode.next;
    prevNode.next = newNode;
    this.size++;
  }

  removeFrom(index) {
    if (index < 0 || index >= this.size) {
      console.log(`Provided index: ${index} is out of the list boundary;
        current size= ${this.size}`);
      return null;
    }
    let removedNode;

    if (index === 0) {
      removedNode = this.head;
      this.head = this.head.next;
    } else {
      let prevNode = this.head;
      let currIndex = 1;
      while (currIndex < index) {
        prevNode = prevNode.next;
        currIndex++;
      }

      removedNode = prevNode.next;
      prevNode.next = removedNode.next;
    }
    this.size--;

    return removedNode.value;
  }

  print() {
    if (this.isEmpty()) {
      console.log("The list is empty");
    } else {
      let current = this.head;
      let listValues = "";
      while (current) {
        listValues += `${current.value} `;
        current = current.next;
      }
      console.log(listValues);
    }

  }
}

// const list = new LinkedList();
// console.log("List is empty: ", list.isEmpty());
// console.log("List size", list.getSize());
// list.print();
// list.prepend(10);
// list.print();
// list.prepend(20);
// list.prepend(30);
// list.print();

// const list = new LinkedList();
// console.log("List is empty: ", list.isEmpty());
// console.log("List size", list.getSize());
// list.print();
// list.append(10);
// list.print();
// list.append(20);
// list.append(30);
// list.print();

const list = new LinkedList();
console.log("List is empty? ", list.isEmpty());
console.log("List size= ", list.getSize());
list.print();

list.insert(10, 0);
list.print();

list.insert(20, 0);
list.print();

list.insert(30, 1);
list.print();

list.insert(40, 2);
list.print();

console.log(list.getSize());

console.log(list.removeFrom(10));
console.log(list.removeFrom(0));
list.print();
console.log(list.removeFrom(1));
list.print();
console.log(list.getSize());