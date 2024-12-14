class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  isEmpty() {
    return this.root === null;
  }

  insert(value) {
    const newNode = new Node(value);

    if (this.isEmpty()) {
      this.root = newNode;
    } else {
      this._insertNode(this.root, newNode)
    }
  }

  /**
   * Private method
   */
  _insertNode(root, newNode) {
    if (newNode.value < root.value) {
      if (root.left === null) {
        root.left = newNode;
      } else {
        this._insertNode(root.left, newNode);
      }
    } else {
      if (root.right === null) {
        root.right = newNode;
      } else {
        this._insertNode(root.right, newNode);
      }
    }
  }

  search(root, value) {
    if (!root) {
      return false;
    } else {
      if (root.value === value) {
        return true;
      } else if (value < root.value) {
        return this.search(root.left, value);
      } else {
        return this.search(root.right, value)
      }
    }
  }

  // `preorder()` method is one of three ways to implement Depth First Search
  preorder(root) {
    if (root) {
      console.log(root.value);
      this.preorder(root.left);
      this.preorder(root.right);
    }
  }

  // `inorder()` method is one of three ways to implement Depth First Search
  inorder(root) {
    if (root) {
      this.inorder(root.left);
      console.log(root.value);
      this.inorder(root.right);
    }
  }

  // `postorder()` method is one of three ways to implement Depth First Search
  postorder(root) {
    if (root) {
      this.postorder(root.left);
      this.postorder(root.right);
      console.log(root.value);
    }
  }

  // Breadth First Search algorithm
  levelOrder() {
    // Step 1 - create a queue
    /**
    * I am using array for simplicity. However, an array is definitely not
    * the best choice due to its linear time complexity.
    * A better option is to use optimised queue which leverages a javascript
    * object with two pointers: `front` and `rear`, and thus, achieve O(1) complexity.
    * Here I just don't want to link another file to this file.
    */
    const queue = [];

    // Step 2 - enqueue the root node
    queue.push(this.root);

    // As long as the queue is not empty, perform a set of operations
    while (queue.length) {
      // a. dequeue the node from the queue
      let curr = queue.shift();
      // b. read the node's value
      console.log(curr.value);
      // c. enqueue the node's left child if it exists
      if (curr.left) {
        queue.push(curr.left);
      }
      // d. enqueue the node's right child if it exists
      if (curr.right) {
        queue.push(curr.right);
      }
    }
  }
}


const bst = new BinarySearchTree();

console.log("BST is empty: ", bst.isEmpty());

bst.insert(10);
bst.insert(5);
bst.insert(15);
bst.insert(3);
bst.insert(7);

// bst.preorder(bst.root);
// console.log("");
// bst.inorder(bst.root);
// console.log("");
// bst.postorder(bst.root);

// console.log(bst.search(bst.root, 10));
// console.log(bst.search(bst.root, 5));
// console.log(bst.search(bst.root, 15));

// console.log(bst.search(bst.root, 20));

bst.levelOrder();