class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
    this.size = 0;
  }

  isEmpty() {
    return this.size === 0;
  }

  getSize() {
    return this.size;
  }

  print() {
    if (this.isEmpty()) {
      console.log('List is empty');
    } else {
      let curr = this.head;
      let listValues = '';
      while (curr) {
        listValues += `${curr.value} `;
        curr = curr.next;
      }
      console.log(listValues);
    }
  }

  // O(1) time
  prepend(value) {
    const node = new Node(value);
    if (this.isEmpty()) {
      this.head = node;
      this.tail = node;
    } else {
      node.next = this.head;
      this.head = node;
    }
    this.size++;
  }

  // O(1) time
  append(value) {
    const node = new Node(value);
    if (this.isEmpty()) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.size++;
  }

  // O(1) time
  removeFromFront() {
    if (this.isEmpty()) {
      return null;
    }

    const value = this.head.value;
    if (this.getSize() === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = this.head.next;
    }

    this.size--;
    return value;
  }

  // O(n) time
  removeFromEnd() {
    if (this.isEmpty()) {
      return null;
    }

    const value = this.tail.value;
    if (this.getSize() === 1) {
      this.head = null;
      this.tail = null;
    } else {
      let prev = this.head;
      while (prev.next !== this.tail) {
        prev = prev.next;
      }
      prev.next = null;
      this.tail = prev;
    }

    this.size--;
    return value;
  }
}

const list = new LinkedList();

console.log('List is empty? ', list.isEmpty());
console.log('List size ', list.getSize());
list.print();

list.append(1);
list.append(2);
list.append(3);
list.prepend(0);
list.print();
console.log('List size ', list.getSize());

list.removeFromFront();
list.print();

list.removeFromEnd();
list.print();

list.removeFromFront();
list.print();

list.removeFromFront();
list.print();