class Graph {
  constructor() {
    this.adjacentList = {};
  }

  addVertex(vertex) {
    if (!this.adjacentList[vertex]) {
      // I could've used an array instead of Set, but Set has better performance
      this.adjacentList[vertex] = new Set();
    }
  }

  addEdge(vertex1, vertex2) {
    if (!this.adjacentList[vertex1]) {
      this.addVertex(vertex1);
    }

    if (!this.adjacentList[vertex2]) {
      this.addVertex(vertex2);
    }

    // undirected graph so vertex1 is connected to vertex2
    // and vertex2 is connected to vertex1 in the same way
    this.adjacentList[vertex1].add(vertex2);
    this.adjacentList[vertex2].add(vertex1);
  }

  hasEdge(vertex1, vertex2) {
    return this.adjacentList[vertex1].has(vertex2)
      && this.adjacentList[vertex2].has(vertex1);
  }

  display() {
    for(const vertex in this.adjacentList) {
      console.log(vertex + " -> " + [...this.adjacentList[vertex]]);
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