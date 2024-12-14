const adjacencyList = {
  'A': ['B'],
  'B': ['A', 'C'],
  'C': ['B'],
};

// get the list of all the nodes A is connected to
console.log(adjacencyList['A']);
// get the list of all the nodes B is connected to
console.log(adjacencyList['B']);
