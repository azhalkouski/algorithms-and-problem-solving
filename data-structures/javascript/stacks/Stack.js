class Stack {
  constructor() {
    this.items = [];
  }

  push(item) {
    // O(1) time
    this.items.push(item);
  }

  pop() {
    // O(1) time
    return this.items.pop();
  }

  peek() {
    return this.items[this.items.length-1];
  }

  isEmpty() {
    return this.items.length === 0;
  }

  size() {
    return this.items.length;
  }
}

const stack = new Stack();

console.log(stack.isEmpty());

stack.push(10);
stack.push(20);
stack.push(30);

console.log(stack.isEmpty());
console.log(stack.size());

console.log(stack.pop()); // removes 30 as it was the last added item
console.log(stack.pop()); // 20 as it was added before 30

console.log(stack.peek() === 10);