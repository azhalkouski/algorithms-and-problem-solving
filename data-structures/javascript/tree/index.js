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


}


const bst = new BinarySearchTree();

console.log("BST is empty: ", bst.isEmpty());

bst.insert(10);
bst.insert(5);
bst.insert(15);