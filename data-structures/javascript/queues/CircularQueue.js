class CircularQueue {
  constructor(capacity) {
    this.items = new Array(capacity);
    this.capacity = capacity;
    this.currentLength = 0;
    this.rear = -1;
    this.front = -1;
  }

  isFull() {
    return this.currentLength === this.capacity;
  }

  isEmpty() {
    return this.currentLength === 0;
  }

  enqueue(element) {
    if (!this.isFull()) {
      // when we have capacity of 5, and we dequeued an element from position 0
      // and we now can enqueue another element, this.rear should not point to
      // 4+1 = 5 since the length of the queue is 5 and there is no position at
      // index 5. thus, (4+1) % 5 = 0 and we insert into position this.items[0]
      this.rear = (this.rear + 1) % this.capacity;
      this.items[this.rear] = element;
      this.currentLength += 1;
      if (this.front === -1) {
        this.front = this.rear; // this will be index 0 when we first insert
      }
    }
  }

  dequeue() {
    if (this.isEmpty()) {
      return null;
    }

    const item = this.items[this.front];
    this.items[this.front] = null;
    // increment front so as to dequeue next element
    this.front = (this.front + 1) % this.capacity;
    this.currentLength -= 1;
    if (this.isEmpty()) {
      this.front = -1;
      this.rear = -1;
    }

    return item;
  }

  peek() {
    if (!this.isEmpty()) {
      return this.items[this.front];
    } else {
      return null;
    }
  }

  print() {
    if (this.isEmpty()) {
      console.log('Queue is empty');
    } else {
      let i;
      let str = "";
      for (i = this.front; i !== this.rear; i = (i+1) % this.capacity) {
        str += this.items[i] + " ";
      }
      str += this.items[i];
      console.log(str);
    }
  }
}

const queue = new CircularQueue(5);
console.log(queue.isEmpty());

queue.enqueue(10);
queue.enqueue(20);
queue.enqueue(30);
queue.enqueue(40);
queue.enqueue(50);

console.log(queue.isFull());
queue.print();

console.log(queue.dequeue());
console.log(queue.peek());
queue.print();

queue.enqueue(60);
queue.print();

