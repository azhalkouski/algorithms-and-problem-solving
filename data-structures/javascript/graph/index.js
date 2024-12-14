class Graph {
  constructor() {
    this.adjacencyList = {};
  }

  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) {
      // I could've used an array instead of Set, but Set has better performance
      this.adjacencyList[vertex] = new Set();
    }
  }

  addEdge(vertex1, vertex2) {
    if (!this.adjacencyList[vertex1]) {
      this.addVertex(vertex1);
    }

    if (!this.adjacencyList[vertex2]) {
      this.addVertex(vertex2);
    }

    // undirected graph so vertex1 is connected to vertex2
    // and vertex2 is connected to vertex1 in the same way
    this.adjacencyList[vertex1].add(vertex2);
    this.adjacencyList[vertex2].add(vertex1);
  }

  removeEdge(vertex1, vertex2) {
    // .delete is the built-in method of Set data structure
    this.adjacencyList[vertex1].delete(vertex2);
    this.adjacencyList[vertex2].delete(vertex1);
  }

  removeVertex(vertex) {
    if (!this.adjacencyList[vertex]) {
      return;
    }

    for (const adjacentVertex of this.adjacencyList[vertex]) {
      this.removeEdge(vertex, adjacentVertex)
    }

    delete this.adjacencyList[vertex];
  }

  hasEdge(vertex1, vertex2) {
    return this.adjacencyList[vertex1].has(vertex2)
      && this.adjacencyList[vertex2].has(vertex1);
  }

  display() {
    for(const vertex in this.adjacencyList) {
      console.log(vertex + " -> " + [...this.adjacencyList[vertex]]);
    }
  }
}

const graph = new Graph();

graph.addVertex('A');
graph.addVertex('B');
graph.addVertex('C');

graph.addEdge('A', 'B');
graph.addEdge('B', 'C');

graph.display();

console.log(graph.hasEdge('A', 'B'));
console.log(graph.hasEdge('A', 'C'));

// graph.removeEdge("A", "B");
graph.removeVertex("B");
graph.display();