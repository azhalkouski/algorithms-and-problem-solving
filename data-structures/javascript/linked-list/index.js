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

const list = new LinkedList();
// console.log("List is empty: ", list.isEmpty());
// console.log("List size", list.getSize());
// list.print();
// list.prepend(10);
// list.print();
// list.prepend(20);
// list.prepend(30);
// list.print();

console.log("List is empty: ", list.isEmpty());
console.log("List size", list.getSize());
list.print();
list.append(10);
list.print();
list.append(20);
list.append(30);
list.print();