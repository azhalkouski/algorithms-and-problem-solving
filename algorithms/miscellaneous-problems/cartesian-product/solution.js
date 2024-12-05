// O(nm)
function cartesianProduct(arrA, arrB) {
  const product = [];

  for (let i = 0; i < arrA.length; i++) {
    for (let j = 0; j < arrB.length; j++) {
      product.push([arrA[i], arrB[j]]);
    }
  }

  return product;
}

console.log(cartesianProduct([1,2], [3,4]).toString() === "1,3,1,4,2,3,2,4");
console.log(cartesianProduct([1,2], [3,4,5]).toString() === "1,3,1,4,1,5,2,3,2,4,2,5");