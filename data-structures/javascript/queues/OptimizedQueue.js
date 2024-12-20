class OptimizedQueue {
  constructor() {
    this.items = {};
    this.rear = 0;
    this.front = 0;
  }

  enqueue(item) {
    // O(1) time
    this.items[this.rear] = item;
    this.rear++;
  }

  dequeue() {
    // O(1) time
    const item = this.items[this.front];
    delete this.items[this.front];
    this.front++;
    return item;
  }

  isEmpty() {
    return this.rear - this.front === 0;
  }

  size() {
    return this.rear - this.front;
  }

  peek() {
    return this.items[this.front];
  }

  print() {
    console.log(this.items);
  }
}

const queue = new OptimizedQueue();
console.log(queue.isEmpty());

queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
console.log(queue.size());
queue.print();

console.log(queue.dequeue());
console.log(queue.peek() === 20)
console.log(queue.dequeue());
console.log(queue.peek() === 30)