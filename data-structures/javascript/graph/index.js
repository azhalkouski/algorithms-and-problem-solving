//    A  B  C
// A  0  1  0
// B  1  0  1
// C  0  1  0

// The adjacency matrix above tells us that we have a undirected graph which has
// three verices. A is connected to B. B is connected to C. C is not connected to A.
// B is connected to A in the same way A is connected to B.
// C is connected to B in the same way B is connected to C.

const matrix = [
  [0, 1, 0],
  [1, 0, 1],
  [0, 1, 0]
];

console.log(matrix[0][0]); // A is NOT connected to itself
console.log(matrix[0][1]); // A is connected to B
console.log(matrix[0][2]); // A is NOT connected to C
