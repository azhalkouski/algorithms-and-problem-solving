/**
 * O(n) Time
 * O(1) Space
 * @param {number} n
 */
function factorial(n) {
  if (n === 0 || n === 1) {
    return 1;
  }

  let factorial = n;
  for (let i = n - 1; i > 1; i--) {
    factorial = factorial * i;
  }
  return factorial;
}

console.log(factorial(0) === 1);
console.log(factorial(1) === 1);
console.log(factorial(2) === 2);
console.log(factorial(3) === 6);
console.log(factorial(4) === 24);
console.log(factorial(5) === 120);
